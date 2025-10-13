from __future__ import annotations

import copy
from math import gcd

import pytest


class Pythonic:
    def solve(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        if n == 0:
            return
        k %= n
        if k == 0:
            return

        # Easiest way is to use a copy
        rotated = nums[-k:] + nums[:-k]
        for i in range(n):
            nums[i] = rotated[i]


class Reverse:
    def solve(self, nums: list[int], k: int) -> None:
        def reverse_segment(arr, begin, end):
            left, right = begin, end - 1
            while left < right:
                arr[left], arr[right] = arr[right], arr[left]
                left += 1
                right -= 1

        n = len(nums)
        if not n:
            return None
        k %= n
        reverse_segment(nums, 0, n)
        reverse_segment(nums, 0, k)
        reverse_segment(nums, k, n)


class CyclingReplacement:
    def solve(self, nums: list[int], k: int) -> None:
        grcd = gcd(k, len(nums))
        _tmp = 0
        for _i in range(grcd):
            pass


# Explicit multi-export for test discovery
ALL_SOLUTIONS = [Pythonic, CyclingReplacement, Reverse]

TEST_CASES = [
    ("Simple rotation", ([1, 2, 3, 4, 5, 6, 7], 3), [5, 6, 7, 1, 2, 3, 4]),
    ("Rotation with k < len(nums)", ([-1, -100, 3, 99], 2), [3, 99, -1, -100]),
    ("Rotation with k being a multiple of len(nums)", ([1, 2, 3, 4], 8), [1, 2, 3, 4]),
    ("Rotation with k > len(nums)", ([1, 2, 3, 4], 9), [4, 1, 2, 3]),
    ("Rotation with k = 0", ([1, 2, 3], 0), [1, 2, 3]),
    ("Rotation of an empty list", ([], 5), []),
    ("Rotation of a single element list", ([1], 5), [1]),
]


@pytest.mark.parametrize(
    ("name", "args", "expected"),
    TEST_CASES,
    ids=[c[0] for c in TEST_CASES],
)
def test_solutions(name, args, expected):
    for solution_class in ALL_SOLUTIONS:
        solution = solution_class()
        # Prevent test pollution by deep-copying mutable arguments
        args_copy = copy.deepcopy(args)
        solution.solve(*args_copy)
        # The first argument is the list that should be modified in-place
        actual = args_copy[0]
        assert actual == expected


if __name__ == "__main__":
    pytest.main([__file__])
