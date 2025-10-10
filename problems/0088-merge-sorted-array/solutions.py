from __future__ import annotations

import copy

import pytest


class Baseline:
    def solve(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None: ...


class Optimized:
    def solve(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None: ...


# Explicit multi-export for test discovery
ALL_SOLUTIONS = [Baseline, Optimized]

TEST_CASES = [
    ("types", ([0], 0, [0], 0), None),
    ("empty_list", ([], 0, [], 0), None),
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
