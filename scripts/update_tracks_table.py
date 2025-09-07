#!/usr/bin/env python3
from __future__ import annotations

import json
import re
from pathlib import Path

import yaml

REPO_ROOT = Path(__file__).resolve().parents[1]
TRACKS_DIR = REPO_ROOT / "tracks"
README_PATH = REPO_ROOT / "README.md"


def parse_track_md(path: Path):
    """Parse a track .md file to extract basic stats.

    Returns dict with:
    - name: track display title (from first H1)
    - file: filename stem
    - main_count: number of problem rows in "## Problems"
    - ext_count: number of problem rows in "## Extensions" (if any)
    - main_linked: rows in main table that contain a markdown link
    - ext_linked: rows in extensions table that contain a markdown link
    """

    text = path.read_text(encoding="utf-8")

    # Title: first H1
    m = re.search(r"^#\s+(.+)$", text, flags=re.MULTILINE)
    title = m.group(1).strip() if m else path.stem

    def table_rows(section_title: str):
        # Find section start
        sec = re.search(
            rf"^##\s+{re.escape(section_title)}\s*$",
            text,
            flags=re.MULTILINE,
        )
        if not sec:
            return []
        start = sec.end()
        # Take until next ## or end
        next_sec = re.search(r"^##\s+", text[start:], flags=re.MULTILINE)
        block = text[start : start + (next_sec.start() if next_sec else len(text))]
        # Extract table body lines that look like a row, not header or separator
        rows = []
        for line in block.splitlines():
            s = line.strip()
            if not s.startswith("|"):
                continue
            if set(s.replace("|", "").strip()) <= {"-", ":"}:
                # separator line like |---|
                continue
            # skip header line (assume contains the word Problem)
            if re.search(r"\bProblem\b", s):
                continue
            # non-empty data row
            rows.append(s)
        return rows

    main_rows = table_rows("Problems")
    ext_rows = table_rows("Extensions (Optional)")

    def count_linked(rows):
        linked = 0
        for r in rows:
            # Consider a row linked if the first cell contains a markdown link
            # e.g., | [Title](...)
            first_cell = r.split("|")[1] if "|" in r else r
            if "[" in first_cell and "](" in first_cell:
                linked += 1
        return linked

    stats = {
        "name": title,
        "file": path.stem,
        "main_count": len(main_rows),
        "ext_count": len(ext_rows),
        "main_linked": count_linked(main_rows),
        "ext_linked": count_linked(ext_rows),
    }
    return stats


def kebab(s: str) -> str:
    return "-".join("".join(ch.lower() if ch.isalnum() else "-" for ch in s).split("-"))


def find_problem_dir_by_slug(slug: str) -> Path | None:
    problems_dir = REPO_ROOT / "problems"
    if not problems_dir.exists():
        return None
    for p in sorted(problems_dir.iterdir()):
        if p.is_dir() and p.name.endswith(f"-{slug}"):
            return p
    return None


def load_stats(pdir: Path) -> dict | None:
    stats_fp = pdir / "stats.json"
    if not stats_fp.exists():
        return None
    try:
        return json.loads(stats_fp.read_text())
    except Exception:
        return None


def compute_done_from_yaml(md_path: Path) -> int | None:
    """If a matching YAML exists (in tracks/ or archive/), count problems done.

    Counts both main and optional extensions.
    Returns None if no YAML present.
    """
    # Look for a sibling YAML first, then fallback to archive/ or tracks/
    candidates = [
        md_path.with_suffix(".yaml"),
        REPO_ROOT / "archive" / (md_path.stem + ".yaml"),
        REPO_ROOT / "tracks" / (md_path.stem + ".yaml"),
    ]
    yml = next((p for p in candidates if p.exists()), None)
    if not yml:
        return None
    try:
        data = yaml.safe_load(yml.read_text()) or {}
    except Exception:
        return None
    problems = data.get("problems") or []
    extensions = (data.get("extensions") or {}).get("optional") or []

    done = 0
    for item in [*problems, *extensions]:
        slug = kebab(str(item.get("slug") or "").strip())
        if not slug:
            continue
        pdir = find_problem_dir_by_slug(slug)
        if not pdir:
            continue
        stats = load_stats(pdir)
        if stats and stats.get("optimal_solution") is True:
            done += 1
    return done


def build_table(stats_list):
    # Columns: Track, Main, Ext, Total, Done, Progress, Linked, Unlinked
    header = (
        "| Track | Main | Ext | Total | Done | Progress | Linked | Unlinked |\n"
        "|---|---:|---:|---:|---:|---:|---:|---:|\n"
    )
    rows = []
    for st in stats_list:
        total = st["main_count"] + st["ext_count"]
        linked = st["main_linked"] + st["ext_linked"]
        unlinked = total - linked
        done = st.get("done_count") if st.get("done_count") is not None else linked
        pct = f"{round((done / total) * 100) if total else 0}%"
        # Link the track name to its markdown in tracks/
        track_link = "[" + st["name"] + f"](tracks/{st['file']}.md)"
        rows.append(
            f"| {track_link} | {st['main_count']} | {st['ext_count']} | {total} | {done} | {pct} \
                | {linked} | {unlinked} |"
        )
    return header + "\n".join(rows) + "\n"


def update_readme(table_md: str):
    content = README_PATH.read_text(encoding="utf-8")
    placeholder = "{tracks_table}"
    begin_marker = "<!-- BEGIN_TRACKS_TABLE -->"
    end_marker = "<!-- END_TRACKS_TABLE -->"

    def with_markers(tbl: str) -> str:
        return f"{begin_marker}\n{tbl}{end_marker}"

    if placeholder in content:
        updated = content.replace(placeholder, with_markers(table_md))
        README_PATH.write_text(updated, encoding="utf-8")
        return

    # If markers exist, replace the enclosed content
    begin_idx = content.find(begin_marker)
    end_idx = content.find(end_marker)
    if begin_idx != -1 and end_idx != -1 and end_idx > begin_idx:
        updated = content[:begin_idx] + with_markers(table_md) + content[end_idx + len(end_marker) :]
        README_PATH.write_text(updated, encoding="utf-8")
        return

    # Fallback: locate existing table under the Tracks section and replace it
    tracks_hdr = re.search(r"^#\s+Tracks\s*$", content, flags=re.MULTILINE)
    if tracks_hdr:
        after = content[tracks_hdr.end() :]
        # Find first table header line starting with '|'
        table_start_rel = re.search(r"^\|.*\n", after, flags=re.MULTILINE)
        if table_start_rel:
            start_pos = tracks_hdr.end() + table_start_rel.start()
            # Consume contiguous table lines (starting with '|')
            table_block = re.match(r"(\|.*\n)+", content[start_pos:])
            if table_block:
                end_pos = start_pos + table_block.end()
                updated = content[:start_pos] + with_markers(table_md) + content[end_pos:]
                README_PATH.write_text(updated, encoding="utf-8")
                return

    raise SystemExit("Cannot locate placeholder or existing tracks table in README.md")


def main():
    track_files = sorted(p for p in TRACKS_DIR.glob("*.md") if p.is_file())
    if not track_files:
        raise SystemExit("No track .md files found in 'tracks/'")
    stats = []
    for p in track_files:
        s = parse_track_md(p)
        done = compute_done_from_yaml(p)
        s["done_count"] = done
        stats.append(s)
    table = build_table(stats)
    update_readme(table)


if __name__ == "__main__":
    main()
