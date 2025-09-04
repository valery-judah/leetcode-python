#!/usr/bin/env python
from __future__ import annotations

import argparse
import json
import re
import shutil
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

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


def main() -> None:
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
    args = ap.parse_args()

    by_id, by_slug = _load_problems_index()

    q = args.query.strip()
    is_id = q.isdigit()
    problem = by_id.get(q) if is_id else by_slug.get(kebab(q))

    if not problem:
        raise SystemExit(f"Problem not found in lists by {'id' if is_id else 'slug'}: {q}")

    # Extract fields
    pid_str = str(problem.get("id") or "").strip()
    try:
        number = int(pid_str)
    except ValueError:
        raise SystemExit(f"Invalid problem id: {pid_str}")
    slug = kebab(str(problem.get("slug") or ""))
    title = str(problem.get("name") or slug.replace("-", " ").title())
    difficulty = _normalize_difficulty(problem.get("difficulty")) or "easy"
    tags_list = problem.get("tags") or []
    if isinstance(tags_list, list):
        tags = ", ".join(tags_list)
    else:
        tags = str(tags_list)
    url = str(problem.get("leetcode_url") or f"https://leetcode.com/problems/{slug}/")
    # Prepare similar questions markdown list
    similar_md = "None"
    similars = problem.get("similar_questions") or []
    if isinstance(similars, list) and similars:
        items: list[str] = []
        for it in similars:
            if not isinstance(it, dict):
                continue
            title = str(it.get("title") or it.get("name") or "").strip() or "Related"
            s_slug = kebab(str(it.get("slug") or ""))
            s_url = str(it.get("leetcode_url") or (f"https://leetcode.com/problems/{s_slug}/" if s_slug else ""))
            # Try to resolve difficulty from lists by id/slug
            s_id = str(it.get("id") or "").strip()
            resolved = None
            if s_id and s_id in by_id:
                resolved = by_id[s_id]
            elif s_slug and s_slug in by_slug:
                resolved = by_slug[s_slug]
            s_diff = _normalize_difficulty((resolved or {}).get("difficulty")) if resolved else None
            if not s_diff and s_id and s_id in SIMILAR_DIFFICULTY_OVERRIDES:
                s_diff = SIMILAR_DIFFICULTY_OVERRIDES[s_id]
            diff_label = f"[{s_diff.title()}] " if s_diff else ""
            if s_url:
                items.append(f"- {diff_label}[{title}]({s_url})")
            else:
                items.append(f"- {diff_label}{title}")
        if items:
            similar_md = "\n".join(items)

    dirname = f"{number:04d}-{slug}"
    base = ROOT / "problems" / dirname

    # Determine rewrite mode. Default is in-place rewrite (no delete).
    full_rewrite = bool(args.full_rewrite)
    # default behavior: rewrite files unless user asks not to
    rewrite_files = not bool(args.no_overwrite)
    if base.exists():
        if full_rewrite:
            shutil.rmtree(base)
            base.mkdir(parents=True, exist_ok=True)
        else:
            # reuse existing directory
            pass
    else:
        base.mkdir(parents=True, exist_ok=True)

    context = dict(
        number=number,
        title=title,
        difficulty=difficulty,
        tags=tags,
        url=url,
        slug=slug,
        dirname=dirname,
        created=datetime.utcnow().isoformat(timespec="seconds") + "Z",
        similar_md=similar_md,
    )

    # multi-solution scaffold (consolidated file in problem root)
    variant_tpl = ROOT / "templates" / "solutions_multi.py.tpl"
    solutions_path = base / "solutions.py"
    if (not solutions_path.exists()) or full_rewrite or rewrite_files:
        solutions_path.write_text(render(variant_tpl, **context))

    # problem README with standardized Files section
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

    # dump raw problem info alongside, for reference/automation
    problem_json_path = base / f"{number:04d}-problem.json"
    try:
        if (not problem_json_path.exists()) or full_rewrite or rewrite_files:
            problem_json_path.write_text(json.dumps(problem, indent=2, ensure_ascii=False) + "\n")
    except Exception:
        pass

    # no package marker; tests load solution via runpy, not imports

    print(f"Created {base.relative_to(ROOT)}")
    print("Next:")
    print(f"  - Edit {base / 'solutions.py'} and add classes to ALL_SOLUTIONS")
    print("  - Add TEST_CASES in solutions.py; run: pytest -q")


if __name__ == "__main__":
    main()
