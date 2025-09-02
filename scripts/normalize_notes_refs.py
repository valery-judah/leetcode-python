#!/usr/bin/env python3
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

EXCLUDE_DIRS = {
    ".git",
    "venv",
    "htmlcov",
    "site",
    "old_leetcode",  # do not mass-edit legacy
}


def should_skip(path: Path) -> bool:
    parts = set(p.name for p in path.parents)
    return bool(parts & EXCLUDE_DIRS)


def replace_task_paths(text: str) -> str:
    # Replace legacy notes.md paths to task readme.md
    pattern = re.compile(r"`?tasks/(\d{4}-[^/]+?)/notes\.md`?")
    return pattern.sub(lambda m: f"tasks/{m.group(1)}/readme.md", text)


def replace_docs_language(text: str, rel: str) -> str:
    # Target only docs and templates wording changes
    if not (rel.startswith("docs/") or rel.startswith("templates/") or rel == "readme.md"):
        return text

    replacements: list[tuple[re.Pattern[str], str]] = [
        # Narrative phrasing
        (re.compile(r"notes\.md write-ups", re.IGNORECASE), "task README write-ups"),
        # Generic wording
        (re.compile(r"problem notes\.md", re.IGNORECASE), "problem README"),
        (re.compile(r"per[- ]task notes\.md", re.IGNORECASE), "per-task README"),
        # Action items and guidance
        (
            re.compile(r"Document the solution in notes\.md\.", re.IGNORECASE),
            "Document the solution in the README.",
        ),
        (
            re.compile(r"docstrings/notes\.md updates per task", re.IGNORECASE),
            "docstrings/README updates per task",
        ),
    ]

    out = text
    for pat, repl in replacements:
        out = pat.sub(repl, out)
    return out


def is_text_file(p: Path) -> bool:
    try:
        _ = p.read_text(encoding="utf-8")
        return True
    except Exception:
        return False


def main() -> int:
    changed = []
    for p in ROOT.rglob("*"):
        if not p.is_file():
            continue
        if should_skip(p):
            continue
        if p.name.endswith((".png", ".jpg", ".jpeg", ".gif", ".svg", ".ico")):
            continue
        if not is_text_file(p):
            continue

        rel = str(p.relative_to(ROOT))
        src = p.read_text(encoding="utf-8")
        dst = replace_task_paths(src)
        dst = replace_docs_language(dst, rel)
        if dst != src:
            p.write_text(dst, encoding="utf-8")
            changed.append(rel)

    for rel in changed:
        print(f"updated: {rel}")
    print(f"total files updated: {len(changed)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
