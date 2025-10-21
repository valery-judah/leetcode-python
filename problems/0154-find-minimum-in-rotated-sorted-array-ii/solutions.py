from __future__ import annotations

import copy

import pytest


class Baseline:
    def solve(self, nums: list[int]) -> int:
        """A simple linear scan is a valid baseline."""
        # Constraints: 1 <= n <= 5000, so list is never empty.
        return min(nums)


class Optimized:
    def solve(self, nums: list[int]) -> int:
        """Binary search with duplicate handling."""
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] > nums[right]:
                # The minimum is in the right half
                left = mid + 1
            elif nums[mid] < nums[right]:
                # The minimum is in the left half (or mid is the minimum)
                right = mid
            else:  # nums[mid] == nums[right]
                # We can't determine which side the minimum is on.
                # Safely discard the rightmost element.
                right -= 1
        return nums[left]


# Explicit multi-export for test discovery
ALL_SOLUTIONS = [Baseline, Optimized]

TEST_CASES = [
    # From problem description
    ("example_1", ([1, 3, 5],), 1),
    ("example_2", ([2, 2, 2, 0, 1],), 0),
    # No rotation
    ("no_rotation_asc", ([1, 2, 3, 4, 5],), 1),
    ("no_rotation_with_duplicates", ([1, 1, 2, 3, 3],), 1),
    # Rotated
    ("rotated_simple", ([3, 4, 5, 1, 2],), 1),
    ("rotated_pivot_right", ([4, 5, 6, 7, 0, 1, 2],), 0),
    ("rotated_pivot_left", ([13, 15, 17, 11],), 11),
    # With duplicates - the crux of this problem
    ("duplicates_at_ends_and_middle", ([3, 3, 1, 3],), 1),
    ("duplicates_around_pivot", ([3, 1, 1, 2],), 1),
    ("duplicates_at_ends", ([3, 0, 3, 3, 3],), 0),
    ("duplicates_everywhere", ([1, 3, 1, 1, 1],), 1),
    # All elements are the same
    ("all_elements_same", ([2, 2, 2, 2, 2],), 2),
    # Single element
    ("single_element", ([1],), 1),
    # Two elements
    ("two_elements_rotated", ([2, 1],), 1),
    ("two_elements_not_rotated", ([1, 2],), 1),
    ("two_elements_same", ([1, 1],), 1),
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
