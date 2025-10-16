from __future__ import annotations

import copy

import pytest


class Baseline:
    def solve(self, nums: list[int]) -> int:
        left, right = 0, len(nums) - 1
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid  # a long reasoning here
        return nums[right]


class Optimized:
    def solve(self, nums: list[int]) -> int:
        """
        Finds the minimum element in a rotated sorted array using binary search.
        This approach has a time complexity of O(log n).
        """
        res = nums[0]
        left, right = 0, len(nums) - 1

        while left <= right:
            # If the current window is sorted, the left element is the minimum
            if nums[left] <= nums[right]:
                res = min(res, nums[left])
                break

            mid = (left + right) // 2
            res = min(res, nums[mid])

            # Decide which half to search in
            if nums[mid] >= nums[left]:
                # The left part is sorted, so the pivot is in the right part
                left = mid + 1
            else:
                # The pivot is in the left part (including mid)
                right = mid - 1
        return res


# Explicit multi-export for test discovery
ALL_SOLUTIONS = [Baseline, Optimized]

TEST_CASES = [
    ("single_element", ([1],), 1),
    ("basic_rotation", ([3, 4, 5, 1, 2],), 1),
    ("three_elements", ([2, 0, 1],), 0),
    ("full_rotation_to_sorted", ([1, 2, 3, 4, 5],), 1),
    ("large_numbers", ([4, 5, 6, 7, 0, 1, 2],), 0),
    ("two_elements_rotated", ([2, 1],), 1),
    ("two_elements_sorted", ([1, 2],), 1),
    ("pivot_on_right", ([5, 6, 1, 2, 3, 4],), 1),
    ("pivot_on_left", ([2, 3, 4, 5, 6, 1],), 1),
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
