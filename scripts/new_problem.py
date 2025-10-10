#!/usr/bin/env python
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

import leetcode_index

ROOT = Path(__file__).resolve().parents[1]
try:
    # Local helper for converting LeetCode meta types to Python annotations
    from common.testgen import generate_test_cases_from_signature

    from .meta_types import py_type_from_meta
    from .parser import parse_meta
except Exception:  # pragma: no cover - allow running as a script
    # Fallback when executed directly: import via sys.path manipulation
    import sys as _sys

    here = Path(__file__).parent
    _sys.path.insert(0, str(here))
    _sys.path.insert(0, str(here.parent / "common"))
    from meta_types import py_type_from_meta
    from parser import parse_meta
    from testgen import generate_test_cases_from_signature

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


def _max_line_length(default: int = 110) -> int:
    """Return configured max line length from pyproject.toml, else default.

    Prefers `[tool.ruff].line-length`, then `[tool.black].line-length`.
    Falls back to `default` when unavailable.
    """
    try:
        txt = (ROOT / "pyproject.toml").read_text()
    except Exception:
        return default
    import re as _re

    m = _re.search(r"(?ms)^\[tool\.ruff\].*?^line-length\s*=\s*(\d+)", txt)
    if m:
        return int(m.group(1))
    m = _re.search(r"(?ms)^\[tool\.black\].*?^line-length\s*=\s*(\d+)", txt)
    if m:
        return int(m.group(1))
    m = _re.search(r"(?m)^line-length\s*=\s*(\d+)", txt)
    return int(m.group(1)) if m else default


def _extract_constraints_md(content_html: str | None) -> str:
    """Extract constraints list items from problem HTML and render as bullets.

    - Preserves exponents: 10<sup>5</sup> -> 10^5
    - HTML entities are unescaped.
    Returns 'None' when not found.
    """
    if not content_html:
        return "None"
    import re
    from html import unescape

    html = content_html
    # Locate the constraints list (<strong>Constraints:</strong> ... <ul> ... </ul>)
    m = re.search(r"<strong>\s*Constraints\s*:</strong>.*?<ul>(.*?)</ul>", html, re.IGNORECASE | re.DOTALL)
    if not m:
        return "None"
    ul = m.group(1)
    # Replace <sup>x</sup> with ^x
    ul = re.sub(r"<\s*sup\s*>(.*?)<\s*/\s*sup\s*>", r"^\1", ul, flags=re.IGNORECASE | re.DOTALL)
    # Extract list items
    items = re.findall(r"<\s*li\s*>(.*?)<\s*/\s*li\s*>", ul, flags=re.IGNORECASE | re.DOTALL)
    lines: list[str] = []
    for it in items:
        # Strip remaining tags
        text = re.sub(r"<[^>]+>", "", it)
        text = unescape(text).strip()
        if text:
            lines.append(f"- `{text}`")
    return "\n".join(lines) if lines else "None"


def _extract_examples_md(content_html: str | None) -> str:
    """Extract all example <pre> blocks and render them as fenced code snippets.

    Each example is labeled as "Example i" in order of appearance.
    Braces are escaped to avoid str.format issues in templates.
    Returns 'None' when not found.
    """
    if not content_html:
        return "None"
    import re
    from html import unescape

    blocks = re.findall(r"<pre>(.*?)</pre>", content_html, re.IGNORECASE | re.DOTALL)
    if not blocks:
        return "None"
    parts: list[str] = []
    for i, blob in enumerate(blocks, start=1):
        # Remove any residual HTML inside pre
        text = re.sub(r"<[^>]+>", "", blob)
        text = unescape(text).strip()
        text = text.replace("{", "{{").replace("}", "}}")
        parts.append(f"### Example {i}\n\n```text\n{text}\n```")
    return "\n\n".join(parts) if parts else "None"


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
    from datetime import UTC, datetime

    return datetime.now(UTC).isoformat(timespec="seconds").replace("+00:00", "Z")


# --- Field normalization helpers (to support schema variants) ---
def _get_id(d: dict) -> str:
    """Return the visible LeetCode problem number as a string.

    Prefer the explicit frontend number when present (`questionFrontendId` or
    `frontendQuestionId`), else fall back to `id`, else `questionId`.
    Returns empty string when not resolvable.
    """
    val = (
        d.get("questionFrontendId") or d.get("frontendQuestionId") or d.get("id") or d.get("questionId") or ""
    )
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
    import argparse

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


