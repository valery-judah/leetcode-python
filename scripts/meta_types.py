from __future__ import annotations

"""Helpers to normalize LeetCode metaData types to Python type hints.

Exposed API:
- py_type_from_meta(raw: str) -> str
"""


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
