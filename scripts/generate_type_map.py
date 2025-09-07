#!/usr/bin/env python
from __future__ import annotations

import json
from pathlib import Path

try:
    from meta_types import py_type_from_meta
except ImportError:
    import sys

    sys.path.insert(0, str(Path(__file__).parent))
    from meta_types import py_type_from_meta

import re

ROOT = Path(__file__).resolve().parents[1]
METADATA_FILE = ROOT / "scripts" / "metadata_scanned.txt"
OUTPUT_FILE = ROOT / "scripts" / "type_mapping.json"


def main() -> None:
    """
    Scans the metadata summary file, extracts all unique types, and generates
    a JSON mapping from raw types to Python types, skipping SQL-related types.
    """
    if not METADATA_FILE.is_file():
        print(f"Error: Metadata file not found: {METADATA_FILE}")
        return

    all_types = set()
    type_pattern = re.compile(r"^\s+([^:]+):\s+\d+.*$")

    with open(METADATA_FILE) as f:
        for line in f:
            match = type_pattern.match(line)
            if match:
                all_types.add(match.group(1).strip())

    # Filter out empty strings and SQL types
    filtered_types = {t for t in all_types if t and "sql" not in t.lower()}

    # Generate the mapping using the existing converter
    type_mapping = {raw_type: py_type_from_meta(raw_type) for raw_type in sorted(list(filtered_types))}

    # Write the mapping to the output file
    with open(OUTPUT_FILE, "w") as f:
        json.dump(type_mapping, f, indent=2, sort_keys=True)
        f.write("\n")

    print(f"Successfully generated type mapping to {OUTPUT_FILE}")
    print(f"Found and mapped {len(type_mapping)} unique types from metadata.")
    print("\nNote: You can manually override or add mappings in " "'scripts/type_mapping.manual.json'.")


if __name__ == "__main__":
    main()
