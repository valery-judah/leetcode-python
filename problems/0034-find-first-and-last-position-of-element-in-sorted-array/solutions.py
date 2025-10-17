from __future__ import annotations

import copy

import pytest


class Baseline:
    def solve(self, nums: list[int], target: int) -> list[int]:
        """
        Finds the first and last positions of a target in a sorted array.
        This baseline approach uses two separate binary searches.
        """
        first = self._find_first(nums, target)
        if first == -1:
            return [-1, -1]
        last = self._find_last(nums, target)
        return [first, last]

    def _find_first(self, nums: list[int], target: int) -> int:
        low, high = 0, len(nums) - 1
        first_pos = -1
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == target:
                first_pos = mid
                high = mid - 1  # Look for an earlier occurrence
            elif nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        return first_pos

    def _find_last(self, nums: list[int], target: int) -> int:
        low, high = 0, len(nums) - 1
        last_pos = -1
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == target:
                last_pos = mid
                low = mid + 1  # Look for a later occurrence
            elif nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        return last_pos


class Optimized:
    def solve(self, nums: list[int], target: int) -> list[int]:
        """
        Optimized approach using a single, reusable binary search function
        to find both the first and last positions.
        """
        first = self._binary_search(nums, target, find_first=True)
        if first == -1:
            return [-1, -1]
        last = self._binary_search(nums, target, find_first=False)
        return [first, last]

    def _binary_search(self, nums: list[int], target: int, find_first: bool) -> int:
        low, high = 0, len(nums) - 1
        position = -1
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == target:
                position = mid
                if find_first:
                    high = mid - 1  # Continue searching on the left
                else:
                    low = mid + 1  # Continue searching on the right
            elif nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        return position


class TemplateBased:
    def solve(self, nums: list[int], target: int) -> list[int]:
        """
        Finds the first and last positions using a binary search template
        where the loop condition is `left + 1 < right`.
        """
        if not nums:
            return [-1, -1]

        first = self._find_first(nums, target)
        if first == -1:
            return [-1, -1]
        last = self._find_last(nums, target)
        return [first, last]

    def _find_first(self, nums: list[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left + 1 < right:
            mid = (left + right) // 2
            if nums[mid] < target:
                left = mid
            else:  # nums[mid] >= target
                right = mid

        if nums[left] == target:
            return left
        if nums[right] == target:
            return right
        return -1

    def _find_last(self, nums: list[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left + 1 < right:
            mid = (left + right) // 2
            if nums[mid] > target:
                right = mid
            else:  # nums[mid] <= target
                left = mid

        if nums[right] == target:
            return right
        if nums[left] == target:
            return left
        return -1


# Explicit multi-export for test discovery
ALL_SOLUTIONS = [Baseline, Optimized, TemplateBased]

TEST_CASES = [
    ("example1", ([5, 7, 7, 8, 8, 10], 8), [3, 4]),
    ("example2", ([5, 7, 7, 8, 8, 10], 6), [-1, -1]),
    ("example3", ([], 0), [-1, -1]),
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
