from __future__ import annotations

import copy

import pytest


class Baseline:
    def solve(self, x: int) -> int:
        if x < 2:
            return x
        res = 0
        for i in range(2, x // 2):
            if i * i >= x:
                res = i
        return res

class Optimized:
    def solve(self, x: int) -> int: ...


# Explicit multi-export for test discovery
ALL_SOLUTIONS = [Baseline]

TEST_CASES = [
    ("zero", (0,), 0),
    ("one", (1,), 1),
    ("two", (2,), 1),
    ("three", (3,), 1),
    ("four", (4,), 2),
    ("eight", (8,), 2),
    ("nine", (9,), 3),
    ("sixteen", (16,), 4),
    ("twenty_four", (24,), 4),
    ("twenty_five", (25,), 5),
    ("twenty_six", (26,), 5),
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
