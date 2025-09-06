from __future__ import annotations

from typing import List, Tuple

"""Helpers to auto-generate typed stub TEST_CASES and explanatory comments.

These are intentionally simple, aiming to:
- Provide arity/type-correct tuples for stub-mode tests
- Seed a couple of representative shapes (e.g., empty list if list-typed)
- Emit concise guidance on how to evolve cases to assertion-mode later
"""


def _example_for(py_t: str) -> str:
    t = py_t.strip()
    if t.startswith("list[") and t.endswith("]"):
        inner = t[5:-1]
        return f"[{_example_for(inner)}]"
    if "ListNode" in t:
        return "ListNode(1, ListNode(2))"
    if "TreeNode" in t:
        return "TreeNode(1, TreeNode(2), TreeNode(3))"
    if "UndirectedGraphNode" in t:
        return "UndirectedGraphNode(1)"
    if "RandomListNode" in t:
        return "RandomListNode(1)"
    if "NestedInteger" in t:
        return "NestedInteger(1)"
    if t in ("int",):
        return "0"
    if t in ("float",):
        return "0.0"
    if t in ("bool",):
        return "False"
    if t in ("str",):
        return "'a'"
    if t in ("None",):
        return "None"
    return "None"


def make_stub_cases(params: List[Tuple[str, str]]) -> tuple[list[tuple[str, List[str]]], List[str]]:
    """Create default stub cases and comment lines for TEST_CASES.

    Returns (cases, comments_lines) where each case is (label, args_value_exprs:list[str]).
    """
    # Primary default values
    defaults = [_example_for(t) for _, t in params]
    cases: list[tuple[str, List[str]]] = [("types", defaults)]

    # Empty-list variant when any param is list-typed
    if any(t.startswith("list[") and t.endswith("]") for _, t in params):
        empty_variant: List[str] = []
        for (_, t), dv in zip(params, defaults, strict=False):
            if t.startswith("list[") and t.endswith("]"):
                empty_variant.append("[]")
            else:
                empty_variant.append(dv)
        cases.append(("empty_list", empty_variant))

    # Comments tailored to parameter list
    lines: list[str] = []
    sig_preview = ", ".join(f"{n}: {t}" for n, t in params) if params else ""
    if sig_preview:
        lines.append(f"# Signature preview: solve(self, {sig_preview})")
    # Per-param hints
    if params:
        for name, t in params:
            if t.startswith("list[") and t.endswith("]"):
                inner = t[5:-1]
                hint = f"[{_example_for(inner)}]"
            else:
                hint = _example_for(t)
            lines.append(f"# - {name}: e.g., {hint}")

    # We also suggest an empty-collection variant when any list is present
    if any(t.startswith("list[") for _, t in params):
        lines.append("# Includes basic empty-collection variant for list-typed parameters.")

    return cases, lines