def _resolve_problem(query: str) -> tuple[dict | None, int | None, str | None]:
    """Resolve a problem by id/slug, first from leetcode_index, then archive."""
    problem = None
    problem_id_resolved = None
    slug_resolved = None
    try:
        # Prioritize resolving from the index
        problem_id_resolved, slug_resolved = leetcode_index.resolve(int(query) if query.isdigit() else query)
        problem = _load_problem_from_archive(slug_resolved)
    except (KeyError, ValueError):
        # Fallback to archive-only if index fails
        problem = _load_problem_from_archive(query)
    except Exception as e:
        print(f"E: Unexpected error resolving problem '{query}': {e}", file=sys.stderr)
        problem = _load_problem_from_archive(query)

    if not problem:
        print(f"W: Problem '{query}' not found in leetcode_index or archive.", file=sys.stderr)
    return problem, problem_id_resolved, slug_resolved


def _render_similar_md(
    number: int,
    slug: str,
    similars: list,
) -> str:
    """Render the Similar Questions markdown table.

    Columns: Number | Difficulty | Name (repo link when available) | LeetCode link
    """
    import os

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
        resolved = _load_problem_from_archive(s_slug or s_id)
        if not s_id and resolved:
            s_id = _get_id(resolved)

        # Prefer difficulty provided on the similar item itself; else use resolved metadata
        s_diff = _normalize_difficulty(it.get("difficulty"))
        if not s_diff:
            s_diff = _normalize_difficulty((resolved or {}).get("difficulty")) if resolved else None
        if not s_diff and s_id and s_id in SIMILAR_DIFFICULTY_OVERRIDES:
            s_diff = SIMILAR_DIFFICULTY_OVERRIDES[s_id]

        # Build repo-relative link to the similar problem's readme when possible
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
        leet_col = f"[{s_title}]({s_url})" if s_url else ""

        rows.append(f"| {num_col} | {diff_col} | {name_col} | {leet_col} |")

    if rows:
        header = "| Number | Difficulty | Name | LeetCode |\n|---|---|---|---|"
        similar_md = header + "\n" + "\n".join(rows)
    return similar_md


def _build_context(
    problem: dict, resolved_id: int | None, resolved_slug: str | None
) -> tuple[dict, int, str, Path]:
    pid_str = _get_id(problem)
    try:
        # Prioritize the ID from the index resolver, as archive data may be inconsistent
        number = resolved_id if resolved_id is not None else int(pid_str)
    except (ValueError, TypeError) as e:
        raise SystemExit(f"Invalid problem id: {pid_str} (resolved: {resolved_id})") from e
    # Prioritize slug from index resolver
    slug = resolved_slug or _get_slug(problem)
    title = _get_title(problem, slug=slug)
    difficulty = _normalize_difficulty(problem.get("difficulty")) or "easy"
    tags_list = _get_tags(problem)
    tags = ", ".join(tags_list)
    url = _get_url(problem, slug)
    similar_md = _render_similar_md(number, slug, problem.get("similar_questions") or [])

    # Build signature preview from metaData when available
    def _signature_from_meta(p: dict) -> str:
        meta = parse_meta(p.get("metaData"))
        if not isinstance(meta, dict):
            return "`...` → `...`"
        params = meta.get("params")
        ret = None
        meta_ret = meta.get("return")
        if isinstance(meta_ret, dict):
            ret = meta_ret.get("type")
        elif isinstance(meta_ret, str):
            ret = meta_ret
        parts: list[str] = []
        if isinstance(params, list):
            for it in params:
                if not isinstance(it, dict):
                    continue
                nm = str(it.get("name") or "arg").strip() or "arg"
                ty = py_type_from_meta(str(it.get("type") or "object"))
                parts.append(f"{nm}: {ty}")
        rty = py_type_from_meta(str(ret or "object"))
        params_str = ", ".join(parts)
        arrow = " -> "
        signature_str = f"({params_str}) {arrow}{rty}"
        return f"`{signature_str}`"

    signature = _signature_from_meta(problem)
    # Function name (when available)
    meta_obj = parse_meta(problem.get("metaData"))
    function_name = (
        str(meta_obj.get("name")).strip() if isinstance(meta_obj, dict) and meta_obj.get("name") else ""
    )
    # Primary pattern heuristic from tags (pick the first known pattern)
    PATTERN_PRIORITY = [
        "Sliding Window",
        "Two Pointers",
        "Binary Search",
        "Graph",
        "Tree",
        "Heap (Priority Queue)",
        "Stack",
        "Monotonic Stack",
        "Greedy",
        "Dynamic Programming",
        "Backtracking",
        "Hash Table",
        "Sorting",
        "Prefix Sum",
        "Queue",
        "Linked List",
        "Math",
        "Bit Manipulation",
    ]
    primary_pattern = next(
        (t for t in PATTERN_PRIORITY if t in tags_list),
        (tags_list[0] if tags_list else ""),
    )
    # Constraints and Examples from content
    content_html = str(problem.get("content") or "")
    constraints_md = _extract_constraints_md(content_html)
    examples_md = _extract_examples_md(content_html)
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
        similar_md=similar_md,
        signature=signature,
        function_name=function_name,
        primary_pattern=primary_pattern or "",
        constraints_md=constraints_md,
        examples_md=examples_md,
    )
    return context, number, slug, base


