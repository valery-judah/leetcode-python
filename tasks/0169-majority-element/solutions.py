
"""
Problem 169: Majority Element
https://leetcode.com/problems/majority-element/
Difficulty: easy
Tags: array,hash-table,divide-and-conquer,sorting,counting
"""

from __future__ import annotations

from typing import List


class Solution:
    def solve(self, nums: List[int]) -> int:
        return 1


# For consistency with multi-variant discovery
ALL_SOLUTIONS = [Solution]

# Canonical small test cases for generic stub tests
# Each entry: (label, args_tuple, kwargs_dict)
TEST_CASES = [
    ("example_1", [3, 2, 3], 3),
    ("example_2", [2, 2, 1, 1, 1, 2, 2], 1),
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
