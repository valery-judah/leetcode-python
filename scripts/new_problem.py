#!/usr/bin/env python
from __future__ import annotations

import argparse
import json
import os
import re
import shutil
from datetime import UTC, datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
try:
    # Local helper for converting LeetCode meta types to Python annotations
    from .meta_types import py_type_from_meta  # type: ignore
    from .testgen import make_stub_cases  # type: ignore
except Exception:  # pragma: no cover - allow running as a script
    # Fallback when executed directly: import via sys.path manipulation
    import sys as _sys

    here = Path(__file__).parent
    _sys.path.insert(0, str(here))
    _sys.path.insert(0, str(here.parent / "common"))
    from meta_types import py_type_from_meta  # type: ignore
    from testgen import make_stub_cases  # type: ignore

# Manual corrections for difficulties when list sources omit them
SIMILAR_DIFFICULTY_OVERRIDES: dict[str, str] = {
    # id: difficulty (lowercase)
    "220": "hard",  # Contains Duplicate III
}


def kebab(s: str) -> str:
    s = s.strip().lower()
    s = re.sub(r"[^a-z0-9]+", "-", s)
    return re.sub(r"-+", "-", s).strip("-")


def render(tpl_path: Path, **kw) -> str:
    tpl = tpl_path.read_text()
    return tpl.format(**kw)


def _iter_list_files() -> list[Path]:
    lists_dir = ROOT / "lists"
    if not lists_dir.exists():
        return []
    return sorted(lists_dir.glob("*.json"))


def _load_problems_index() -> tuple[dict[str, dict], dict[str, dict]]:
    by_id: dict[str, dict] = {}
    by_slug: dict[str, dict] = {}
    for fp in _iter_list_files():
        try:
            data = json.loads(fp.read_text())
        except Exception:
            continue
        problems = data.get("problems")
        if not isinstance(problems, list):
            continue
        for item in problems:
            if not isinstance(item, dict):
                continue
            pid = str(item.get("id") or "").strip()
            slug = str(item.get("slug") or "").strip().lower()
            if not pid and not slug:
                continue
            if pid:
                existing = by_id.get(pid)
                if not existing:
                    by_id[pid] = item
                else:
                    # Prefer entry that has a concrete difficulty if existing lacks it
                    if (not existing.get("difficulty")) and item.get("difficulty"):
                        by_id[pid] = item
            if slug:
                existing_s = by_slug.get(slug)
                if not existing_s:
                    by_slug[slug] = item
                else:
                    if (not existing_s.get("difficulty")) and item.get("difficulty"):
                        by_slug[slug] = item
    return by_id, by_slug


def _normalize_difficulty(s: str | None) -> str | None:
    if not s:
        return None
    s = s.strip().lower()
    if s in {"easy", "medium", "hard"}:
        return s
    # Fallback map common variants
    mapping = {"e": "easy", "m": "medium", "h": "hard"}
    return mapping.get(s, s)


def _utc_now_iso_z() -> str:
    """Return current UTC time in ISO8601 with seconds precision and 'Z' suffix."""
    return datetime.now(UTC).isoformat(timespec="seconds").replace("+00:00", "Z")


# --- Field normalization helpers (to support schema variants) ---
def _get_id(d: dict) -> str:
    """Return the problem id as a string.

    Prefer `id`, else fall back to `questionFrontendId` or `questionId` when provided.
    Returns empty string when missing.
    """
    val = d.get("id") or d.get("questionFrontendId") or d.get("questionId") or ""
    return str(val).strip()


def _get_slug(d: dict) -> str:
    """Return the kebab-case slug.

    Prefer `slug`, else `titleSlug`, else derive from name/title.
    """
    raw = d.get("slug") or d.get("titleSlug") or d.get("name") or d.get("title") or ""
    return kebab(str(raw))


def _get_title(d: dict, slug: str | None = None) -> str:
    """Return the display title.

    Prefer `name`, else `title`, else title-cased slug.
    """
    title = d.get("name") or d.get("title")
    if title:
        return str(title)
    if slug:
        return slug.replace("-", " ").title()
    # Last resort if slug not given, recompute
    return _get_slug(d).replace("-", " ").title()


def _get_tags(d: dict) -> list[str]:
    """Return tags as a flat list of names.

    Prefer `tags` when it is a list[str]. Else map `topicTags` (list[dict]) → names.
    """
    tags = d.get("tags")
    if isinstance(tags, list) and (not tags or isinstance(tags[0], str)):
        # If empty or elements are strings, use as-is
        return [str(t) for t in tags]
    topic_tags = d.get("topicTags")
    if isinstance(topic_tags, list):
        names: list[str] = []
        for t in topic_tags:
            if isinstance(t, dict) and t.get("name"):
                names.append(str(t["name"]))
        return names
    return []