def _ensure_base_dir(base: Path, *, full_rewrite: bool) -> None:
    import shutil

    if base.exists():
        if full_rewrite:
            shutil.rmtree(base)
            base.mkdir(parents=True, exist_ok=True)
    else:
        base.mkdir(parents=True, exist_ok=True)


def _determine_type_imports(params: list[tuple[str, str]], ret_type: str) -> str:
    """Determine which common types to import based on signature."""
    needed: set[str] = set()

    def _collect_needed(t: str) -> None:
        if re.search(r"\bListNode\b", t):
            needed.add("ListNode")
        if re.search(r"\bTreeNode\b", t):
            needed.add("TreeNode")
        if re.search(r"\bUndirectedGraphNode\b", t):
            needed.add("UndirectedGraphNode")
        if re.search(r"\bRandomListNode\b", t):
            needed.add("RandomListNode")
        if re.search(r"\bNestedInteger\b", t):
            needed.add("NestedInteger")
        # Plain Node (avoid clashes with ListNode/TreeNode)
        if (
            re.search(r"\bNode\b", t)
            and not re.search(r"\bListNode\b", t)
            and not re.search(r"\bTreeNode\b", t)
            and not re.search(r"\bUndirectedGraphNode\b", t)
            and not re.search(r"\bRandomListNode\b", t)
        ):
            needed.add("Node")

    for _, t in params:
        _collect_needed(t)
    _collect_needed(ret_type)

    import_names = [
        n
        for n in [
            "ListNode",
            "TreeNode",
            "Node",
            "UndirectedGraphNode",
            "RandomListNode",
            "NestedInteger",
        ]
        if n in needed
    ]
    if import_names:
        names_joined = ", ".join(import_names)
        return f"from common.types import {names_joined}"
    return ""


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
    meta = parse_meta(problem.get("metaData") if isinstance(problem, dict) else None)
    content: str
    if isinstance(meta, dict) and (params_list := meta.get("params")) and isinstance(params_list, list):
        params = []
        for p in params_list:
            if not isinstance(p, dict):
                continue
            pname = kebab(str(p.get("name") or "arg")).replace("-", "_") or "arg"
            ptype = py_type_from_meta(str(p.get("type") or ""))
            params.append((pname, ptype))
        meta_ret = meta.get("return")
        r_raw = None
        if isinstance(meta_ret, dict):
            r_raw = meta_ret.get("type")
        elif isinstance(meta_ret, str):
            r_raw = meta_ret
        ret_type = py_type_from_meta(str(r_raw or "object"))
        # Add default values for stub testing
        # Ensure parameter names are unique to avoid invalid syntax like
        # "inputs, inputs" when LC metadata has duplicate names.
        seen: dict[str, int] = {}
        deduped_params: list[tuple[str, str]] = []
        for n, t in params:
            count = seen.get(n, 0) + 1
            seen[n] = count
            name = f"{n}_{count}" if count > 1 else n
            deduped_params.append((name, t))

        sig_params_parts = []
        for n, t in deduped_params:
            sig_params_parts.append(f"{n}: {t}")
        type_imports: str = _determine_type_imports(params, ret_type)
        generated_cases: str = generate_test_cases_from_signature(params, ret_type)
        # Prefer single-line signature when short; otherwise use multi-line for readability (E501).
        # Template provides 4 spaces indentation before this block.
        if sig_params_parts:
            single_params = ", ".join(sig_params_parts)
            single_line_sig = f"def solve(self, {single_params}) -> {ret_type}:"
        else:
            single_line_sig = f"def solve(self) -> {ret_type}:"

        max_len = _max_line_length(110)
        # Account for 4 spaces of indentation present in the template.
        if 4 + len(single_line_sig) <= max_len:
            solve_signature = single_line_sig
        else:
            # Multi-line fallback; indent continuation lines by 8 spaces
            if sig_params_parts:
                cont = "\n".join(["        self,", *[f"        {p}," for p in sig_params_parts]])
            else:
                cont = "        self,"
            # Closing paren aligns with the 'def' indent (4 spaces inside class)
            solve_signature = "def solve(\n" f"{cont}\n" f"    ) -> {ret_type}:"

        context["import_types"] = f"\n{type_imports}" if type_imports else ""
        context["generated_cases"] = generated_cases
        context["solve_signature"] = solve_signature
        tpl_text = render(variant_tpl, **context)
        if not tpl_text.lstrip().startswith("from __future__ import annotations"):
            tpl_text = "from __future__ import annotations\n\n" + tpl_text
        content = tpl_text
    else:
        context["import_types"] = ""
        context["generated_cases"] = "TEST_CASES = []"
        context["solve_signature"] = "def solve(self, *args, **kwargs):"
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


