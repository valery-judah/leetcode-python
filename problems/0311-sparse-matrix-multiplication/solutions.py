from __future__ import annotations

import copy

import pytest


class Baseline:
    def solve(self, mat1: list[list[int]], mat2: list[list[int]]) -> list[list[int]]: ...


class Optimized:
    def solve(self, mat1: list[list[int]], mat2: list[list[int]]) -> list[list[int]]: ...


# Explicit multi-export for test discovery
ALL_SOLUTIONS = [Baseline, Optimized]

TEST_CASES = [
    ("types", ([[0]], [[0]]), [[0]]),
    ("empty_list", ([], []), [[0]]),
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
