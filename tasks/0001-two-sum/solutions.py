"""
Problem 1: Two Sum
https://leetcode.com/problems/two-sum/
Difficulty: easy
Tags: array,hash-map
"""

from __future__ import annotations


class Solution:
    def solve(self, nums: list[int], target: int) -> list[int]:
        """
        Finds two numbers in a list that add up to a specific target.

        Single-pass O(n) using a hashmap of seen indices.
        """
        num_index: dict[int, int] = {}
        for i, num in enumerate(nums):
            need = target - num
            if need in num_index:
                return [num_index[need], i]
            num_index[num] = i
        return []


class BruteForce:
    def solve(self, nums: list[int], target: int) -> list[int]:
        """O(n^2) baseline: check all index pairs i < j."""
        n = len(nums)
        for i in range(n):
            for j in range(i + 1, n):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return []


ALL_SOLUTIONS = [Solution, BruteForce]

# Canonical small test cases consumed by tests via
# common.testutil.cases_from_solutions(__file__, "TEST_CASES").
# Each entry: (label, nums, target, expected_indices)
TEST_CASES: list[tuple[str, list[int], int, list[int]]] = [
    ("base", [2, 7, 11, 15], 9, [0, 1]),
    ("mid", [3, 2, 4], 6, [1, 2]),
    ("dupes", [3, 3], 6, [0, 1]),
    ("negative", [-10, 7, 19, 15], 9, [0, 2]),
    ("zero", [0, 4, 3, 0], 0, [0, 3]),
    # Additional unique-pair cases to avoid ambiguity across implementations
    ("non_adjacent", [1, 10, 25, 35, 60], 85, [2, 4]),
    ("mixed_zero_neg", [0, -1, 1, 2], 1, [0, 2]),
    ("first_last", [2, 99, 100, 1, 8], 10, [0, 4]),
    ("large_vals", [1_000_000, -1_000_000, 3, 4], 7, [2, 3]),
    ("all_negatives", [-3, -2, -5, -7], -10, [0, 3]),
]


if __name__ == "__main__":
    # Convenience: running this file executes tests for its task folder.
    import subprocess
    import sys
    from pathlib import Path

    task_dir = Path(__file__).parent
    # 1) Run example and equivalence tests quietly
    subprocess.run(
        [sys.executable, "-m", "pytest", "-q", str(task_dir), "-k", "not properties"],
        check=False,
    )
    # 2) Run property tests with verbose output and Hypothesis statistics
    subprocess.run(
        [
            sys.executable,
            "-m",
            "pytest",
            str(task_dir),
            "-k",
            "properties",
            "-vv",
            "--hypothesis-show-statistics",
        ],
        check=False,
    )
