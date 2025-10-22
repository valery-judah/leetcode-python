from __future__ import annotations

import copy
from math import ceil

import pytest


class Baseline:
    def solve(self, piles: list[int], h: int) -> int:
        # Brute-force: check every possible speed from 1 up to the max pile size
        # A speed of max(piles) is guaranteed to work since h >= len(piles)
        for speed in range(1, max(piles) + 2):
            hours_spent = 0
            for pile in piles:
                hours_spent += ceil(pile / speed)
            if hours_spent <= h:
                return speed
        return -1  # Should not be reached


class Optimized:
    def solve(self, piles: list[int], h: int) -> int:
        def isWorkable(probe: int):
            hours = 0
            for pile in piles:
                hours += ceil(pile / probe)
            return hours <= h

        left, right = 1, max(piles)
        while left < right:
            mid = left + (right - left) // 2
            if isWorkable(mid):
                right = mid
                # mid could be the least workable speed
            else:
                left = mid + 1
        return left


# Explicit multi-export for test discovery
ALL_SOLUTIONS = [Baseline, Optimized]

TEST_CASES = [
    ("example1", ([3, 6, 7, 11], 8), 4),
    ("example2", ([30, 11, 23, 4, 20], 5), 30),
    ("example3", ([30, 11, 23, 4, 20], 6), 23),
    ("h_equals_piles_length", ([3, 6, 7, 11], 4), 11),
    ("large_h", ([3, 6, 7, 11], 100), 1),
    ("single_pile_1", ([100], 2), 50),
    ("single_pile_2", ([100], 1), 100),
    ("single_pile_3", ([100], 100), 1),
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
