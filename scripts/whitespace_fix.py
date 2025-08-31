from __future__ import annotations

import os
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

SKIP_DIRS = {
    ".git",
    "venv",
    ".mypy_cache",
    ".ruff_cache",
    ".pytest_cache",
    "site",
    "htmlcov",
    "__pycache__",
}
TEXT_EXTS = {".py", ".md", ".toml", ".yml", ".yaml", ".txt", ".svg", ".ini", ".cfg"}
ALWAYS_INCLUDE = {".clinerules"}

changed: list[Path] = []

for dirpath, dirnames, filenames in os.walk(ROOT):
    # prune skip dirs
    dirnames[:] = [d for d in dirnames if d not in SKIP_DIRS]
    for name in filenames:
        p = Path(dirpath) / name
        rel = p.relative_to(ROOT)
        if name == ".gitkeep":
            # normalize to truly empty file
            if p.read_bytes():
                p.write_bytes(b"")
                changed.append(rel)
            continue
        if rel.as_posix() in ALWAYS_INCLUDE or p.suffix.lower() in TEXT_EXTS:
            try:
                data = p.read_text(encoding="utf-8")
            except Exception:
                continue  # skip binary or undecodable
            orig = data
            # split to lines without keeping ends
            lines = data.splitlines()
            # remove trailing spaces/tabs on each line
            lines = [ln.rstrip(" \t") for ln in lines]
            # drop trailing empty lines
            while lines and lines[-1] == "":
                lines.pop()
            # rejoin with exactly one trailing newline
            data = ("\n".join(lines) + "\n") if lines else ""
            if data != orig:
                p.write_text(data, encoding="utf-8")
                changed.append(rel)

if changed:
    print("Fixed whitespace in:")
    for r in changed:
        print(" -", r)
else:
    print("No changes needed.")
