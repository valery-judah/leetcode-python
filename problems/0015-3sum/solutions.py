from __future__ import annotations

import pytest


class TwoPointers:
    def solve(self, nums: list[int]) -> list[list[int]]:
        triplets = []
        nums.sort()
        for i, a in enumerate(nums):
            if a > 0:
                break
            if i > 0 and a == nums[i - 1]:
                continue
            left, right = i + 1, len(nums) - 1
            while left < right:
                cur_sum = a + nums[left] + nums[right]
                if cur_sum > 0:
                    right -= 1
                elif cur_sum < 0:
                    left += 1
                else:
                    triplets.append([a, nums[left], nums[right]])
                    # moving pointers
                    left += 1
                    # here we have to remember that we need to guarantee triplets uniqueness
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    right -= 1
        return triplets


class Optimized:
    def solve(self, nums: list[int] | None = None) -> list[list[int]]: ...


# Explicit multi-export for test discovery
ALL_SOLUTIONS = [TwoPointers]


TEST_CASES = [
    # --- Corrected User-Provided & Basic Edge Cases ---
    ("empty_list", ([],), []),
    ("not_enough_elements_one", ([0],), []),
    ("not_enough_elements_two", ([1, -1],), []),
    # --- No Solution Cases ---
    ("no_solution_all_positives", ([1, 2, 3, 4, 5],), []),
    ("no_solution_all_negatives", ([-1, -2, -3, -4],), []),
    ("no_solution_mixed", ([-1, -2, 4, 5],), []),
    # --- Standard Cases & LeetCode Examples ---
    ("leetcode_example_1", ([-1, 0, 1, 2, -1, -4],), [[-1, -1, 2], [-1, 0, 1]]),
    ("simple_case", ([-1, 0, 1],), [[-1, 0, 1]]),
    ("multiple_solutions", ([-4, -1, -1, 0, 1, 2],), [[-1, -1, 2], [-1, 0, 1]]),
    # --- Critical Cases for Duplicate and Zero Handling ---
    ("all_zeros", ([0, 0, 0, 0, 0],), [[0, 0, 0]]),
    ("single_triplet_of_zeros", ([0, 0, 0],), [[0, 0, 0]]),
    ("duplicates_in_solution", ([-2, 1, 1, 2],), [[-2, 1, 1]]),
    ("many_duplicates_to_skip", ([1, 1, 1, -2, -2, -2, 1, 1],), [[-2, 1, 1]]),
    (
        "complex_case_with_zeros_and_duplicates",
        ([-1, 0, 1, 0, 2, -1, -4, 0],),
        [[-1, -1, 2], [-1, 0, 1], [0, 0, 0]],
    ),
]
@pytest.mark.parametrize(
    "_, nums, expected",
    TEST_CASES,
)
def test_solutions(_, nums, expected):
    for solution_class in ALL_SOLUTIONS:
        solution = solution_class()
        actual = solution.solve(*nums)
        assert sorted(map(sorted, actual)) == sorted(map(sorted, expected))


if __name__ == "__main__":
    pytest.main([__file__])
