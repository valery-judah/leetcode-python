#!/usr/bin/env python3
"""
Extract unique LeetCode problem IDs used across all YAMLs under `archive/`.

Process:
- Scan all `archive/**/*.yaml` files and extract problem slugs from `- slug: <slug>` entries.
- Search those slugs across JSON files under `archive/problems` (follows symlinks).
- Collect matching `id` fields for entries with the same `slug` (including nested entries such as `similar_questions`).
- Output unique, numerically sorted IDs (one per line) to `ids_tracks.txt` at the repo root.

Note: YAML is parsed by simple pattern matching to avoid external dependencies.
"""  # noqa: E501

from __future__ import annotations

import json
import re
from pathlib import Path
from typing import Any, Iterable, Set

ROOT = Path(__file__).resolve().parent
ARCHIVE_DIR = ROOT / "archive"
OUTPUT_FILE = ROOT / "ids_tracks.txt"


def iter_yaml_files() -> Iterable[Path]:
    # All YAMLs under archive
    for path in sorted(ARCHIVE_DIR.rglob("*.yaml")):
        if path.is_file():
            yield path


def extract_slugs_from_yaml(path: Path) -> Set[str]:
    """
    Extract slugs only from the `problems:` and `extensions:` sections to avoid
    picking up slugs listed under `omitted:` or other metadata.
    """
    slug_re = re.compile(r"^\s*-\s*slug:\s*([a-z0-9\-]+)\s*$")
    top_level_key_re = re.compile(r"^([A-Za-z0-9_]+):\s*$")

    allowed_sections = {"problems", "extensions"}
    current_section: str | None = None
    slugs: Set[str] = set()
    saw_any_section = False

    try:
        with path.open("r", encoding="utf-8") as f:
            for raw in f:
                line = raw.rstrip("\n")

                # Detect top-level section changes (no leading spaces)
                if line and not line.startswith(" "):
                    mtop = top_level_key_re.match(line)
                    current_section = mtop.group(1) if mtop else None
                    if mtop:
                        saw_any_section = True

                # Only capture slugs when inside allowed sections
                if current_section in allowed_sections:
                    m = slug_re.match(line)
                    if m:
                        slugs.add(m.group(1))
                elif not saw_any_section:
                    # If file has no recognizable top-level sections, accept any '- slug:'
                    m = slug_re.match(line)
                    if m:
                        slugs.add(m.group(1))
    except Exception as e:
        raise RuntimeError(f"Failed reading {path}: {e}")  # noqa: B904
    return slugs


def iter_json_files_in_problems() -> Iterable[Path]:
    """Recursively find JSON files under `archive/problems` following symlinks."""
    import os

    problems_dir = ARCHIVE_DIR / "problems"
    if not problems_dir.exists():
        return []  # type: ignore[return-value]

    for root, _dirs, files in os.walk(problems_dir, followlinks=True):
        for name in files:
            if name.endswith(".json"):
                p = Path(root) / name
                if p.is_file():
                    yield p


def collect_ids_from_json(json_obj: Any, target_slugs: Set[str], out_ids: Set[str]) -> None:
    # Recursively traverse json to find dicts with matching slug and an id.
    if isinstance(json_obj, dict):
        slug = json_obj.get("slug")
        pid = json_obj.get("id")
        if slug in target_slugs and pid is not None:
            # Ensure ids are strings to normalize; keep only digits just in case
            out_ids.add(str(pid))
        for v in json_obj.values():
            collect_ids_from_json(v, target_slugs, out_ids)
    elif isinstance(json_obj, list):
        for item in json_obj:
            collect_ids_from_json(item, target_slugs, out_ids)
    # Primitives are ignored


def main() -> None:
    if not ARCHIVE_DIR.exists():
        raise SystemExit(f"Archive directory not found: {ARCHIVE_DIR}")

    # 1) Gather slugs from all YAMLs
    slugs: Set[str] = set()
    for yaml_path in iter_yaml_files():
        slugs |= extract_slugs_from_yaml(yaml_path)

    if not slugs:
        # Still proceed to write an empty file to make the outcome explicit
        OUTPUT_FILE.write_text("", encoding="utf-8")
        print(f"No slugs found in tracks. Wrote empty {OUTPUT_FILE}")
        return

    # 2) Scan JSONs under archive/problems and collect matching IDs
    ids: Set[str] = set()
    for json_path in iter_json_files_in_problems():
        try:
            with json_path.open("r", encoding="utf-8") as f:
                data = json.load(f)
            collect_ids_from_json(data, slugs, ids)
        except json.JSONDecodeError:
            # Skip malformed JSONs gracefully
            continue
        except Exception:
            # Ignore other read errors but continue scanning
            continue

    # 3) Sort numerically when possible, fallback to lexicographic
    def sort_key(x: str):
        try:
            return (0, int(x))
        except (ValueError, TypeError):
            return (1, str(x))

    sorted_ids = sorted(ids, key=sort_key)

    # 4) Write output
    OUTPUT_FILE.write_text("\n".join(sorted_ids) + ("\n" if sorted_ids else ""), encoding="utf-8")
    print(f"Found {len(sorted_ids)} unique IDs. Wrote to {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
