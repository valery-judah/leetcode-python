from __future__ import annotations

import copy

import pytest


class WithFunc:
    def solve(self, nums: list[int], target: int) -> int:
        if not nums:
            return -1

        def find_pivot_index(nums: list[int]) -> int:
            left, right = 0, len(nums) - 1
            while left < right:
                mid = left + (right - left) // 2
                if nums[mid] < nums[right]:
                    right = mid
                else:
                    left = mid + 1
            return left

        left, right = 0, len(nums) - 1
        # now we have to find a pivot element
        pivot = find_pivot_index(nums)
        # and set search space accordingly to what?
        if nums[pivot] <= target and target <= nums[right]:
            left = pivot
        else:
            right = pivot - 1

        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] > target:
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                return mid
        return -1


# Explicit multi-export for test discovery
ALL_SOLUTIONS = [WithFunc]

TEST_CASES = [
    ("types", ([4, 5, 6, 7, 0, 1, 2], 0), 4),
    ("missing target", ([4, 5, 6, 7, 0, 1, 2], 3), -1),
    ("empty_list", ([], 0), -1),
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
