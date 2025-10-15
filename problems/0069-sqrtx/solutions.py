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
        """
        An efficient O(log n) solution using binary search.
        It searches for the integer square root in the range [2, x // 2].
        The search space is halved in each iteration until the root is found.
        """
        # Base cases for 0 and 1
        if x < 2:
            return x
        # Set the search range for the square root
        left, right = 2, x // 2
        while left <= right:
            # Calculate the midpoint to check
            mid = (left + right) // 2
            num = mid * mid
            if num > x:
                # The square is too large, so search in the left half
                right = mid - 1
            elif num < x:
                # The square is too small, so search in the right half
                left = mid + 1
            else:
                # Found the exact square root
                return mid
        # If no exact square is found, 'right' will be the integer square root
        return right


class NewtonsMethod:
    def solve(self, x: int) -> int:
        """
        A fast iterative solution using Newton's method.
        It starts with an initial guess and refines it in each iteration
        using the formula: r = (r + x // r) // 2.
        The process converges quadratically to the integer square root.
        """
        if x == 0:
            return 0
        # Start with an initial guess for the root (x itself)
        r = x
        # Iteratively refine the guess until r*r is no longer greater than x
        while r * r > x:
            # Apply the Newton-Raphson formula to get a better approximation
            r = (r + x // r) // 2
        return r


class BinarySearchFirstFalse:
    def solve(self, x: int) -> int:
        """
        An alternative binary search to find the first integer k where k*k > x.
        This is analogous to std::upper_bound. The final answer is k - 1.
        """
        # Search space is the half-open interval [0, x + 1)
        left, right = 0, x + 1
        # Loop until the search space is exhausted (left == right)
        while left < right:
            # Standard midpoint calculation to prevent overflow
            mid = left + (right - left) // 2
            if mid * mid <= x:
                # If mid*mid is not too large, the boundary must be higher.
                # We can discard mid and everything to its left.
                left = mid + 1
            else:
                # mid*mid is too large. mid could be the first such number.
                # We keep mid in the search space.
                right = mid
        # The loop terminates when left is the first integer where left*left > x.
        # The integer square root is therefore left - 1.
        return left - 1


# Explicit multi-export for test discovery
ALL_SOLUTIONS = [Baseline, BinarySearch, NewtonsMethod, BinarySearchFirstFalse]

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
