# LeetCode Index: Detailed Implementation Plan

This plan defines an SSOT-driven index for mapping **LeetCode problem IDs ↔ slugs**. It is structured so another agent can implement it end-to-end with minimal clarification.

## 0) Objectives
- Single Source of Truth (SSOT) for `{id, slug, title, aliases, deprecated}`.
- Deterministic build that generates fast lookup artifacts for import and CLI use.
- CI guardrails to prevent drift between SSOT and generated maps.
- Backward compatibility for renames via `aliases`.

**Non‑goals:** Scraping LeetCode, syncing tags/difficulty, or storing full statements.

---

## 1) Repo layout
```
repo/
├─ data/
│  └─ problems.index.jsonl               # SSOT (hand‑edited, reviewed)
├─ generated/
│  ├─ id_to_slug.json                    # derived (do not edit)
│  ├─ slug_to_id.json                    # derived (do not edit; includes aliases)
│  └─ _maps.py                           # derived Python dicts used by package
├─ leetcode_index/
│  ├─ __init__.py                        # public API
│  ├─ __main__.py                        # CLI entrypoint
│  └─ _build.py                          # builder and validators
├─ scripts/
│  ├─ build_index.py                     # thin wrapper around package build (optional)
│  └─ leetcode_index_implementation_plan.md
├─ tests/
│  ├─ test_build.py
│  └─ test_api.py
├─ pyproject.toml
└─ .github/workflows/index.yml
```

---

## 2) SSOT format (`data/problems.index.jsonl`)
**One JSON per line.** Strict schema:
```json
{"id": 242, "slug": "valid-anagram", "title": "Valid Anagram", "aliases": [], "deprecated": false}
{"id": 1,   "slug": "two-sum",       "title": "Two Sum",        "aliases": ["two-sum-1"], "deprecated": false}
```
Rules:
- `id`: int, unique, > 0
- `slug`: string, unique, normalized lower‑kebab
- `title`: string, optional but recommended
- `aliases`: list[str], all normalized, unique across file; may include historical slugs
- `deprecated`: bool, default `false`

**Normalization**: lowercase, trim, replace `[^a-z0-9-]` with `-`, collapse `--+` to `-`, strip leading/trailing `-`.

---

## 3) Build pipeline (`leetcode_index/_build.py`)
Responsibilities:
1. Read SSOT, normalize, and validate constraints.
2. Construct maps:
   - `ID_TO_SLUG: dict[int, str]`
   - `SLUG_TO_ID: dict[str, int]` (includes aliases → canonical id)
3. Emit artifacts atomically:
   - `generated/id_to_slug.json`
   - `generated/slug_to_id.json`
   - `generated/_maps.py` with the two dict literals and `INDEX_VERSION`.

### 3.1 Validation checklist
- Duplicate `id` → error.
- Duplicate `slug` → error.
- Alias collision with any slug or another alias → error.
- Non‑normalized input encountered → auto‑normalize, but emit warning list.
- `deprecated == true` rows still generate mappings but are flagged in a report.

### 3.2 Determinism
- Sort keys when serializing JSON.
- Stable iteration by sorting by `id` before building.
- Atomic writes: write to tempfile in same directory then `replace`.

### 3.3 Version fingerprint
- Compute `INDEX_VERSION = sha256(problems.index.jsonl bytes).hexdigest()[:8]` and embed in `_maps.py`.

---

## 4) Package API (`leetcode_index/__init__.py`)
Public surface (type hints included):
```python
from typing import Tuple

from ._maps import ID_TO_SLUG, SLUG_TO_ID, INDEX_VERSION  # populated post-build

__all__ = [
    "get_slug", "get_id", "exists_id", "exists_slug", "resolve",
    "ID_TO_SLUG", "SLUG_TO_ID", "INDEX_VERSION",
]

def get_slug(problem_id: int) -> str: ...

def get_id(slug_or_alias: str) -> int: ...

def exists_id(problem_id: int) -> bool: ...

def exists_slug(slug_or_alias: str) -> bool: ...

def resolve(x: int | str) -> Tuple[int, str]:
    """Accept id or slug/alias. Return (id, canonical_slug)."""
```
Behavior:
- All lookups are O(1).
- `get_id` and `exists_slug` lowercase the key.
- On missing keys, raise `KeyError` with the unknown token.
- If `_maps.py` is missing, import should raise `RuntimeError` with rebuild instruction.

---

