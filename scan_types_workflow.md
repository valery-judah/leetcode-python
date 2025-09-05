Scan Types Workflow

Purpose

- Inventory `metaData` function signatures across `archive/problems/*.json`.
- Identify parameter/return types, and highlight types not yet covered by our converter (`scripts/meta_types.py`).

Run The Scan

- Generate report:
  - `python scripts/scan_metadata.py > meta-scan.txt`
- Quick peek at the top:
  - `sed -n '1,120p' meta-scan.txt`

Understanding The Report

- Top function names: frequency of `metaData.name` (helps spot common signatures).
- Parameter types: counts of `metaData.params[].type` with an example file.
- Return types: counts of `metaData.return.type` with an example file.
- Potentially unmapped types: types that our converter maps to `object` (i.e., no known mapping). These appear under:
  - `Parameters:` and/or `Returns:` sections with example file paths.

Mapping New Types

- Converter file: `scripts/meta_types.py:1`
- Add scalar aliases in `base_map` (e.g., `"long long" -> int`, `"void" -> None`).
- Collections:
  - Already supported: `T[]`, `T[][]` (recursive), and generic forms `list<...>`, `array<...>` (nested supported).
- Structs / nodes:
  - Add cases in the lower section (e.g., `"UndirectedGraphNode" -> "UndirectedGraphNode | None"`).
- Re-run the scan and ensure previously unmapped types disappear from the Unmapped section.

Validating Generation

- Use a problem with `metaData` to confirm generation works:
  - `python scripts/new_problem.py <id> --full-rewrite`
  - Open `problems/<id-slug>/solutions.py`
    - Verify typed signature matches expectations.
    - Verify `TEST_CASES` contains a simple, type-correct tuple.

Quick Checklist

- [ ] Run `python scripts/scan_metadata.py > meta-scan.txt`
- [ ] Review Parameter/Return sections for new types
- [ ] Check Unmapped section for gaps
- [ ] Update `scripts/meta_types.py` mappings
- [ ] Re-run scan to confirm coverage
- [ ] Spot-check `new_problem.py` generation on representative problems
