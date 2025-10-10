from __future__ import annotations

import copy

import pytest

from common.types import ListNode


class Baseline:
    def solve(self, head: ListNode | None, pos: int) -> bool: ...


class Optimized:
    def solve(self, head: ListNode | None, pos: int) -> bool: ...


# Explicit multi-export for test discovery
ALL_SOLUTIONS = [Baseline, Optimized]

TEST_CASES = [
    ("types", (ListNode(1, ListNode(2)), 0), False),
]


@pytest.mark.parametrize(
    ("_", "args", "expected"),
    TEST_CASES,
)
def test_solutions(_, args, expected):
    for solution_class in ALL_SOLUTIONS:
        solution = solution_class()
        # Prevent test pollution by deep-copying mutable arguments
        args_copy = copy.deepcopy(args)
        actual = solution.solve(*args_copy)
        assert actual == expected


if __name__ == "__main__":
    pytest.main([__file__])
