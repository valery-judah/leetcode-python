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
    if t.endswith("[]"):
        inner = t[:-2]
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
    if t in ("int", "long"):
        return "0"
    if t in ("float", "double"):
        return "0.0"
    if t in ("bool",):
        return "False"
    if t in ("str", "character"):
        return '"a"'
    if t in ("None",):
        return "None"
    return "None"


def make_stub_cases(params: List[Tuple[str, str]]) -> list[tuple[str, List[str]]]:
    """Create default stub cases and comment lines for TEST_CASES.

    Returns (cases, comments_lines) where each case is (label, args_value_exprs:list[str]).
    """
    # Primary default values
    defaults = [_example_for(t) for _, t in params]
    cases: list[tuple[str, List[str]]] = [("types", defaults)]

    # Empty-list variant when any param is list-typed
    if any(t.startswith("list[") and t.endswith("]") for _, t in params):
        empty_variant: List[str] = []
        # Python 3.9 compatibility: no 'strict' kw in zip
        for (_, t), dv in zip(params, defaults, strict=False):
            if t.startswith("list[") and t.endswith("]"):
                empty_variant.append("[]")
            else:
                empty_variant.append(dv)
        cases.append(("empty_list", empty_variant))

    return cases


def generate_test_cases_from_signature(params: list[tuple[str, str]], ret_type: str) -> str:
    """Generate a string for TEST_CASES based on function signature."""
    stub_cases = make_stub_cases(params)

    def _tuple_expr(values: list[str]) -> str:
        if not values:
            return "()"
        if len(values) == 1:
            return f"({values[0]},)"
        return f"""({", ".join(values)})"""

    cases_lines: list[str] = []
    stub_expected = _example_for(ret_type)
    for label, raw_values in stub_cases:
        # raw_values are already expressions (strings)
        cases_lines.append(f'    ("{label}", {_tuple_expr(raw_values)}, {stub_expected}),')

    return "TEST_CASES = [\n" + "\n".join(cases_lines) + "\n]"
