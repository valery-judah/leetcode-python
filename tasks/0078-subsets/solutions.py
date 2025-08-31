"""
Problem 78: Subsets
https://leetcode.com/problems/subsets/
Difficulty: medium
Tags:
"""

from __future__ import annotations


class Backtracking:
    def solve(self, nums: list[int]) -> list[list[int]]:
        """Generate all subsets via depth-first backtracking."""
        res: list[list[int]] = []

        def backtrack(start: int, path: list[int]) -> None:
            res.append(path.copy())
            for i in range(start, len(nums)):
                path.append(nums[i])
                backtrack(i + 1, path)
                path.pop()

        backtrack(0, [])
        return res


class Iterative:
    def solve(self, nums: list[int]) -> list[list[int]]:
        """Iteratively expand the power set by adding each element."""
        res: list[list[int]] = [[]]
        for x in nums:
            res += [subset + [x] for subset in res]
        return res


class Bitmask:
    def solve(self, nums: list[int]) -> list[list[int]]:
        """Enumerate subsets using bit masks from 0..(2^n-1)."""
        n = len(nums)
        res: list[list[int]] = []
        for mask in range(1 << n):
            curr: list[int] = []
            for i in range(n):
                if (mask >> i) & 1:
                    curr.append(nums[i])
            res.append(curr)
        return res


# Default alias for single-solution loaders
Solution = Backtracking

# Explicit multi-variant export for discovery tests
ALL_SOLUTIONS = [Backtracking, Iterative, Bitmask]


# Optional: declare canonical small test cases here for reuse by tests
# Each item: (label, nums, expected_subsets)
TEST_CASES: list[tuple[str, list[int], list[list[int]]]] = [
    (
        "example_1",
        [1, 2, 3],
        [
            [],
            [1],
            [2],
            [3],
            [1, 2],
            [1, 3],
            [2, 3],
            [1, 2, 3],
        ],
    ),
    ("empty", [], [[]]),
    ("single", [0], [[], [0]]),
    ("two", [1, 2], [[], [1], [2], [1, 2]]),
    (
        "unsorted",
        [3, 1, 2],
        [
            [],
            [1],
            [2],
            [3],
            [1, 2],
            [1, 3],
            [2, 3],
            [1, 2, 3],
        ],
    ),
    (
        "negatives",
        [-1, 0, 1],
        [
            [],
            [-1],
            [0],
            [1],
            [-1, 0],
            [-1, 1],
            [0, 1],
            [-1, 0, 1],
        ],
    ),
]

# Property-based count/uniqueness cases have been moved to common.testutil


if __name__ == "__main__":
    # Convenience: running this file executes tests for its task folder.
    import subprocess
    import sys
    from pathlib import Path

    task_dir = Path(__file__).parent
    subprocess.run([sys.executable, "-m", "pytest", "-q", str(task_dir)], check=False)
