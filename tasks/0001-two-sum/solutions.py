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


ALL_SOLUTIONS = [Solution]


if __name__ == "__main__":
    # Convenience: running this file executes tests for its task folder.
    import subprocess
    import sys
    from pathlib import Path

    task_dir = Path(__file__).parent
    subprocess.run([sys.executable, "-m", "pytest", "-q", str(task_dir)], check=False)