## 5) CLI (`leetcode_index/__main__.py`)
Commands:
- `build` → run builder and validators.
- `lookup --id 242` → print `valid-anagram`.
- `lookup --slug two-sum` → print `1`.
- `dump-id-to-slug` → stdout JSON.
- `dump-slug-to-id` → stdout JSON.

Exit codes: non‑zero on validation errors or missing build.

Installable console script in `pyproject.toml`:
```toml
[project]
name = "leetcode-index-local"
version = "0.1.0"
requires-python = ">=3.10"

[project.scripts]
leetcode-index = "leetcode_index.__main__:main"
```

---

## 6) CI guardrails (`.github/workflows/index.yml`)
- Ensure generated artifacts are up‑to‑date.
- Fail PR if diff exists after rebuild.

```yaml
name: index-check
on: [push, pull_request]
jobs:
  check:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with: { python-version: "3.11" }
      - run: python -m pip install -e .
      - run: python -m leetcode_index build
      - run: git diff --exit-code generated/_maps.py generated/id_to_slug.json generated/slug_to_id.json
```

---

## 7) Tests (`tests/`)
### 7.1 Unit tests
- `test_build.py`
  - Duplicate id/slug detection.
  - Alias collision detection.
  - Normalization of odd inputs.
  - Deterministic outputs across runs.
- `test_api.py`
  - `get_id`/`get_slug` happy paths.
  - `resolve` from id and slug.
  - Missing keys raise `KeyError`.

### 7.2 Golden files
- Seed a small fixture SSOT to verify exact JSON and `_maps.py` content (hash only if content too large).

---

## 8) Migration from existing JSON sources
1. Create a one‑off script `scripts/migrate_sources_to_ssot.py` that:
   - Loads all legacy JSON files.
   - For each record, extract `id`, `slug`, optional `title`.
   - Normalize slugs and de‑dupe.
   - If a slug changes from legacy name, put the legacy into `aliases`.
   - If multiple different slugs map to same id, choose canonical by priority: `editorial > curated > community > first-seen`; others → `aliases`.
   - Detect id collisions with different slugs and stop for manual resolution.
2. Write the resulting rows to `data/problems.index.jsonl` sorted by id.
3. Run `python -m leetcode_index build` and fix any validation failures.

---

## 9) Coding standards and quality
- Python 3.11+, `ruff` for lint, `pytest` for tests, `mypy` optional.
- No third‑party deps in runtime package.
- Builder uses only stdlib.
- Logging: print concise error lists on validation failures with line numbers.

---

## 10) Performance notes
- Dicts are small enough for memory. For 3–5k problems this is trivial.
- Build time is O(n). Lookups are O(1).

---

## 11) Error messages (spec)
- Duplicate id: `E100 duplicate id {id} at line {lineno}`
- Duplicate slug: `E101 duplicate slug {slug} at line {lineno}`
- Alias collision: `E102 alias '{alias}' collides with existing slug/alias at line {lineno}`
- Not normalized: `W200 normalized '{raw}' → '{norm}' at line {lineno}`
- Missing build: `E300 index not built. Run: python -m leetcode_index build`

---

## 12) Developer commands
```bash
# setup
pip install -e .

# build artifacts
python -m leetcode_index build

# lookups
leetcode-index lookup --id 242
leetcode-index lookup --slug two-sum

# dump for other scripts
leetcode-index dump-id-to-slug > /tmp/id2slug.json
leetcode-index dump-slug-to-id > /tmp/slug2id.json
```

---

## 13) Acceptance criteria
- ✅ SSOT exists and validates with zero errors.
- ✅ Generated artifacts are reproducible and committed.
- ✅ Importing `from leetcode_index import get_id, get_slug` works after build.
- ✅ CLI provides `build`, `lookup`, and `dump-*` commands.
- ✅ CI fails if generated files are stale or validation fails.
- ✅ Tests cover happy path and main failure modes.

---

## 14) Implementation tasks (checklist)
- [ ] Create `data/problems.index.jsonl` with a seed of 10 sample rows.
- [ ] Implement `leetcode_index/_build.py` with: normalization, validation, atomic writes, version hash.
- [ ] Implement `leetcode_index/__init__.py` API functions.
- [ ] Implement CLI in `leetcode_index/__main__.py`.
- [ ] Add `pyproject.toml` metadata and console script entry.
- [ ] Add unit tests in `tests/` and a small fixture SSOT.
- [ ] Add GitHub Action workflow `index.yml`.
- [ ] Run full roundtrip build + tests; commit generated artifacts.
- [ ] Migrate legacy JSONs into SSOT using one‑off script; add aliases as needed.