def _write_content_html(
    base: Path,
    number: int,
    slug: str,
    problem: dict,
    *,
    full_rewrite: bool,
    rewrite_files: bool,
) -> None:
    """Write a renderable HTML page for the LeetCode `content`.

    Produces `NNNN-slug-content.html` that wraps the raw LeetCode HTML fragment
    into a full HTML document and links a shared stylesheet at
    `../../common/leetcode-content.css`.
    """
    try:
        content = problem.get("content") if isinstance(problem, dict) else None
        if not content:
            return

        # Derive bits for title and link
        title = _get_title(problem, slug=slug)
        lc_url = _get_url(problem, slug)

        # Build full HTML document with a link to the shared CSS
        css_href = "../../common/leetcode-content.css"
        doc = (
            "<!doctype html>\n"
            '<html lang="en">\n'
            "<head>\n"
            '  <meta charset="utf-8">\n'
            '  <meta name="viewport" content="width=device-width, initial-scale=1">\n'
            f"  <title>{number:04d}. {title}</title>\n"
            f'  <link rel="stylesheet" href="{css_href}">\n'
            "</head>\n"
            "<body>\n"
            '  <main class="lc-content">\n'
            f"    <!-- Source: {lc_url} -->\n"
            f"{content}\n"
            "  </main>\n"
            "</body>\n"
            "</html>\n"
        )

        out_path = base / f"{number:04d}-{slug}-content.html"
        if (not out_path.exists()) or full_rewrite or rewrite_files:
            out_path.write_text(doc)
    except Exception:
        # Best‑effort; avoid breaking scaffold creation if content write fails
        pass


def main() -> None:
    args = _parse_args()

    q = args.query.strip()
    problem, resolved_id, resolved_slug = _resolve_problem(q)
    if not problem:
        raise SystemExit(f"Problem not found by query: {q}")

    # Build context and target base dir
    context, number, slug, base = _build_context(
        problem, resolved_id=resolved_id, resolved_slug=resolved_slug
    )

    full_rewrite = bool(args.full_rewrite)
    rewrite_files = not bool(args.no_overwrite)
    _ensure_base_dir(base, full_rewrite=full_rewrite)

    # Write outputs
    _write_solutions(base, problem, context, full_rewrite=full_rewrite, rewrite_files=rewrite_files)
    _write_readme_and_symlink(base, context, number, full_rewrite=full_rewrite, rewrite_files=rewrite_files)
    _write_problem_json(base, number, problem, full_rewrite=full_rewrite, rewrite_files=rewrite_files)
    _write_stats(base, full_rewrite=full_rewrite, rewrite_files=rewrite_files)
    _write_content_html(base, number, slug, problem, full_rewrite=full_rewrite, rewrite_files=rewrite_files)

    print(f"Created {base.relative_to(ROOT)}")
    print("Next:")
    print(f"  - Edit {(base / 'solutions.py').relative_to(ROOT)} and add classes to ALL_SOLUTIONS")
    print("  - Add TEST_CASES in solutions.py; run: pytest -q")


if __name__ == "__main__":
    main()
