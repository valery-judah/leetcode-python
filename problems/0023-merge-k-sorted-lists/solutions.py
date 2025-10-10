from __future__ import annotations

import copy

import pytest

from common.types import ListNode


class Baseline:
    def solve(self, lists: list[ListNode | None]) -> ListNode | None: ...


class Optimized:
    def solve(self, lists: list[ListNode | None]) -> ListNode | None: ...


# Explicit multi-export for test discovery
ALL_SOLUTIONS = [Baseline, Optimized]

TEST_CASES = [
    ("types", ([ListNode(1, ListNode(2))],), ListNode(1, ListNode(2))),
    ("empty_list", ([],), ListNode(1, ListNode(2))),
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