def _get_url(d: dict, slug: str) -> str:
    """Return LeetCode URL, falling back to the canonical slug URL."""
    return str(d.get("leetcode_url") or f"https://leetcode.com/problems/{slug}/")


def _load_problem_from_archive(query: str) -> dict | None:
    """Try to load a single problem JSON from archive/problems by id or slug.

    - If query is digits: match "{id:04d}-*.json"
    - Else: treat as slug: match "*-{slug}.json"
    Returns the parsed dict or None if not found or invalid.
    """
    apath = ROOT / "archive" / "problems"
    if not apath.exists():
        return None

    q = query.strip()
    try:
        patterns: list[str]
        if q.isdigit():
            patterns = [f"{int(q):04d}-*.json"]
        else:
            s = kebab(q)
            patterns = [f"*-{s}.json"] if s else []
    except Exception:
        return None

    for pat in patterns:
        matches = sorted(apath.glob(pat))
        if not matches:
            continue
        # Prefer the first sorted match (should be unique per id/slug)
        try:
            return json.loads(matches[0].read_text())
        except Exception:
            return None
    return None


def _parse_args() -> argparse.Namespace:
    ap = argparse.ArgumentParser(description="Create a LeetCode problem skeleton from lists by id or slug")
    ap.add_argument("query", help="leetcode id (e.g., 1) or slug (e.g., two-sum)")
    # Rewrite controls
    ap.add_argument(
        "--rewrite",
        action="store_true",
        help="rewrite files in place without deleting the directory",
    )
    ap.add_argument(
        "--full-rewrite",
        action="store_true",
        help="delete and recreate the directory (clobber).",
    )
    ap.add_argument(
        "--no-overwrite",
        action="store_true",
        help="do not overwrite existing files; only create missing ones",
    )
    return ap.parse_args()


def _resolve_problem(query: str, by_id: dict[str, dict], by_slug: dict[str, dict]) -> dict | None:
    is_id = query.isdigit()
    problem = _load_problem_from_archive(query)
    if not problem:
        problem = by_id.get(query) if is_id else by_slug.get(kebab(query))
    return problem


def _render_similar_md(
    number: int,
    slug: str,
    similars: list,
    by_id: dict[str, dict],
    by_slug: dict[str, dict],
) -> str:
    """Render the Similar Questions markdown table.

    Columns: Number | Difficulty | Name (repo link when available) | LeetCode link
    """
    similar_md = "None"
    if not (isinstance(similars, list) and similars):
        return similar_md
    rows: list[str] = []
    current_base = ROOT / "problems" / f"{number:04d}-{slug}"
    for it in similars:
        if not isinstance(it, dict):
            continue
        s_title = str(it.get("title") or it.get("name") or "").strip() or "Related"
        s_slug = kebab(str(it.get("slug") or ""))
        s_url = str(it.get("leetcode_url") or (f"https://leetcode.com/problems/{s_slug}/" if s_slug else ""))
        # Try to resolve difficulty and id from lists by id/slug or archive
        s_id = str(it.get("id") or "").strip()
        resolved = None
        if s_id and s_id in by_id:
            resolved = by_id[s_id]
        elif s_slug and s_slug in by_slug:
            resolved = by_slug[s_slug]
            if not s_id:
                s_id = str(resolved.get("id") or "").strip()
        if (not s_id) and s_slug:
            arch = _load_problem_from_archive(s_slug)
            if isinstance(arch, dict):
                s_id = str(arch.get("id") or "").strip()
                if not resolved:
                    resolved = arch

        # Prefer difficulty provided on the similar item itself; else use resolved metadata
        s_diff = _normalize_difficulty(it.get("difficulty"))
        if not s_diff:
            s_diff = _normalize_difficulty((resolved or {}).get("difficulty")) if resolved else None
        if not s_diff and s_id and s_id in SIMILAR_DIFFICULTY_OVERRIDES:
            s_diff = SIMILAR_DIFFICULTY_OVERRIDES[s_id]

        # Build repo-relative link to the similar problem's readme when possible
        link_md: str | None = None
        dirname_sim: str | None = None
        try:
            if s_id:
                dirname_sim = f"{int(s_id):04d}-{s_slug}" if s_slug else None
        except Exception:
            dirname_sim = None

        other_readme: Path | None = None
        if dirname_sim:
            other_readme = ROOT / "problems" / dirname_sim / "readme.md"
        else:
            # Try to locate by slug only under problems dir
            if s_slug:
                cands = sorted((ROOT / "problems").glob(f"*-{s_slug}"))
                if cands:
                    other_readme = cands[0] / "readme.md"

        # Prepare table columns
        try:
            num_col = f"{int(s_id):04d}" if s_id else ""
        except Exception:
            num_col = s_id or ""
        diff_col = s_diff.title() if s_diff else ""

        # Name column: repo-relative link when available, else plain title
        if other_readme is not None:
            rel = Path(os.path.relpath(other_readme, start=current_base)).as_posix()
            name_col = f"[{s_title}]({rel})"
        else:
            name_col = s_title

        # LeetCode link column
        leet_col = f"[link]({s_url})" if s_url else ""

        rows.append(f"| {num_col} | {diff_col} | {name_col} | {leet_col} |")

    if rows:
        header = "| Number | Difficulty | Name | LeetCode |\n|---|---|---|---|"
        similar_md = header + "\n" + "\n".join(rows)
    return similar_md


