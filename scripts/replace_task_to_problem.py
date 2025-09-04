#!/usr/bin/env python3
"""
Replace whole-word 'problem' -> 'problem' across .py and .md files, preserving case and plurals.

Examples:
- problem -> problem
- problems -> problems
- Problem -> Problem
- Problems -> Problems
- PROBLEM -> PROBLEM
- PROBLEMS -> PROBLEMS

Skips substrings (e.g., 'multitask' unchanged). Supports dry-run.
"""

from __future__ import annotations

import argparse
import re
from pathlib import Path
from typing import Iterable, Tuple

WORD_RE = re.compile(r"\b(problems?)\b", re.IGNORECASE)


def replacement(match: re.Match) -> str:
    word = match.group(1)
    is_plural = word.lower().endswith("s")

    # Determine case style of the singular base
    base = word[:-1] if is_plural else word

    if base.isupper():
        repl_base = "PROBLEM"
    elif base[0].isupper() and base[1:].islower():
        repl_base = "Problem"
    elif base.islower():
        repl_base = "problem"
    else:
        # Mixed/unknown case: default to preserving first char case
        repl_base = base[0] + "roblem"

    return repl_base + ("S" if is_plural and repl_base.isupper() else ("s" if is_plural else ""))


SKIP_DIR_NAMES = {
    ".git",
    ".hg",
    ".svn",
    ".mypy_cache",
    ".pytest_cache",
    "__pycache__",
    "venv",
    ".venv",
    "env",
    "site-packages",
    "node_modules",
    "build",
    "dist",
    ".tox",
    ".ruff_cache",
    "problems",
}


def find_target_files(root: Path, exts: Iterable[str]) -> Iterable[Path]:
    # Use manual walk to allow directory pruning
    stack = [root]
    while stack:
        current = stack.pop()
        try:
            entries = list(current.iterdir())
        except PermissionError:
            continue
        for entry in entries:
            name = entry.name
            if entry.is_dir():
                if name in SKIP_DIR_NAMES:
                    continue
                stack.append(entry)
            elif entry.is_file():
                if entry.suffix.lower() in exts:
                    yield entry


def process_file(path: Path) -> Tuple[bool, str]:
    try:
        text = path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        # Skip binary or non-utf8 files
        return False, ""
    new_text, count = WORD_RE.subn(replacement, text)
    return (count > 0), new_text


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("root", nargs="?", default=".", help="Root directory to scan (default: .)")
    parser.add_argument(
        "--ext",
        action="append",
        default=[".py", ".md"],
        help="File extensions to include (repeatable)",
    )
    parser.add_argument("--dry-run", action="store_true", help="Do not write changes; just report")
    args = parser.parse_args()

    root = Path(args.root).resolve()
    exts = tuple(s.lower() if s.startswith(".") else f".{s.lower()}" for s in args.ext)

    changed = 0
    total = 0
    for file in find_target_files(root, exts):
        total += 1
        did_change, new_text = process_file(file)
        if not did_change:
            continue

        changed += 1
        if args.dry_run:
            print(f"DRY-RUN would update: {file}")
        else:
            file.write_text(new_text, encoding="utf-8")

    print(f"Scanned files: {total}")
    print(f"Files changed: {changed}")


if __name__ == "__main__":
    main()
