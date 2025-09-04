#!/usr/bin/env python3
"""
Generate / regenerate repo structure from track yaml files.

- Reads all `tracks/track_*.yaml` (and optional `extensions.optional`) and builds a unified problem set.
- Optionally enriches with IDs by scanning existing problems/* directories and lists/*.json.
- Creates missing problem folders under problems/, writes `problem.json`, README, solution stub, and test stub.
- Idempotent. Default is dry-run. Use --apply to write changes.

Requires: PyYAML (for reading track yaml). Install:
  pip install pyyaml
"""
from __future__ import annotations

import argparse
import datetime as dt
import json
import re
from dataclasses import dataclass, field
from pathlib import Path
from typing import Dict, Iterable, List, Tuple

try:
    import yaml  # type: ignore
except Exception:  # pragma: no cover
    print("[warn] PyYAML not available. Install with: pip install pyyaml", flush=True)
    yaml = None  # type: ignore

# ---------------------------- models ----------------------------

@dataclass
class TrackProblem:
    slug: str
    title: str | None
    difficulty: str | None
    primary_pattern: str | None
    section: str | None
    why: str | None
    track: str
    kind: str  # 'core' or 'extension'

@dataclass
class ProblemRecord:
    slug: str
    id: int | None = None
    title: str | None = None
    difficulty: str | None = None
    primary_pattern: str | None = None
    section: str | None = None
    why: str | None = None
    sources: List[str] = field(default_factory=list)  # track names
    kind: str = "core"  # core or extension
    status: str = "todo"
    topics: List[str] = field(default_factory=list)
    patterns: List[str] = field(default_factory=list)
    created_at: str = field(default_factory=lambda: dt.datetime.utcnow().isoformat(timespec="seconds") + "Z")

    def merge_track(self, tp: TrackProblem) -> None:
        self.title = self.title or tp.title
        self.difficulty = self.difficulty or tp.difficulty
        self.primary_pattern = self.primary_pattern or tp.primary_pattern
        self.section = self.section or tp.section
        self.why = self.why or tp.why
        if tp.track not in self.sources:
            self.sources.append(tp.track)
        # prefer core over extension for kind
        if self.kind != "core":
            self.kind = tp.kind
        # patterns list includes primary
        if tp.primary_pattern and tp.primary_pattern not in self.patterns:
            self.patterns.append(tp.primary_pattern)

# ---------------------------- utils ----------------------------

TRACK_LINE_RE = re.compile(r"^\s*track:\s*([^#\n]+?)\s*$", re.MULTILINE)
FOLDER_ID_SLUG_RE = re.compile(r"^(\d{4})-(.+)$")


def read_yaml(p: Path) -> dict:
    if yaml is None:
        raise RuntimeError("PyYAML not installed. pip install pyyaml")
    return yaml.safe_load(p.read_text(encoding="utf-8"))


def read_json(p: Path):
    return json.loads(p.read_text(encoding="utf-8"))


def write_text(p: Path, text: str, apply: bool) -> None:
    if apply:
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(text, encoding="utf-8")


def write_json(p: Path, obj, apply: bool, indent: int = 2) -> None:
    if apply:
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(json.dumps(obj, indent=indent, ensure_ascii=False) + "\n", encoding="utf-8")


# ---------------------------- discovery ----------------------------

def load_tracks(tracks_dir: Path) -> Dict[str, List[TrackProblem]]:
    """Return mapping track_name -> list of TrackProblem."""
    ret: Dict[str, List[TrackProblem]] = {}
    for y in sorted(tracks_dir.glob("track_*.yaml")):
        data = read_yaml(y)
        track_name = str(data.get("track") or y.stem)
        coll: List[TrackProblem] = []
        for kind, key in [("core", "problems"), ("extension", "extensions")]:
            if key == "problems" and isinstance(data.get("problems"), list):
                for it in data["problems"]:
                    coll.append(TrackProblem(
                        slug=str(it.get("slug")),
                        title=it.get("title"),
                        difficulty=it.get("difficulty"),
                        primary_pattern=it.get("primary_pattern"),
                        section=it.get("section"),
                        why=it.get("why"),
                        track=track_name,
                        kind="core",
                    ))
            elif key == "extensions" and isinstance(data.get("extensions"), dict):
                opt = data["extensions"].get("optional")
                if isinstance(opt, list):
                    for it in opt:
                        coll.append(TrackProblem(
                            slug=str(it.get("slug")),
                            title=it.get("title"),
                            difficulty=it.get("difficulty"),
                            primary_pattern=it.get("primary_pattern"),
                            section=it.get("section"),
                            why=it.get("why"),
                            track=track_name,
                            kind="extension",
                        ))
        ret[track_name] = coll
    return ret


