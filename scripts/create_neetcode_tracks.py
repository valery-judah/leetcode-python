#!/usr/bin/env python3
"""Generate track YAML files from the NeetCode 250 JSON list.

Reads ``archive/lists/neetcode_250.json`` and writes one YAML file per
category into both ``archive`` and ``tracks`` directories. The YAML
structure is minimal and mirrors the style of ``track_0_foundations.yaml``
without the manual annotations.
"""
from __future__ import annotations

import json
import re
from collections import OrderedDict
from pathlib import Path
from typing import Dict, List

ROOT = Path(__file__).resolve().parents[1]
LIST_PATH = ROOT / "archive" / "lists" / "neetcode_250.json"
ARCHIVE_DIR = ROOT / "archive"
TRACKS_DIR = ROOT / "tracks"


def slugify(text: str) -> str:
    """Convert a category name into a filesystem-friendly slug."""
    text = text.lower()
    # Replace non-alphanumeric characters with underscores
    text = re.sub(r"[^a-z0-9]+", "_", text)
    # Collapse repeated underscores
    text = re.sub(r"_+", "_", text)
    # Strip leading/trailing underscores
    return text.strip("_")


def load_problems() -> List[Dict[str, str]]:
    with LIST_PATH.open() as f:
        data = json.load(f)
    return data["problems"]


def group_by_category(problems: List[Dict[str, str]]) -> OrderedDict[str, List[Dict[str, str]]]:
    grouped: OrderedDict[str, List[Dict[str, str]]] = OrderedDict()
    for prob in problems:
        cat = prob["category"]
        grouped.setdefault(cat, []).append(prob)
    return grouped


def build_yaml(track_id: str, title: str, description: str, problems: List[Dict[str, str]]) -> str:
    lines = [
        "version: 1",
        f"track: {track_id}",
        f"title: {title}",
        f"description: {description}",
        "problems:",
    ]
    for p in problems:
        lines.append(f"  - slug: {p['slug']}")
        lines.append(f"    title: {p['name']}")
        lines.append(f"    difficulty: {p['difficulty'].lower()}")
    return "\n".join(lines) + "\n"


def write_track(track_id: str, content: str) -> None:
    for directory in (ARCHIVE_DIR, TRACKS_DIR):
        path = directory / f"{track_id}.yaml"
        path.write_text(content, encoding="utf-8")


def main() -> None:
    problems = load_problems()
    grouped = group_by_category(problems)
    for idx, (category, probs) in enumerate(grouped.items()):
        slug = slugify(category)
        track_id = f"track_neetcode_{idx}_{slug}"
        title = f"NeetCode 250 — {category}"
        description = f"Problems from the NeetCode 250 list for {category}."
        yaml_content = build_yaml(track_id, title, description, probs)
        write_track(track_id, yaml_content)


if __name__ == "__main__":
    main()
