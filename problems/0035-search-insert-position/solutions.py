from __future__ import annotations

import copy
from collections import namedtuple

import pytest


class Baseline:
    def solve(self, nums: list[int], target: int) -> int:
        for i, num in enumerate(nums):
            if num >= target:
                return i
        return len(nums)


class Optimized:
    def solve(self, nums: list[int], target: int) -> int:
        low, high = 0, len(nums)
        while low < high:
            mid = (low + high) // 2
            if nums[mid] < target:
                low = mid + 1
            else:
                high = mid
        return low


# Explicit multi-export for test discovery
ALL_SOLUTIONS = [Baseline, Optimized]

TestCase = namedtuple("TestCase", ["label", "nums", "target", "expected"])


TEST_CASES = [
    TestCase(label="example1", nums=[1, 3, 5, 6], target=5, expected=2),
    TestCase(label="example2", nums=[1, 3, 5, 6], target=2, expected=1),
    TestCase(label="example3", nums=[1, 3, 5, 6], target=7, expected=4),
    TestCase(label="edge_case_target_smaller", nums=[1, 3, 5, 6], target=0, expected=0),
    TestCase(label="edge_case_empty_list", nums=[], target=5, expected=0),
    TestCase(label="edge_case_single_element_found", nums=[1], target=1, expected=0),
    TestCase(label="edge_case_single_element_insert_before", nums=[1], target=0, expected=0),
    TestCase(label="edge_case_single_element_insert_after", nums=[1], target=2, expected=1),
]


@pytest.mark.parametrize("test_case", TEST_CASES, ids=lambda tc: tc.label)
def test_solutions(test_case: TestCase):
    for solution_class in ALL_SOLUTIONS:
        solution = solution_class()
        # Prevent test pollution by deep-copying mutable arguments
        nums_copy = copy.deepcopy(test_case.nums)
        actual = solution.solve(nums_copy, test_case.target)
        assert actual == test_case.expected


if __name__ == "__main__":
    pytest.main([__file__])
