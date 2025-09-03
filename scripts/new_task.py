#!/usr/bin/env python
from __future__ import annotations

import argparse
import re
import shutil
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def kebab(s: str) -> str:
    s = s.strip().lower()
    s = re.sub(r"[^a-z0-9]+", "-", s)
    return re.sub(r"-+", "-", s).strip("-")


def render(tpl_path: Path, **kw) -> str:
    tpl = tpl_path.read_text()
    return tpl.format(**kw)


def main() -> None:
    ap = argparse.ArgumentParser(description="Create a LeetCode problem skeleton")
    ap.add_argument("slug", help="leetcode slug, e.g., two-sum")
    ap.add_argument("number", type=int, help="problem number, e.g., 1")
    ap.add_argument("--title", help="human title, default from slug", default=None)
    ap.add_argument("--difficulty", choices=["easy", "medium", "hard"], default="easy")
    ap.add_argument("--tags", default="")
    ap.add_argument("--url", default="")
    args = ap.parse_args()

    slug = kebab(args.slug)
    title = args.title or slug.replace("-", " ").title()
    dirname = f"{args.number:04d}-{slug}"
    base = ROOT / "problems" / dirname
    if base.exists():
        shutil.rmtree(base)
    base.mkdir(parents=True, exist_ok=True)

    context = dict(
        number=args.number,
        title=title,
        difficulty=args.difficulty,
        tags=args.tags,
        url=args.url or f"https://leetcode.com/problems/{slug}/",
        slug=slug,
        dirname=dirname,
        created=datetime.utcnow().isoformat(timespec="seconds") + "Z",
    )

    # multi-solution scaffold (consolidated file in problem root)
    variant_tpl = ROOT / "templates" / "solutions_multi.py.tpl"
    (base / "solutions.py").write_text(render(variant_tpl, **context))

    # problem README with standardized Files section
    problem_readme_tpl = ROOT / "templates" / "problem_readme.md.tpl"
    (base / "readme.md").write_text(render(problem_readme_tpl, **context))
    link_path = base / f"{args.number:04d}.readme.md"
    if link_path.exists():
        link_path.unlink()
    link_path.symlink_to("readme.md")

    # no package marker; tests load solution via runpy, not imports

    print(f"Created {base.relative_to(ROOT)}")
    print("Next:")
    print(f"  - Edit {base / 'solutions.py'} and add classes to ALL_SOLUTIONS")
    print("  - Add TEST_CASES in solutions.py; run: pytest -q")


if __name__ == "__main__":
    main()
