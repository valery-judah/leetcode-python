from __future__ import annotations

import copy

import pytest


class Baseline:
    def solve(self, nums: list[int], target: int) -> bool:
        return target in nums


class Optimized:
    def solve(self, nums: list[int], target: int) -> bool:
        low, high = 0, len(nums) - 1

        while low <= high:
            mid = low + (high - low) // 2

            if nums[mid] == target:
                return True

            # The case where we can't determine which side is sorted
            if nums[low] == nums[mid] and nums[mid] == nums[high]:
                low += 1
                high -= 1
                continue

            # Left half is sorted
            if nums[low] <= nums[mid]:
                if nums[low] <= target < nums[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
            # Right half is sorted
            else:
                if nums[mid] < target <= nums[high]:
                    low = mid + 1
                else:
                    high = mid - 1

        return False


# Explicit multi-export for test discovery
ALL_SOLUTIONS = [Baseline, Optimized]

TEST_CASES = [
    ("example1", ([2, 5, 6, 0, 0, 1, 2], 0), True),
    ("example2", ([2, 5, 6, 0, 0, 1, 2], 3), False),
    ("single_element_found", ([1], 1), True),
    ("single_element_not_found", ([1], 0), False),
    ("empty_list", ([], 5), False),
    ("target_at_start", ([4, 5, 6, 7, 0, 1, 2], 4), True),
    ("target_at_end", ([4, 5, 6, 7, 0, 1, 2], 2), True),
    ("target_in_middle_left_part", ([4, 5, 6, 7, 0, 1, 2], 5), True),
    ("target_in_middle_right_part", ([4, 5, 6, 7, 0, 1, 2], 1), True),
    ("pivot_element", ([4, 5, 6, 7, 0, 1, 2], 0), True),
    ("not_found_greater", ([4, 5, 6, 7, 0, 1, 2], 8), False),
    ("not_found_smaller", ([4, 5, 6, 7, 0, 1, 2], -1), False),
    ("duplicates_tricky", ([1, 0, 1, 1, 1], 0), True),
    ("all_duplicates_found", ([1, 1, 1, 1, 1], 1), True),
    ("all_duplicates_not_found", ([1, 1, 1, 1, 1], 2), False),
    ("two_elements_rotated_found_1", ([3, 1], 3), True),
    ("two_elements_rotated_found_2", ([3, 1], 1), True),
    ("two_elements_rotated_not_found", ([3, 1], 2), False),
    ("no_rotation_found", ([1, 2, 3, 4, 5], 3), True),
    ("no_rotation_not_found", ([1, 2, 3, 4, 5], 6), False),
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
