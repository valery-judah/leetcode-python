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
    ("example1", ([1, 3, 5, 6], 5), 2),
    ("example2", ([1, 3, 5, 6], 2), 1),
    ("example3", ([1, 3, 5, 6], 7), 4),
    ("edge_case_target_smaller", ([1, 3, 5, 6], 0), 0),
    ("edge_case_empty_list", ([], 5), 0),
    ("edge_case_single_element_found", ([1], 1), 0),
    ("edge_case_single_element_insert_before", ([1], 0), 0),
    ("edge_case_single_element_insert_after", ([1], 2), 1),
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
