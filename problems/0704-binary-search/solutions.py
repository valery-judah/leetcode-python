from __future__ import annotations

import copy

import pytest


class Baseline:
    def solve(self, nums: list[int], target: int) -> int: ...


class Optimized:
    def solve(self, nums: list[int], target: int) -> int: ...


# Explicit multi-export for test discovery
ALL_SOLUTIONS = [Baseline, Optimized]

TEST_CASES = [
    ("single_element_found", ([5], 5), 0),
    ("single_element_missing", ([5], 4), -1),
    ("target_at_left", ([1, 2, 3, 4, 5], 1), 0),
    ("target_at_right", ([1, 2, 3, 4, 5], 5), 4),
    ("target_in_middle", ([1, 3, 5, 7, 9], 7), 3),
    ("missing_between_values", ([1, 3, 5, 7, 9], 4), -1),
    ("all_negative_numbers", ([-10, -3, 0, 5, 9], -3), 1),
    ("target_below_range", ([2, 4, 6, 8, 10], 1), -1),
    ("target_above_range", ([2, 4, 6, 8, 10], 12), -1),
    ("empty_array", ([], 0), -1),
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
