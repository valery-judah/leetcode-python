#!/usr/bin/env python
from __future__ import annotations

import argparse
import re
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
    ap.add_argument(
        "--multi",
        action="store_true",
        help="scaffold a solutions/ folder and discovery test for multiple variants",
    )
    args = ap.parse_args()

    slug = kebab(args.slug)
    title = args.title or slug.replace("-", " ").title()
    dirname = f"{args.number:04d}-{slug}"
    base = ROOT / "tasks" / dirname
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

    # README
    readme_tpl = ROOT / "templates" / "README.md.tpl"
    (base / "README.md").write_text(render(readme_tpl, **context))

    if args.multi:
        # multi-solution scaffold
        sols_dir = base / "solutions"
        sols_dir.mkdir(exist_ok=True)

        # add a starter variant
        variant_tpl = ROOT / "templates" / "solution_variant.py.tpl"
        (sols_dir / "baseline.py").write_text(render(variant_tpl, **context))

        # discovery test with parametrized variants
        test_tpl = ROOT / "templates" / "test_multi_solutions.py.tpl"
        test_name = f"test_{args.number:04d}_{slug.replace('-', '_')}.py"
        (base / test_name).write_text(render(test_tpl, **context))
    else:
        # single-solution scaffold
        solution_tpl = ROOT / "templates" / "solution.py.tpl"
        (base / "solution.py").write_text(render(solution_tpl, **context))

        test_tpl = ROOT / "templates" / "test_solution.py.tpl"
        (base / "test_solution.py").write_text(render(test_tpl, **context))

    # no package marker; tests load solution via runpy, not imports

    print(f"Created {base.relative_to(ROOT)}")
    print("Next:")
    if args.multi:
        print(f"  - Add variants under {base/'solutions'} (export class Solution)")
        print(f"  - Edit tests in {base} matching 'test_*.py'")
    else:
        print(f"  - Edit {base/'solution.py'} and {base/'test_solution.py'}")
    print("  - Run: pytest -q")


if __name__ == "__main__":
    main()
