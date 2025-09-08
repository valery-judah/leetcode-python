from __future__ import annotations
import hashlib, json, os, re, sys, tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SSOT = ROOT / "data" / "problems.index.jsonl"
GEN = ROOT / "generated"
MAPS = ROOT / "leetcode_index" / "_maps.py"

_slug_rx = re.compile(r"[^a-z0-9-]+")


def norm(s: str) -> str:
    s = _slug_rx.sub("-", s.strip().lower())
    s = re.sub(r"-{2,}", "-", s)
    return s.strip("-")


def atomic_write(path: Path, data: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.NamedTemporaryFile("w", delete=False, dir=str(path.parent)) as tmp:
        tmp.write(data)
        tmp.flush()
        os.fsync(tmp.fileno())
        Path(tmp.name).replace(path)


def build() -> None:
    ids, slugs, aliases = set(), set(), set()
    rows = []
    with SSOT.open() as f:
        for i, line in enumerate(f, 1):
            r = json.loads(line)
            raw_slug = r["slug"]
            r["slug"] = norm(r["slug"])
            r["aliases"] = [norm(a) for a in r.get("aliases", [])]
            if r["id"] in ids:
                sys.exit(f"E100 duplicate id {r['id']} at line {i}")
            if r["slug"] in slugs:
                sys.exit(f"E101 duplicate slug {r['slug']} at line {i}")
            for a in r["aliases"]:
                if a in aliases or a in slugs:
                    sys.exit(f"E102 alias '{a}' collides at line {i}")
            ids.add(r["id"])
            slugs.add(r["slug"])
            aliases.update(r["aliases"])
            if norm(raw_slug) != raw_slug:
                print(f"W200 normalized '{raw_slug}' → '{r['slug']}' at line {i}")
            rows.append(r)

    rows.sort(key=lambda r: r["id"])  # determinism
    id_to_slug = {r["id"]: r["slug"] for r in rows}
    slug_to_id = {r["slug"]: r["id"] for r in rows}
    for r in rows:
        for a in r["aliases"]:
            slug_to_id[a] = r["id"]

    id_json = json.dumps(id_to_slug, sort_keys=True, indent=2)
    slug_json = json.dumps(slug_to_id, sort_keys=True, indent=2)

    # version
    h = hashlib.sha256(SSOT.read_bytes()).hexdigest()[:8]
    py = (
        "# GENERATED. Do not edit\n"
        f"INDEX_VERSION = '{h}'\n"
        f"ID_TO_SLUG = {json.dumps(id_to_slug, sort_keys=True)}\n"
        f"SLUG_TO_ID = {json.dumps(slug_to_id, sort_keys=True)}\n"
    )

    atomic_write(GEN / "id_to_slug.json", id_json)
    atomic_write(GEN / "slug_to_id.json", slug_json)
    atomic_write(MAPS, py)
