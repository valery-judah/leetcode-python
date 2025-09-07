from __future__ import annotations

import json
from pathlib import Path

"""Helpers to normalize LeetCode metaData types to Python type hints.

Exposed API:
- py_type_from_meta(raw: str) -> str
"""

# Load the generated type mapping file
_type_mapping: dict[str, str] | None = None


def _load_type_mapping() -> dict[str, str]:
    """
    Loads the generated and manual type mapping files, with manual
    overrides taking precedence.
    """
    global _type_mapping
    if _type_mapping is not None:
        return _type_mapping

    # Load the generated mapping file
    mapping: dict[str, str] = {}
    generated_mapping_file = Path(__file__).parent / "type_mapping.json"
    if generated_mapping_file.exists():
        try:
            loaded_data = json.loads(generated_mapping_file.read_text())
            if isinstance(loaded_data, dict):
                mapping.update(loaded_data)
        except (OSError, json.JSONDecodeError):
            pass  # Ignore errors in generated file

    # Load the manual override mapping file
    manual_mapping_file = Path(__file__).parent / "type_mapping.manual.json"
    if manual_mapping_file.exists():
        try:
            manual_data = json.loads(manual_mapping_file.read_text())
            if isinstance(manual_data, dict):
                mapping.update(manual_data)  # Overrides generated mappings
        except (OSError, json.JSONDecodeError):
            pass  # Ignore errors in manual file

    _type_mapping = mapping
    return _type_mapping


def py_type_from_meta(t: str) -> str:
    """Convert a LeetCode metaData type string into a Python type annotation.

    Examples:
    - "integer" -> "int"
    - "integer[]" -> "list[int]"
    - "integer[][]" -> "list[list[int]]"
    - "ListNode" -> "ListNode | None"
    - "ListNode[]" -> "list[ListNode | None]"
    - "character" -> "str"
    Unknown types fall back to "object".
    """
    raw = (t or "").strip()

    # First, check the pre-generated mapping file
    mapping = _load_type_mapping()
    if raw in mapping:
        return mapping[raw]

    # Fallback to original logic if not found in mapping
    tl = raw.lower()

    base_map = {
        "integer": "int",
        "int": "int",
        "long": "int",
        "long long": "int",
        "short": "int",
        "byte": "int",
        "float": "float",
        "double": "float",
        "string": "str",
        "string ": "str",
        "boolean": "bool",
        "bool": "bool",
        "character": "str",
        "char": "str",
        "void": "None",
    }

    # Handle nested arrays like integer[][] or ListNode[]
    if tl.endswith("[]"):
        inner = raw[:-2]
        return f"list[{py_type_from_meta(inner)}]"

    # Support generic-like forms: list<...>, possibly nested
    tl_nospace = tl.replace(" ", "")
    if (tl_nospace.startswith("list<") or tl_nospace.startswith("array<")) and tl_nospace.endswith(">"):
        inner = raw[raw.find("<") + 1 : raw.rfind(">")]
        return f"list[{py_type_from_meta(inner)}]"

    # Common LeetCode struct types
    if tl == "listnode":
        return "ListNode | None"
    if tl == "treenode":
        return "TreeNode | None"
    if tl == "narytreenode":
        return "Node | None"
    if tl == "node":
        return "Node | None"
    if tl == "undirectedgraphnode":
        return "UndirectedGraphNode | None"
    if tl == "randomlistnode":
        return "RandomListNode | None"
    if tl == "nestedinteger":
        return "NestedInteger"

    return base_map.get(tl, base_map.get(tl.capitalize(), "object"))
