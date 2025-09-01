"""
Problem 217: Contains Duplicate
https://leetcode.com/problems/contains-duplicate/
Difficulty: easy
Tags: array,hash-set,sorting
"""

from __future__ import annotations


class BruteForce:
    def solve(self, nums: list[int]) -> bool:
        for i, v in enumerate(nums):
            for j in range(i, len(nums)):
                if v == nums[j]:
                    return True
        return False


class SetBased:
    def solve(self, nums: list[int]) -> bool:
        seen: set[int] = set()
        for n in nums:
            if n in seen:
                return True
            seen.add(n)
        return False


class Sorting:
    def solve(self, nums: list[int]) -> bool:
        nums_sorted = sorted(nums)
        return any(nums_sorted[i] == nums_sorted[i - 1] for i in range(1, len(nums_sorted)))


# Default alias for single-export usage (optional)
Solution = SetBased

# Explicit multi-export for test discovery
ALL_SOLUTIONS = [BruteForce, SetBased, Sorting]


# Canonical small test cases for default generic tests
# Each entry: (label, nums, expected)
TEST_CASES: list[tuple[str, list[int], bool]] = [
    ("dupe_simple", [1, 2, 3, 1], True),
    ("no_dupe", [1, 2, 3, 4], False),
    ("multi_dupes", [1, 1, 1, 3, 3, 4, 3, 2, 4, 2], True),
    ("empty", [], False),
    ("single", [5], False),
    ("zeros", [0, 0], True),
    ("negatives", [-1, -2, -1], True),
]


if __name__ == "__main__":
    # Convenience: running this file executes the generic spec filtered to this task.
    import subprocess
    import sys
    from pathlib import Path

    task_dir = Path(__file__).parent
    root = task_dir.parent
    task_name = task_dir.name
    # Run the single generic spec, filtered to this task's params
    subprocess.run(
        [sys.executable, "-m", "pytest", "-q", str(root), "-k", task_name],
        check=False,
    )
