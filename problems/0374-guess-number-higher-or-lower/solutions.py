from __future__ import annotations

import copy

import pytest

_pick: int = 0


def guess(num: int) -> int:
    """
    Pre-defined API for the guess game.
    @param num, your guess
    @return -1 if num is higher than the picked number
             1 if num is lower than the picked number
             0 if num is equal to the picked number
    """
    if num > _pick:
        return -1
    if num < _pick:
        return 1
    return 0


class Baseline:
    def solve(self, n: int, pick: int) -> int:
        global _pick
        _pick = pick

        low, high = 1, n
        while low <= high:
            # Using (low + high) // 2 is fine in Python, as integers have
            # arbitrary precision. But this is better practice in general.
            current_guess = low + (high - low) // 2
            feedback = guess(current_guess)
            if feedback == 0:
                return current_guess
            elif feedback == -1:  # Our guess is higher than the number
                high = current_guess - 1
            else:  # Our guess is lower than the number
                low = current_guess + 1
        return -1  # Should not be reached given the problem constraints


class Optimized:
    def solve(self, n: int, pick: int) -> int:
        global _pick
        _pick = pick

        # Lower-bound search with a half-open interval [low, high)
        low, high = 1, n
        while low < high:
            mid = low + (high - low) // 2
            result = guess(mid)
            if result == 0:
                return mid
            # If our guess is too low, the number must be in the upper half.
            if result == 1:
                low = mid + 1
            # Otherwise, the number is in the lower half, including mid.
            else:
                high = mid
        # The loop terminates when low == high, which is our answer.
        return low


# Explicit multi-export for test discovery
ALL_SOLUTIONS = [Baseline, Optimized]

TEST_CASES = [
    ("n=10, pick=6", (10, 6), 6),
    ("n=1, pick=1", (1, 1), 1),
    ("n=2, pick=1", (2, 1), 1),
    ("n=2, pick=2", (2, 2), 2),
    # Test with large numbers
    ("n=2126753390, pick=1702766719", (2126753390, 1702766719), 1702766719),
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
