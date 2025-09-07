#!/usr/bin/env python
from __future__ import annotations

import json
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

# Import the meta type converter to detect unmapped types
try:
    from .meta_types import py_type_from_meta  # type: ignore
except Exception:  # pragma: no cover
    import sys as _sys

    _sys.path.insert(0, str(Path(__file__).parent))
    from meta_types import py_type_from_meta  # type: ignore


def main() -> None:
    apath = ROOT / "archive" / "problems"
    counters = {
        "param_types": Counter(),
        "return_types": Counter(),
        "functions": Counter(),
    }
    examples: dict[str, dict] = {}

    for fp in sorted(apath.glob("*.json")):
        try:
            data = json.loads(fp.read_text())
        except Exception:
            continue
        meta = data.get("metaData")
        if not isinstance(meta, dict):
            continue
        fname = str(meta.get("name") or "")
        if fname:
            counters["functions"][fname] += 1
        # params
        params = meta.get("params")
        if isinstance(params, list):
            for p in params:
                if isinstance(p, dict):
                    t = str(p.get("type") or "").strip()
                    if t:
                        counters["param_types"][t] += 1
        # return
        ret = meta.get("return")
        if isinstance(ret, dict):
            t = str(ret.get("type") or "").strip()
            if t:
                counters["return_types"][t] += 1
        # save one example for new/uncommon types
        for t in list(counters["param_types"]) + list(counters["return_types"]):
            if t not in examples:
                examples[t] = {
                    "file": str(fp.relative_to(ROOT)),
                    "id": data.get("id"),
                    "slug": data.get("slug") or data.get("titleSlug"),
                }

    # Print summary
    print("MetaData summary (archive/problems):")
    print("")
    print("Top function names:")
    for name, cnt in counters["functions"].most_common(20):
        print(f"  {name}: {cnt}")
    print("")
    print("Parameter types (top 50):")
    for t, cnt in counters["param_types"].most_common(50):
        ex = examples.get(t, {})
        hint = f" (e.g., {ex.get('file')})" if ex else ""
        print(f"  {t}: {cnt}{hint}")
    print("")
    print("Return types (top 50):")
    for t, cnt in counters["return_types"].most_common(50):
        ex = examples.get(t, {})
        hint = f" (e.g., {ex.get('file')})" if ex else ""
        print(f"  {t}: {cnt}{hint}")

    # Unmapped types detection using the converter (maps to 'object')
    def _is_unmapped(t: str) -> bool:
        try:
            mapped = py_type_from_meta(t)
        except Exception:
            return True
        return mapped == "object"

    unmapped_params = [(t, cnt) for t, cnt in counters["param_types"].most_common() if _is_unmapped(t)]
    unmapped_returns = [(t, cnt) for t, cnt in counters["return_types"].most_common() if _is_unmapped(t)]

    if unmapped_params or unmapped_returns:
        print("")
        print("Potentially unmapped types (converter returns 'object'):")
        if unmapped_params:
            print("  Parameters:")
            for t, cnt in unmapped_params[:50]:
                ex = examples.get(t, {})
                hint = f" (e.g., {ex.get('file')})" if ex else ""
                print(f"    {t}: {cnt}{hint}")
        if unmapped_returns:
            print("  Returns:")
            for t, cnt in unmapped_returns[:50]:
                ex = examples.get(t, {})
                hint = f" (e.g., {ex.get('file')})" if ex else ""
                print(f"    {t}: {cnt}{hint}")


if __name__ == "__main__":
    main()
