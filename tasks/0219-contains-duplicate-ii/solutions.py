"""
Problem 219: Contains Duplicate II
https://leetcode.com/problems/contains-duplicate-ii/
Difficulty: easy
Tags: array,hash-map,sliding-window
"""

from __future__ import annotations


class Solution:
    def solve(self, nums: list[int], k: int) -> bool:
        """
        Returns True if there exist indices i != j such that
        nums[i] == nums[j] and abs(i - j) <= k.

        Single-pass O(n) using a hashmap of last seen index per value.
        """
        last_index: dict[int, int] = {}
        for i, v in enumerate(nums):
            if v in last_index and i - last_index[v] <= k:
                return True
            last_index[v] = i
        return False


# Allow tests to parametrize multiple variants from one file.
ALL_SOLUTIONS = [Solution]


# Canonical small test cases for default generic tests
# Each entry: (label, nums, k, expected)
TEST_CASES: list[tuple[str, list[int], int, bool]] = [
    ("basic_true", [1, 2, 3, 1], 3, True),
    ("adjacent_dup", [1, 0, 1, 1], 1, True),
    ("too_far", [1, 2, 3, 1, 2, 3], 2, False),
    ("empty", [], 1, False),
    ("single", [1], 1, False),
    ("k_zero", [1, 2, 1], 0, False),
    ("within_k", [99, 1, 99], 2, True),
    ("negatives", [-1, -2, -3, -1], 3, True),
    ("boundary_eq", [1, 2, 3, 1, 2, 3], 3, True),
    ("no_local_dup", [1, 2, 3, 1, 2, 3], 1, False),
    ("exact_k2", [1, 2, 1], 2, True),
    ("large_k", [1, 2, 3, 1], 100, True),
]


if __name__ == "__main__":
    # Convenience: running this file executes the generic spec filtered to this task.
    import subprocess
    import sys
    from pathlib import Path

    task_dir = Path(__file__).parent
    root = task_dir.parent
    task_name = task_dir.name  # e.g., "0219-contains-duplicate-ii"
    # Run the single generic spec, filtered to this task's params
    subprocess.run(
        [sys.executable, "-m", "pytest", "-q", str(root), "-k", task_name],
        check=False,
    )
