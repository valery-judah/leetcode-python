from __future__ import annotations

import pytest

from common.testgen import generate_test_cases_from_signature


@pytest.mark.parametrize(
    ("params", "ret_type", "expected"),
    [
        (
            [("nums", "list[int]"), ("k", "int")],
            "list[int]",
            (
                "\n# Signature preview: solve(self, nums: list[int], k: int)\n"
                "# - nums: e.g., [0]\n"
                "# - k: e.g., 0\n"
                "# Includes basic empty-collection variant for list-typed parameters.\n"
                "TEST_CASES = [\n"
                '    ("types", ([0], 0), [0]),\n'
                '    ("empty_list", ([], 0), [0]),\n'
                "]"
            ),
        ),
        (
            [("s", "str")],
            "str",
            (
                "\n# Signature preview: solve(self, s: str)\n"
                "# - s: e.g., 'a'\n"
                "TEST_CASES = [\n"
                "    (\"types\", ('a',), 'a'),\n"
                "]"
            ),
        ),
    ],
)
def test_generate_test_cases_from_signature(params, ret_type, expected):
    assert generate_test_cases_from_signature(params, ret_type) == expected
