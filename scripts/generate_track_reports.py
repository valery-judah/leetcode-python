#!/usr/bin/env python
from __future__ import annotations

import json
import os
import sys
from pathlib import Path

import yaml

from leetcode_index import get_id, get_slug

ROOT = Path(__file__).resolve().parents[1]


def find_problem_dir_by_id(problem_id: int) -> Path | None:
    problems_dir = ROOT / "problems"
    if not problems_dir.exists():
        return None
    # Match any folder starting with the zero-padded problem ID.
    prefix = f"{problem_id:04d}-"
    for p in sorted(problems_dir.iterdir()):
        if not p.is_dir():
            continue
        name = p.name
        if name.startswith(prefix):
            # Optional: Verify that the slug in the folder name matches the index.
            expected_slug = get_slug(problem_id)
            if name != f"{prefix}{expected_slug}":
                print(
                    f"W100: Slug mismatch for problem {problem_id}: " f"'{name}' vs '{expected_slug}'",
                    file=sys.stderr,
                )
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


def build_table(rows: list[dict]) -> str:
    header = (
        "| Problem | Diff | Baseline | Complex Justified | Optimal | Repeats | Min Time | Conf | Clarified | "
        "Communicated | Stated | Edge Tests | Clean Impl | Mistakes |\n"
        "|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|"
    )
    lines = [header]
    for r in rows:
        lines.append(
            "| {problem} | {diff} | {baseline} | {complex_just} | {optimal} | {repeats} | {min_time} | "
            "{conf} | {clarified} | {communicated} | {stated} | {edge_tests} | {clean_impl} | {mistakes} |".format(
                problem=r["problem"],
                diff=r.get("diff", ""),
                baseline=r.get("baseline", ""),
                complex_just=r.get("complex_just", ""),
                optimal=r.get("optimal", ""),
                repeats=r.get("repeats", ""),
                min_time=r.get("min_time", ""),
                conf=r.get("conf", ""),
                clarified=r.get("clarified", ""),
                communicated=r.get("communicated", ""),
                stated=r.get("stated", ""),
                edge_tests=r.get("edge_tests", ""),
                clean_impl=r.get("clean_impl", ""),
                mistakes=r.get("mistakes", ""),
            )
        )
    return "\n".join(lines) + "\n"


def bool_icon(v: bool | None) -> str:
    if v is True:
        return "✅"
    if v is False:
        return "✖️"
    return ""


def _process_problem_list(problem_list: list[dict], out_path: Path) -> list[dict]:
    rows: list[dict] = []
    for item in problem_list:
        problem_id, slug = None, None
        if "id" in item:
            problem_id = int(item["id"])
            slug = get_slug(problem_id)
            if "slug" in item and item["slug"] != slug:
                print(
                    f"W101: Slug for problem {problem_id} ('{item['slug']}') does not match index ('{slug}'). "
                    "Using slug from index.",
                    file=sys.stderr,
                )
        elif "slug" in item:
            slug = str(item["slug"])
            problem_id = get_id(slug)

        if not problem_id or not slug:
            sys.exit(f"E200: Could not resolve problem identifier: {item}")

        disp_title = str(item.get("title") or slug.replace("-", " ").title())
        diff = str(item.get("difficulty") or "").title()
        pdir = find_problem_dir_by_id(problem_id)
        stats = load_stats(pdir) if pdir else None
        if pdir and (pdir / "readme.md").exists():
            abs_target = pdir / "readme.md"
            rel_str = os.path.relpath(abs_target, start=out_path.parent)
            problem_link = f"[{disp_title}]({Path(rel_str).as_posix()})"
        elif pdir:
            problem_link = f"{disp_title} ({pdir.name})"
        else:
            problem_link = disp_title
        rows.append(
            {
                "problem": problem_link,
                "diff": diff,
                "baseline": bool_icon((stats or {}).get("baseline_impl")),
                "complex_just": bool_icon((stats or {}).get("complexity_justified")),
                "optimal": bool_icon((stats or {}).get("optimal_solution")),
                "repeats": (stats or {}).get("repeats", ""),
                "min_time": (stats or {}).get("min_impl_time_min", ""),
                "conf": (stats or {}).get("confidence_1to5", ""),
                "clarified": bool_icon(((stats or {}).get("signals") or {}).get("clarified_assumptions")),
                "communicated": bool_icon(((stats or {}).get("signals") or {}).get("communicated_approach")),
                "stated": bool_icon(((stats or {}).get("signals") or {}).get("stated_complexity")),
                "edge_tests": bool_icon(((stats or {}).get("signals") or {}).get("tests_edge_cases")),
                "clean_impl": bool_icon(((stats or {}).get("signals") or {}).get("clean_impl")),
                "mistakes": ", ".join((stats or {}).get("mistakes") or []),
            }
        )
    return rows


def generate_for_track(yaml_path: Path) -> Path:
    data = yaml.safe_load(yaml_path.read_text())
    track_name = str(data.get("track") or yaml_path.stem)
    title = str(data.get("title") or track_name.replace("_", " ").title())
    description = str(data.get("description") or "")
    out_path = (ROOT / "tracks" / yaml_path.stem).with_suffix(".md")

    # Process main problems
    problems = data.get("problems") or []
    rows = _process_problem_list(problems, out_path)
    table = build_table(rows)

    # Process optional extensions
    extensions = (data.get("extensions") or {}).get("optional") or []
    ext_rows = _process_problem_list(extensions, out_path)
    extensions_table = "## Extensions (Optional)\n\n" + build_table(ext_rows) if ext_rows else ""

    tpl = (ROOT / "templates" / "track_report.md.tpl").read_text()
    md = tpl.format(
        track_title=title,
        track_name=track_name,
        description=description,
        problems_table=table,
        extensions_table=extensions_table,
    )

    out_path.write_text(md)
    return out_path


def main(argv: list[str]) -> int:
    tracks_dir = ROOT / "tracks"
    yaml_files = sorted(tracks_dir.glob("*.yaml"))
    if not yaml_files:
        print("No track YAML files found.")
        return 0
    for fp in yaml_files:
        out = generate_for_track(fp)
        print(f"Generated {out.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
