#!/usr/bin/env python
from __future__ import annotations

import json
import sys
from pathlib import Path

from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parents[1]


def main() -> int:
    schema_path = ROOT / "templates" / "stats.schema.json"
    if not schema_path.exists():
        print(f"Schema not found: {schema_path}", file=sys.stderr)
        return 2
    schema = json.loads(schema_path.read_text())
    validator = Draft202012Validator(schema)

    problems_dir = ROOT / "problems"
    if not problems_dir.exists():
        print("No problems directory found; nothing to validate.")
        return 0

    stats_files = sorted(problems_dir.glob("*/stats.json"))
    if not stats_files:
        print("No stats.json files found; nothing to validate.")
        return 0

    any_errors = False
    for fp in stats_files:
        try:
            data = json.loads(fp.read_text())
        except Exception as e:
            print(f"ERROR: {fp}: invalid JSON: {e}")
            any_errors = True
            continue
        errors = sorted(validator.iter_errors(data), key=lambda e: e.path)
        if errors:
            any_errors = True
            print(f"ERROR: {fp}: schema validation failed:")
            for err in errors:
                path = "/".join(str(p) for p in err.path) or "<root>"
                print(f"  - at {path}: {err.message}")

    if any_errors:
        return 1
    print(f"Validated {len(stats_files)} stats.json file(s); all good.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
