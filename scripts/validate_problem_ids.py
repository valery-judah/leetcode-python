#!/usr/bin/env python3
"""
Validate that problem folder IDs/slugs match the archived LeetCode metadata.

Checks performed per folder under `problems/`:
 - Directory prefix ID matches the problem JSON's frontend ID.
 - Directory slug matches the archived slug for that ID.
 - Directory ID matches the archived ID for that slug.

Run:
  python scripts/validate_problem_ids.py           # report only
  python scripts/validate_problem_ids.py --strict  # non‑zero exit if any issues

This script is read‑only and does not mutate files.
"""

from __future__ import annotations

import argparse
import json
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, List, Tuple

ROOT = Path(__file__).resolve().parents[1]
PROBLEMS_DIR = ROOT / "problems"
ARCHIVE_DIR = ROOT / "archive" / "problems"


@dataclass
class Issue:
    folder: Path
    kind: str
    detail: str


def load_archive_index() -> Tuple[Dict[int, str], Dict[str, int]]:
    id_to_slug: Dict[int, str] = {}
    slug_to_id: Dict[str, int] = {}

    for fp in ARCHIVE_DIR.glob("*.json"):
        try:
            data = json.loads(fp.read_text())
        except Exception:
            continue
        slug = data.get("slug") or data.get("titleSlug")
        fid = data.get("questionFrontendId") or data.get("frontendQuestionId") or data.get("id")
        try:
            fid = int(fid)
        except Exception:
            continue
        if not slug:
            continue
        id_to_slug[fid] = slug
        slug_to_id[slug] = fid

    return id_to_slug, slug_to_id


def parse_problem_json(folder: Path) -> Tuple[int, str] | None:
    # Expect a file like 0001-problem.json or 1046-problem.json
    jfiles = sorted(folder.glob("*-problem.json"))
    if not jfiles:
        return None
    try:
        data = json.loads(jfiles[0].read_text())
    except Exception:
        return None
    fid = data.get("questionFrontendId") or data.get("frontendQuestionId") or data.get("id")
    slug = data.get("slug") or data.get("titleSlug")
    try:
        fid_i = int(fid) if fid is not None else None
    except Exception:
        fid_i = None
    if fid_i is None or not slug:
        return None
    return fid_i, slug


def validate(strict: bool = False) -> int:
    issues: List[Issue] = []

    if not PROBLEMS_DIR.exists():
        print("No problems directory found; nothing to validate.")
        return 0

    id_to_slug, slug_to_id = load_archive_index()

    for folder in sorted(PROBLEMS_DIR.iterdir()):
        if not folder.is_dir():
            continue
        m = re.match(r"^(\d+)-(.*)$", folder.name)
        if not m:
            # skip helper dirs like __pycache__
            continue
        did = int(m.group(1))
        dslug = m.group(2)

        # 1) Validate against the folder's problem JSON if present
        pj = parse_problem_json(folder)
        if pj:
            fid, fslug = pj
            if fid != did:
                issues.append(
                    Issue(
                        folder,
                        "folder-id-vs-json-id",
                        f"dir id {did} != json id {fid}",
                    )
                )
            if fslug != dslug:
                issues.append(
                    Issue(
                        folder,
                        "folder-slug-vs-json-slug",
                        f"dir slug '{dslug}' != json slug '{fslug}'",
                    )
                )

        # 2) Validate folder id -> archive slug
        arch_slug = id_to_slug.get(did)
        if arch_slug is None:
            issues.append(
                Issue(
                    folder,
                    "id-missing-in-archive",
                    f"id {did} not found in archive index",
                )
            )
        elif arch_slug != dslug:
            issues.append(
                Issue(
                    folder,
                    "id-to-slug-mismatch",
                    f"expected slug '{arch_slug}' for id {did}",
                )
            )

        # 3) Validate folder slug -> archive id
        arch_id = slug_to_id.get(dslug)
        if arch_id is None:
            issues.append(
                Issue(
                    folder,
                    "slug-missing-in-archive",
                    f"slug '{dslug}' not found in archive index",
                )
            )
        elif arch_id != did:
            issues.append(
                Issue(
                    folder,
                    "slug-to-id-mismatch",
                    f"expected id {arch_id} for slug '{dslug}'",
                )
            )

    if not issues:
        print("All problem IDs/slugs validate against archive and local JSON.")
        return 0

    print("Found mismatches:")
    for iss in issues:
        print(f"- {iss.kind}: {iss.folder.name} -> {iss.detail}")

    return 1 if strict else 0


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument(
        "--strict",
        action="store_true",
        help="Exit non-zero if any issues are found",
    )
    args = ap.parse_args()
    code = validate(strict=args.strict)
    raise SystemExit(code)


if __name__ == "__main__":
    main()
