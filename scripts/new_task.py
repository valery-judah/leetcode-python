
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
    ap.add_argument("--difficulty", choices=["easy","medium","hard"], default="easy")
    ap.add_argument("--tags", default="")
    ap.add_argument("--url", default="")
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
        created=datetime.utcnow().isoformat(timespec="seconds") + "Z",
    )

    # README
    (base / "README.md").write_text(render(ROOT / "templates" / "README.md.tpl", **context))

    # solution.py
    (base / "solution.py").write_text(render(ROOT / "templates" / "solution.py.tpl", **context))

    # tests
    tests_dir = base
    (tests_dir / "test_solution.py").write_text(render(ROOT / "templates" / "test_solution.py.tpl", **context))

    # package marker for pytest discovery
    (base / "__init__.py").write_text("")

    print(f"Created {base.relative_to(ROOT)}")
    print("Next:")
    print(f"  - Edit {base/'solution.py'} and {base/'test_solution.py'}")
    print("  - Run: pytest -q")

if __name__ == "__main__":
    main()
