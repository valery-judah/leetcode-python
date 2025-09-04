"""
Problem 169: Majority Element
https://leetcode.com/problems/majority-element/
Difficulty: easy
Tags: array,hash-table,divide-and-conquer,sorting,counting
"""

from typing import List


class Solution:
    def solve(self, nums: List[int]) -> int:
        candidate: int = 0
        margin: int = 0

        for n in nums:
            if margin == 0:
                candidate = n

            margin = margin + 1 if n == candidate else margin - 1

        return candidate


# For consistency with multi-variant discovery
ALL_SOLUTIONS = [Solution]

# Canonical small test cases for generic stub tests
# Each entry: (label, args_tuple, kwargs_dict)
TEST_CASES = [
    ("example_1", [3, 2, 3], 3),
    ("example_2", [2, 2, 1, 1, 1, 2, 2], 2),
]

if __name__ == "__main__":
    # Convenience: running this file executes the generic spec filtered to this problem.
    import subprocess
    import sys
    from pathlib import Path

    problem_dir = Path(__file__).parent
    root = problem_dir.parent
    problem_name = problem_dir.name
    # Run the single generic spec, filtered to this problem's params
    subprocess.run(
        [sys.executable, "-m", "pytest", "-q", str(root), "-k", problem_name],
        check=False,
    )
