from __future__ import annotations

import copy

import pytest


class Baseline:
    def solve(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # Make a copy of the first m elements of nums1.
        nums1_copy = nums1[:m]

        # Initialize pointers for nums1_copy, nums2, and the main nums1 array.
        p1 = 0
        p2 = 0
        p = 0

        # Compare elements from nums1_copy and nums2 and write the smaller one into nums1.
        while p1 < m and p2 < n:
            if nums1_copy[p1] <= nums2[p2]:
                nums1[p] = nums1_copy[p1]
                p1 += 1
            else:
                nums1[p] = nums2[p2]
                p2 += 1
            p += 1

        # If there are remaining elements in nums1_copy, copy them.
        if p1 < m:
            nums1[p:] = nums1_copy[p1:]

        # If there are remaining elements in nums2, copy them.
        if p2 < n:
            nums1[p:] = nums2[p2:]


class Optimized:
    def solve(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # p1 points to the last initialized element in nums1.
        p1 = m - 1
        # p2 points to the last element in nums2.
        p2 = n - 1
        # 'to' points to the last position in nums1, where the largest element will be placed.
        to = m + n - 1

        # We merge in reverse order. As long as there are elements to compare in both arrays...
        while p1 >= 0 and p2 >= 0:
            # If the element in nums1 is larger, place it at the 'to' position.
            if nums1[p1] > nums2[p2]:
                nums1[to] = nums1[p1]
                p1 -= 1
            # Otherwise, the element in nums2 is larger or equal, so place it instead.
            else:
                nums1[to] = nums2[p2]
                p2 -= 1
            # Move the insertion pointer to the left.
            to -= 1

        # If p1 becomes < 0, it means all elements from the initial nums1 have been placed.
        # Any remaining elements in nums2 are smaller than all of them and can be copied directly.
        # Using slice assignment is a concise and efficient way to copy these remaining elements.
        if p2 >= 0:
            nums1[: p2 + 1] = nums2[: p2 + 1]



# Explicit multi-export for test discovery
ALL_SOLUTIONS = [Baseline, Optimized]

TEST_CASES = [
    # name, (nums1, m, nums2, n), expected_nums1
    ("m=3, n=3", ([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3), [1, 2, 2, 3, 5, 6]),
    ("m=1, n=0", ([1], 1, [], 0), [1]),
    ("m=0, n=1", ([0], 0, [1], 1), [1]),
    ("m=1, n=1", ([2, 0], 1, [1], 1), [1, 2]),
    (
        "m=3, n=3, nums2 smaller",
        ([4, 5, 6, 0, 0, 0], 3, [1, 2, 3], 3),
        [1, 2, 3, 4, 5, 6],
    ),
    ("empty lists", ([], 0, [], 0), []),
]


@pytest.mark.parametrize(
    ("_", "args", "expected_nums1"),
    TEST_CASES,
)
def test_solutions(_, args, expected_nums1):
    for solution_class in ALL_SOLUTIONS:
        solution = solution_class()
        # Prevent test pollution by deep-copying mutable arguments
        args_copy = copy.deepcopy(args)
        nums1 = args_copy[0]
        solution.solve(*args_copy)
        assert nums1 == expected_nums1


if __name__ == "__main__":
    pytest.main([__file__])
