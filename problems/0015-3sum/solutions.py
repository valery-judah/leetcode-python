from __future__ import annotations

import copy

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


class WithoutSorting:
    def solve(self, nums: list[int]) -> list[list[int]]:
        triplets = set()
        seen = set()
        for i, first_num in enumerate(nums):
            if first_num in seen:
                continue

            complements: dict[int, int] = {}

            for j in range(i + 1, len(nums)):
                if nums[j] in complements:
                    triplet = tuple(sorted((first_num, complements[nums[j]], nums[j])))
                    triplets.add(triplet)
                else:
                    complement = -(first_num + nums[j])
                    complements[complement] = nums[j]

        return [list(triplet) for triplet in triplets]


class Solution:
    def solve(self, nums: list[int]) -> list[list[int]]:
        # Set to store the final unique triplets.
        # We store sorted tuples to handle permutation duplicates like (-1, 0, 1) and (1, 0, -1).
        results = set()

        # Set to keep track of numbers we've already used as the first element `a`.
        # This prevents redundant work, e.g., for inputs like [-1, 0, 1, -1].
        processed_first_nums = set()

        for i, first_num in enumerate(nums):
            if first_num in processed_first_nums:
                continue
            processed_first_nums.add(first_num)

            # Now, solve the 2Sum problem for the rest of the array.
            # Target for the other two numbers is -first_num.
            target = -first_num

            # Hash map for the 2Sum problem. Stores complements we've seen.
            # {value: index}
            seen_complements = {}

            for j in range(i + 1, len(nums)):
                second_num = nums[j]
                complement = target - second_num

                if complement in seen_complements:
                    # Found a valid triplet!
                    triplet = tuple(sorted((first_num, second_num, complement)))
                    results.add(triplet)

                # Add the current number to our map for future 2Sum checks.
                seen_complements[second_num] = j

        return [list(triplet) for triplet in results]


# Explicit multi-export for test discovery
ALL_SOLUTIONS = [TwoPointers, WithoutSorting, Solution]

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
    ("_", "args", "expected"),
    TEST_CASES,
)
def test_solutions(_, args, expected):
    for solution_class in ALL_SOLUTIONS:
        solution = solution_class()
        # Prevent test pollution by deep-copying mutable arguments
        args_copy = copy.deepcopy(args)
        actual = solution.solve(*args_copy)
        # Sort both actual and expected results for comparison
        # The order of triplets, and elements within triplets, does not matter.
        actual_sorted = sorted(map(sorted, actual))
        expected_sorted = sorted(map(sorted, expected))
        assert actual_sorted == expected_sorted


if __name__ == "__main__":
    pytest.main([__file__])