def build_slug_id_map(problems_dir: Path, lists_dir: Path) -> Dict[str, int]:
    """Collect slug->id from existing problem folders and lists/*.json."""
    mapping: Dict[str, int] = {}

    # From problems/<id>-<slug>
    if problems_dir.is_dir():
        for sub in problems_dir.iterdir():
            if not sub.is_dir():
                continue
            m = FOLDER_ID_SLUG_RE.match(sub.name)
            if m:
                pid, pslug = int(m.group(1)), m.group(2)
                mapping.setdefault(pslug, pid)
            else:
                # also check problem.json
                pj = sub / "problem.json"
                if pj.exists():
                    try:
                        data = read_json(pj)
                        if isinstance(data, dict) and data.get("id") and data.get("slug"):
                            mapping.setdefault(str(data["slug"]), int(data["id"]))
                    except Exception:
                        pass

    # From lists/*.json — recurse and extract any objects with id + slug
    if lists_dir.is_dir():
        for jf in lists_dir.glob("*.json"):
            try:
                obj = read_json(jf)
            except Exception:
                continue
            for sid, sslug in _walk_pairs_id_slug(obj):
                try:
                    mapping.setdefault(str(sslug), int(sid))
                except Exception:
                    continue
    return mapping


def _walk_pairs_id_slug(obj) -> Iterable[Tuple[int, str]]:
    if isinstance(obj, dict):
        if "id" in obj and "slug" in obj:
            try:
                yield int(obj["id"]), str(obj["slug"]).strip()
            except Exception:
                pass
        for v in obj.values():
            yield from _walk_pairs_id_slug(v)
    elif isinstance(obj, list):
        for it in obj:
            yield from _walk_pairs_id_slug(it)


# ---------------------------- generation ----------------------------

def decide_folder_name(slug: str, pid: int | None, id_mode: str) -> str:
    if id_mode == "none" or pid is None and id_mode == "auto_none_if_missing":
        return slug
    if pid is None and id_mode == "require":
        raise ValueError(f"ID required for slug {slug} but not found")
    if pid is None:  # auto
        return slug
    return f"{pid:04d}-{slug}"


def load_template(path: Path | None, default: str) -> str:
    if path and path.exists():
        return path.read_text(encoding="utf-8")
    return default


README_DEFAULT = """# ${TITLE}

**ID**: ${ID}
**Slug**: ${SLUG}
**Difficulty**: ${DIFFICULTY}
**Primary pattern**: ${PRIMARY_PATTERN}
**Track(s)**: ${TRACKS}

## Invariant / Idea
${WHY}

## Complexity
- Time: TBD
- Space: TBD

## Notes
- Pitfalls: TBD
"""

SOLUTION_DEFAULT = """def solve(*args, **kwargs):
    \"\"\"Write your solution here.\"\"\"
    raise NotImplementedError
"""

TEST_DEFAULT = """import pytest

# Add tests here

def test_sanity():
    assert True
"""


def render_template(tpl: str, **kw) -> str:
    def repl(match):
        key = match.group(1)
        return str(kw.get(key, ""))
    return re.sub(r"\$\{([A-Z_]+)\}", repl, tpl)


def build_problem_json(rec: ProblemRecord) -> dict:
    return {
        "id": rec.id,
        "slug": rec.slug,
        "title": rec.title,
        "difficulty": rec.difficulty,
        "primary_pattern": rec.primary_pattern,
        "section": rec.section,
        "patterns": rec.patterns,
        "topics": rec.topics,
        "sources": rec.sources,
        "kind": rec.kind,
        "status": rec.status,
        "why": rec.why,
        "created_at": rec.created_at,
    }


# ---------------------------- main flow ----------------------------