def _build_context(
    problem: dict, by_id: dict[str, dict], by_slug: dict[str, dict]
) -> tuple[dict, int, str, Path]:
    pid_str = _get_id(problem)
    try:
        number = int(pid_str)
    except ValueError as e:
        raise SystemExit(f"Invalid problem id: {pid_str}") from e
    slug = _get_slug(problem)
    title = _get_title(problem, slug=slug)
    difficulty = _normalize_difficulty(problem.get("difficulty")) or "easy"
    tags_list = _get_tags(problem)
    tags = ", ".join(tags_list)
    url = _get_url(problem, slug)
    similar_md = _render_similar_md(number, slug, problem.get("similar_questions") or [], by_id, by_slug)

    # Build signature preview from metaData when available
    def _signature_from_meta(p: dict) -> str:
        meta = p.get("metaData")
        if isinstance(meta, str):
            try:
                meta = json.loads(meta)
            except Exception:
                meta = None
        if not isinstance(meta, dict):
            return "`...` → `...`"
        params = meta.get("params")
        ret = (meta.get("return") or {}).get("type") if isinstance(meta.get("return"), dict) else None
        parts: list[str] = []
        if isinstance(params, list):
            for it in params:
                if not isinstance(it, dict):
                    continue
                nm = str(it.get("name") or "arg").strip() or "arg"
                ty = py_type_from_meta(str(it.get("type") or "object"))
                parts.append(f"`{nm}: {ty}`")
        rty = py_type_from_meta(str(ret or "object")) if ret is not None else "object"
        arrow = " → "
        return (", ".join(parts) if parts else "`...`") + arrow + f"`{rty}`"

    signature = _signature_from_meta(problem)
    dirname = f"{number:04d}-{slug}"
    base = ROOT / "problems" / dirname
    context = dict(
        number=number,
        title=title,
        difficulty=difficulty,
        tags=tags,
        url=url,
        slug=slug,
        dirname=dirname,
        created=_utc_now_iso_z(),
        similar_md=similar_md,
        signature=signature,
    )
    return context, number, slug, base


def _ensure_base_dir(base: Path, *, full_rewrite: bool) -> None:
    if base.exists():
        if full_rewrite:
            shutil.rmtree(base)
            base.mkdir(parents=True, exist_ok=True)
    else:
        base.mkdir(parents=True, exist_ok=True)


def _write_solutions(
    base: Path,
    problem: dict,
    context: dict,
    *,
    full_rewrite: bool,
    rewrite_files: bool,
) -> None:
    variant_tpl = ROOT / "templates" / "solutions_multi.py.tpl"
    solutions_path = base / "solutions.py"
    meta = problem.get("metaData") if isinstance(problem, dict) else None
    content: str
    if (
        isinstance(meta, dict)
        and (params_list := meta.get("params"))
        and isinstance(params_list, list)
        and meta.get("return")
    ):
        params = []
        for p in params_list:
            if not isinstance(p, dict):
                continue
            pname = kebab(str(p.get("name") or "arg")).replace("-", "_") or "arg"
            ptype = py_type_from_meta(str(p.get("type") or ""))
            params.append((pname, ptype))
        ret_type = py_type_from_meta(str((meta.get("return") or {}).get("type") or ""))
        sig_params = ", ".join(f"{n}: {t}" for n, t in params)
        # Start from rendered template (to normalize braces like {{}} -> {})
        tpl_text = render(variant_tpl, **context)
        tpl_text = tpl_text.replace(
            "def solve(self, *args, **kwargs):",
            f"def solve(self, {sig_params})-> {ret_type}:",
        )
        # Build typed TEST_CASES and comments via library helper
        stub_cases, comment_lines = make_stub_cases(params)

        # Materialize case tuple expressions using local value generator
        def _example_value(py_t: str) -> str:
            t = py_t.strip()
            if t.startswith("list[") and t.endswith("]"):
                inner = t[5:-1]
                return f"[{_example_value(inner)}]"
            if "ListNode" in t:
                return "ListNode(1, ListNode(2))"
            if "TreeNode" in t:
                return "TreeNode(1, TreeNode(2), TreeNode(3))"
            if "UndirectedGraphNode" in t:
                return "UndirectedGraphNode(1)"
            if "RandomListNode" in t:
                return "RandomListNode(1)"
            if "NestedInteger" in t:
                return "NestedInteger(1)"
            if t == "int":
                return "0"
            if t == "float":
                return "0.0"
            if t == "bool":
                return "False"
            if t == "str":
                return "'a'"
            if t == "None":
                return "None"
            return "None"

        def _tuple_expr(values: list[str]) -> str:
            if not values:
                return "()"
            if len(values) == 1:
                return f"({values[0]},)"
            return f"({', '.join(values)})"

        cases_lines: list[str] = []
        for label, raw_values in stub_cases:
            # raw_values are already expressions (strings)
            cases_lines.append(f'    ("{label}", {_tuple_expr(raw_values)}, {{}}),')
        generated_cases = "\n".join(comment_lines) + "\nTEST_CASES = [\n" + "\n".join(cases_lines) + "\n]"
        # Replace the default TEST_CASES block
        tc_start = tpl_text.find("TEST_CASES = [")
        if tc_start != -1:
            tc_end = tpl_text.find("\n]", tc_start)
            if tc_end != -1:
                tc_end += 2  # include closing bracket line
                # Prepend comments by replacing the block starting two lines above if possible
                # Otherwise, just replace the TEST_CASES array itself.
                tpl_text = tpl_text[:tc_start] + generated_cases + tpl_text[tc_end:]
        if not tpl_text.lstrip().startswith("from __future__ import annotations"):
            tpl_text = "from __future__ import annotations\n\n" + tpl_text
        content = tpl_text
    else:
        content = render(variant_tpl, **context)
    if (not solutions_path.exists()) or full_rewrite or rewrite_files:
        solutions_path.write_text(content)