---

## 15) Future extensions
- Add `title`, `difficulty`, and `url` fields to SSOT when needed.
- Optional SQLite cache for cross‑joins; keep JSONL as SSOT.
- Export `INDEX_VERSION` to consumers for cache busting.

---

## 16) Security and safety
- No network or secrets required.
- Builder must be idempotent and safe to run repeatedly.
- Generated files are read‑only in repo policy.

---

## 17) Example code stubs

**`leetcode_index/_build.py` skeleton**
```python
from __future__ import annotations
import hashlib, json, os, re, sys, tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SSOT = ROOT / "data" / "problems.index.jsonl"
GEN = ROOT / "generated"
MAPS = GEN / "_maps.py"

_slug_rx = re.compile(r"[^a-z0-9-]+")

def norm(s: str) -> str:
    s = _slug_rx.sub("-", s.strip().lower())
    s = re.sub(r"-{2,}", "-", s)
    return s.strip("-")

def atomic_write(path: Path, data: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.NamedTemporaryFile("w", delete=False, dir=str(path.parent)) as tmp:
        tmp.write(data); tmp.flush(); os.fsync(tmp.fileno())
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
            if r["id"] in ids: sys.exit(f"E100 duplicate id {r['id']} at line {i}")
            if r["slug"] in slugs: sys.exit(f"E101 duplicate slug {r['slug']} at line {i}")
            for a in r["aliases"]:
                if a in aliases or a in slugs: sys.exit(f"E102 alias '{a}' collides at line {i}")
            ids.add(r["id"]); slugs.add(r["slug"]); aliases.update(r["aliases"])
            if norm(raw_slug) != raw_slug: print(f"W200 normalized '{raw_slug}' → '{r['slug']}' at line {i}")
            rows.append(r)

    rows.sort(key=lambda r: r["id"])  # determinism
    id_to_slug = {r["id"]: r["slug"] for r in rows}
    slug_to_id = {r["slug"]: r["id"] for r in rows}
    for r in rows:
        for a in r["aliases"]: slug_to_id[a] = r["id"]

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
```

**`leetcode_index/__init__.py` skeleton**
```python
try:
    from ..generated._maps import ID_TO_SLUG, SLUG_TO_ID, INDEX_VERSION  # type: ignore
except Exception as e:
    raise RuntimeError("E300 index not built. Run: python -m leetcode_index build") from e

def get_slug(problem_id: int) -> str: return ID_TO_SLUG[problem_id]

def get_id(slug_or_alias: str) -> int: return SLUG_TO_ID[slug_or_alias.lower()]

def exists_id(problem_id: int) -> bool: return problem_id in ID_TO_SLUG

def exists_slug(slug_or_alias: str) -> bool: return slug_or_alias.lower() in SLUG_TO_ID

def resolve(x):
    if isinstance(x, int): return x, get_slug(x)
    pid = get_id(str(x)); return pid, get_slug(pid)
```

**`leetcode_index/__main__.py` skeleton**
```python
import argparse, json
from ._build import build
from . import get_id, get_slug

def main():
    p = argparse.ArgumentParser()
    sub = p.add_subparsers(dest="cmd", required=True)
    sub.add_parser("build")
    lu = sub.add_parser("lookup"); g = lu.add_mutually_exclusive_group(required=True)
    g.add_argument("--id", type=int); g.add_argument("--slug")
    sub.add_parser("dump-id-to-slug"); sub.add_parser("dump-slug-to-id")
    a = p.parse_args()
    if a.cmd == "build": build(); return
    if a.cmd == "lookup": print(get_slug(a.id) if a.id is not None else get_id(a.slug)); return
    if a.cmd == "dump-id-to-slug":
        from ..generated._maps import ID_TO_SLUG; print(json.dumps(ID_TO_SLUG, sort_keys=True)); return
    if a.cmd == "dump-slug-to-id":
        from ..generated._maps import SLUG_TO_ID; print(json.dumps(SLUG_TO_ID, sort_keys=True)); return

if __name__ == "__main__":
    main()
```

**`.github/workflows/index.yml` skeleton**
```yaml
name: index-check
on: [push, pull_request]
jobs:
  check:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with: { python-version: "3.11" }
      - run: python -m pip install -e .
      - run: python -m leetcode_index build
      - run: git diff --exit-code generated/_maps.py generated/id_to_slug.json generated/slug_to_id.json
```

---

**End of plan.**
