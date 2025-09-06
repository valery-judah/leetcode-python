from __future__ import annotations


class Baseline:
    def solve(self, nums: list[int]) -> bool:
        for i, n in enumerate(nums):
            # search equal number in nums[i + 1 : ]
            for s in nums[i + 1 :]:
                if s == n:
                    return True
        return False


class HashMapOptimized:
    def solve(self, nums: list[int]) -> bool:
        hist = {}
        for n in nums:
            if n in hist:
                return True
            else:
                hist[n] = 1
        return False  # so we didn't seen any duplicate so far -> return False


# Explicit multi-export for test discovery
ALL_SOLUTIONS = [Baseline, HashMapOptimized]


TEST_CASES = [
    ("types", ([1, 2, 0],), False),
    ("simple_duplicate", ([1, 1]), True),
    ("singe_element", ([1]), False),
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