def main(argv: List[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description="Generate/regenerate repo from tracks")
    ap.add_argument("--tracks-dir", default="tracks", help="Directory with track_*.yaml files")
    ap.add_argument("--problems-dir", default="problems", help="Directory to create problem folders")
    ap.add_argument("--lists-dir", default="lists", help="Directory with lists *.json for ID enrichment")
    ap.add_argument("--id-mode", choices=["auto", "auto_none_if_missing", "none", "require"], default="auto", help="Folder naming with ID prefix")
    ap.add_argument("--apply", action="store_true", help="Write changes; otherwise dry-run")
    ap.add_argument("--overwrite", choices=["skip", "merge", "overwrite"], default="merge", help="When problem.json exists")
    ap.add_argument("--readme-template", default="templates/problem_readme.md.tpl")
    ap.add_argument("--solution-template", default="templates/solution.py.tpl")
    ap.add_argument("--test-template", default="templates/test_solution.py.tpl")

    args = ap.parse_args(argv)

    root = Path(__file__).resolve().parents[1]
    tracks_dir = (root / args.tracks_dir).resolve()
    problems_dir = (root / args.problems_dir).resolve()
    lists_dir = (root / args.lists_dir).resolve()

    # Load track problems
    tracks = load_tracks(tracks_dir)

    # Build slug->ProblemRecord
    records: Dict[str, ProblemRecord] = {}
    for tname, items in tracks.items():
        for tp in items:
            slug = tp.slug
            if not slug:
                continue
            rec = records.get(slug)
            if not rec:
                rec = ProblemRecord(slug=slug, kind=tp.kind)
                records[slug] = rec
            rec.merge_track(tp)

    # Enrich with IDs
    slug_to_id = build_slug_id_map(problems_dir, lists_dir)
    for slug, rec in records.items():
        if rec.id is None and slug in slug_to_id:
            rec.id = slug_to_id[slug]

    # Load templates
    readme_tpl = load_template((root / args.readme_template), README_DEFAULT)
    solution_tpl = load_template((root / args.solution_template), SOLUTION_DEFAULT)
    test_tpl = load_template((root / args.test_template), TEST_DEFAULT)

    # Apply
    for slug, rec in sorted(records.items(), key=lambda kv: (kv[1].id is None, kv[1].id or 10**9, kv[0])):
        folder_name = decide_folder_name(rec.slug, rec.id, args.id_mode)
        pdir = problems_dir / folder_name

        # problem.json
        target_json = pdir / "problem.json"
        new_data = build_problem_json(rec)
        action = "create"
        if target_json.exists():
            if args.overwrite == "skip":
                print(f"SKIP problem.json exists: {target_json}")
            elif args.overwrite == "overwrite":
                print(f"WRITE {target_json}")
                write_json(target_json, new_data, apply=args.apply)
            else:  # merge
                try:
                    old = read_json(target_json)
                except Exception:
                    old = {}
                merged = {**old, **{k: v for k, v in new_data.items() if v not in (None, [], "")}}
                print(f"MERGE {target_json}")
                write_json(target_json, merged, apply=args.apply)
        else:
            print(f"CREATE {target_json}")
            write_json(target_json, new_data, apply=args.apply)

        # README
        readme = pdir / "readme.md"
        if not readme.exists():
            rendered = render_template(
                readme_tpl,
                TITLE=rec.title or rec.slug.replace("-", " ").title(),
                ID=(rec.id if rec.id is not None else ""),
                SLUG=rec.slug,
                DIFFICULTY=rec.difficulty or "",
                PRIMARY_PATTERN=rec.primary_pattern or "",
                TRACKS=", ".join(rec.sources),
                WHY=rec.why or "",
            )
            print(f"CREATE {readme}")
            write_text(readme, rendered, apply=args.apply)
        else:
            print(f"OK     {readme} exists")

        # solution stub
        sol = pdir / "solutions.py"
        if not sol.exists():
            print(f"CREATE {sol}")
            write_text(sol, solution_tpl, apply=args.apply)
        else:
            print(f"OK     {sol} exists")

        # test stub (only if pytest infra present)
        test = pdir / "test_solution.py"
        if not test.exists():
            print(f"CREATE {test}")
            write_text(test, test_tpl, apply=args.apply)
        else:
            print(f"OK     {test} exists")

    print("Done.")
    if not args.apply:
        print("(dry-run) Use --apply to write files")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
