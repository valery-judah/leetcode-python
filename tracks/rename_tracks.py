#!/usr/bin/env python3
"""
Rename track YAML files to match their internal `track:` key.

Default: dry-run. Use --apply to make changes.
Handles filename collisions with --resolve {skip,overwrite,suffix}.

Examples
  Dry run:
    python tracks/rename_tracks.py
  Apply with suffixing on conflicts:
    python tracks/rename_tracks.py --apply
  Overwrite conflicts:
    python tracks/rename_tracks.py --apply --resolve overwrite
"""
from __future__ import annotations

import argparse
import hashlib
import os
import re
import sys
from pathlib import Path
from typing import Optional, Tuple

# Optional: use PyYAML if installed, else regex fallback
try:
    import yaml  # type: ignore
except Exception:  # pragma: no cover
    yaml = None  # type: ignore

TRACK_LINE_RE = re.compile(r"^\s*track:\s*([^#\n]+?)\s*$", re.MULTILINE)


def read_text(p: Path) -> str:
    return p.read_text(encoding="utf-8")


def file_sha256(p: Path) -> str:
    h = hashlib.sha256()
    with p.open("rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def extract_track_key(text: str) -> Optional[str]:
    # Fast regex path
    m = TRACK_LINE_RE.search(text)
    if m:
        key = m.group(1).strip().strip('"').strip("'")
        return key or None
    # YAML fallback
    if yaml is not None:
        try:
            data = yaml.safe_load(text)
            if isinstance(data, dict) and isinstance(data.get("track"), str):
                return data["track"].strip()
        except Exception:
            pass
    return None


def plan_moves(tracks_dir: Path) -> Tuple[list[Tuple[Path, Path]], list[str]]:
    moves: list[Tuple[Path, Path]] = []
    notes: list[str] = []

    for p in sorted(tracks_dir.glob("*.yaml")):
        if p.name.startswith("_"):
            continue
        if p.name in {"tracks.yaml", "schema.yaml"}:
            continue
        # Skip non-track files if any live here (defensive)
        try:
            text = read_text(p)
        except Exception as e:
            notes.append(f"WARN cannot read {p.name}: {e}")
            continue
        track_key = extract_track_key(text)
        if not track_key:
            notes.append(f"SKIP {p.name}: no `track:` key found")
            continue
        target = p.with_name(f"{track_key}.yaml")
        if p.name == target.name:
            notes.append(f"OK   {p.name}: name already matches track key")
            continue
        moves.append((p, target))
    return moves, notes


def perform_moves(moves: list[Tuple[Path, Path]], apply: bool, resolve: str) -> None:
    assert resolve in {"skip", "overwrite", "suffix"}

    for src, dst in moves:
        action_note = ""
        if dst.exists() and dst != src:
            # Collision handling
            if file_sha256(src) == file_sha256(dst):
                action_note = "duplicate-content"
                if apply:
                    # Safe to remove src; target already present with same content
                    src.unlink()
                print(f"{('APPLY' if apply else 'DRY  ')} rm   {src.name}  -> {dst.name}  [{action_note}]")
                continue
            if resolve == "skip":
                print(f"DRY  skip {src.name} -> {dst.name}  [exists]")
                if apply:
                    print(f"APPLY skip {src.name} -> {dst.name}  [exists]")
                continue
            elif resolve == "overwrite":
                action_note = "overwrite"
                if apply:
                    # Replace atomically
                    tmp = dst.with_suffix(dst.suffix + ".bak")
                    if tmp.exists():
                        tmp.unlink()
                    dst.replace(tmp)
                    src.replace(dst)
                    # Keep a backup of the old target as .bak
                print(f"{('APPLY' if apply else 'DRY  ')} mv   {src.name}  -> {dst.name}  [{action_note}]")
                continue
            else:  # suffix
                base = dst.stem
                suffix_n = 1
                new_dst = dst.with_name(f"{base}__dup{suffix_n}{dst.suffix}")
                while new_dst.exists():
                    suffix_n += 1
                    new_dst = dst.with_name(f"{base}__dup{suffix_n}{dst.suffix}")
                if apply:
                    src.replace(new_dst)
                print(f"{('APPLY' if apply else 'DRY  ')} mv   {src.name}  -> {new_dst.name}  [suffix]")
                continue
        # No collision
        if apply:
            src.replace(dst)
        print(f"{('APPLY' if apply else 'DRY  ')} mv   {src.name}  -> {dst.name}")


def main(argv: list[str]) -> int:
    ap = argparse.ArgumentParser(description="Rename track YAML files to match their internal `track:` key")
    ap.add_argument("--dir", default=str(Path(__file__).resolve().parent), help="Tracks directory (default: this script's directory)")
    ap.add_argument("--apply", action="store_true", help="Perform renames. Without this flag, runs in dry-run mode.")
    ap.add_argument("--resolve", choices=["skip", "overwrite", "suffix"], default="suffix", help="On filename conflict: skip, overwrite, or suffix (default)")
    args = ap.parse_args(argv)

    tracks_dir = Path(args.dir).resolve()
    if not tracks_dir.is_dir():
        print(f"ERR  Not a directory: {tracks_dir}", file=sys.stderr)
        return 2

    moves, notes = plan_moves(tracks_dir)

    for n in notes:
        print(n)

    if not moves:
        print("Nothing to rename.")
        return 0

    perform_moves(moves, apply=args.apply, resolve=args.resolve)
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
