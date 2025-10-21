from __future__ import annotations

import copy

import pytest


class Bounds:
    def solve(self, nums: list[int], target: int) -> list[int]:

        def lower_bound(a, x):
            left, right = 0, len(a)  # right is one past the last index
            while left < right:
                mid = (left + right) // 2
                if a[mid] < x:
                    left = mid + 1
                else:
                    right = mid  # keep mid as candidate
            return left  # in [0..n]

        def upper_bound(a, x):
            left, right = 0, len(a)  # right is one past the last index
            while left < right:
                mid = (left + right) // 2
                if a[mid] <= x:
                    left = mid + 1
                else:
                    right = mid  # keep mid as candidate
            return left  # in [0..n]

        lb = lower_bound(nums, target)
        if lb == len(nums) or nums[lb] != target:
            return [-1, -1]
        ub = upper_bound(nums, target) - 1
        return [lb, ub]


class LeetCodesApproach:
    def solve(self, nums: list[int], target: int) -> list[int]:

        def find_last(nums, target) -> int:
            left, right = 0, len(nums) - 1
            while left <= right:
                mid = left + (right - left) // 2
                if nums[mid] < target:
                    left = mid + 1
                elif nums[mid] > target:
                    right = mid - 1
                else:
                    if right == mid or nums[mid] != nums[mid + 1]:
                        return mid
                    else:
                        left = mid + 1
            return -1

        def find_first(nums, target) -> int:
            left, right = 0, len(nums) - 1
            while left <= right:
                mid = left + (right - left) // 2
                if nums[mid] < target:
                    left = mid + 1
                elif nums[mid] > target:
                    right = mid - 1
                else:
                    if left == mid or nums[mid] != nums[mid - 1]:
                        return mid
                    else:
                        right = mid - 1
            return -1

        left = find_first(nums, target=target)
        if left == -1:
            return [-1, -1]
        right = find_last(nums, target)
        # first - find first occurence; to do it let's write some tests
        return [left, right]


class Other:
    def solve(self, nums: list[int], target: int) -> list[int]:
        def find_bound(arr, t, is_first):
            low = 0
            high = len(arr) - 1
            index = -1

            while low <= high:
                mid = low + (high - low) // 2
                if arr[mid] == t:
                    index = mid
                    if is_first:
                        # Try to find an earlier occurrence
                        high = mid - 1
                    else:
                        # Try to find a later occurrence
                        low = mid + 1
                elif arr[mid] < t:
                    low = mid + 1
                else:  # arr[mid] > t
                    high = mid - 1
            return index

        first_pos = find_bound(nums, target, True)
        if first_pos == -1:
            return [-1, -1]

        last_pos = find_bound(nums, target, False)
        return [first_pos, last_pos]


# Explicit multi-export for test discovery
ALL_SOLUTIONS = [LeetCodesApproach, Other, Bounds]

TEST_CASES = [
    ("example1", ([5, 7, 7, 8, 8, 10], 8), [3, 4]),
    ("example2", ([5, 7, 7, 8, 8, 10], 6), [-1, -1]),
    ("empty", ([], 0), [-1, -1]),
    ("target_at_start", ([8, 8, 8, 9, 10], 8), [0, 2]),
    ("target_at_end", ([1, 2, 8, 8, 8], 8), [2, 4]),
    ("single_element_match", ([8], 8), [0, 0]),
    ("single_element_no_match", ([8], 9), [-1, -1]),
    ("target_not_present_middle", ([1, 2, 4, 5], 3), [-1, -1]),
    ("all_elements_are_target", ([8, 8, 8, 8], 8), [0, 3]),
    ("single_occurrence", ([1, 2, 3, 4, 5], 3), [2, 2]),
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
