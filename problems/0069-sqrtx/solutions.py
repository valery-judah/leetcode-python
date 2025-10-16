from __future__ import annotations

import copy

import pytest


class Baseline:
    def solve(self, x: int) -> int:
        """
        A simple linear scan approach.
        It iterates from 1 upwards, checking the square of each number.
        The loop stops when the square exceeds x, and it returns the previous number.
        """
        if x == 0:
            return 0
        # Start checking from 1
        i = 1
        # Loop until we find a number whose square is greater than x
        while i * i <= x:
            i += 1
        # The correct integer square root is the number just before i
        return i - 1


class BinarySearch:
    def solve(self, x: int) -> int:
        if x < 2:
            return x
        res = 0
        left, right = 0, x - 1
        while left <= right:
            mid = left + (right - left) // 2
            square = mid * mid
            if square > x:
                right = mid - 1
            elif square <= x:
                res = mid
                left = mid + 1

        return res


# Explicit multi-export for test discovery
ALL_SOLUTIONS = [Baseline, BinarySearch]

TEST_CASES = [
    ("zero", (0,), 0),
    ("one", (1,), 1),
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