def _write_readme_and_symlink(
    base: Path, context: dict, number: int, *, full_rewrite: bool, rewrite_files: bool
) -> None:
    problem_readme_tpl = ROOT / "templates" / "problem_readme.md.tpl"
    readme_path = base / "readme.md"
    if (not readme_path.exists()) or full_rewrite or rewrite_files:
        readme_path.write_text(render(problem_readme_tpl, **context))
    link_path = base / f"{number:04d}.readme.md"
    if link_path.exists():
        try:
            if link_path.is_symlink():
                target = link_path.resolve()
                if target != readme_path.resolve():
                    link_path.unlink()
                    link_path.symlink_to("readme.md")
            else:
                if full_rewrite or rewrite_files:
                    link_path.unlink()
                    link_path.symlink_to("readme.md")
        except FileNotFoundError:
            link_path.symlink_to("readme.md")
    else:
        link_path.symlink_to("readme.md")


def _write_problem_json(
    base: Path, number: int, problem: dict, *, full_rewrite: bool, rewrite_files: bool
) -> None:
    problem_json_path = base / f"{number:04d}-problem.json"
    try:
        if (not problem_json_path.exists()) or full_rewrite or rewrite_files:
            problem_json_path.write_text(json.dumps(problem, indent=2, ensure_ascii=False) + "\n")
    except Exception:
        pass


def _write_stats(base: Path, *, full_rewrite: bool, rewrite_files: bool) -> None:
    stats_path = base / "stats.json"
    stats_tpl = ROOT / "templates" / "stats.json.tpl"
    try:
        if (not stats_path.exists()) or full_rewrite or rewrite_files:
            stats_content = stats_tpl.read_text()
            if not stats_content.endswith("\n"):
                stats_content += "\n"
            stats_path.write_text(stats_content)
    except Exception:
        pass


def main() -> None:
    args = _parse_args()
    by_id, by_slug = _load_problems_index()

    q = args.query.strip()
    problem = _resolve_problem(q, by_id, by_slug)
    if not problem:
        raise SystemExit(f"Problem not found in lists by {'id' if q.isdigit() else 'slug'}: {q}")

    # Build context and target base dir
    context, number, slug, base = _build_context(problem, by_id, by_slug)

    full_rewrite = bool(args.full_rewrite)
    rewrite_files = not bool(args.no_overwrite)
    _ensure_base_dir(base, full_rewrite=full_rewrite)

    # Write outputs
    _write_solutions(base, problem, context, full_rewrite=full_rewrite, rewrite_files=rewrite_files)
    _write_readme_and_symlink(base, context, number, full_rewrite=full_rewrite, rewrite_files=rewrite_files)
    _write_problem_json(base, number, problem, full_rewrite=full_rewrite, rewrite_files=rewrite_files)
    _write_stats(base, full_rewrite=full_rewrite, rewrite_files=rewrite_files)

    print(f"Created {base.relative_to(ROOT)}")
    print("Next:")
    print(f"  - Edit {base / 'solutions.py'} and add classes to ALL_SOLUTIONS")
    print("  - Add TEST_CASES in solutions.py; run: pytest -q")


if __name__ == "__main__":
    main()
