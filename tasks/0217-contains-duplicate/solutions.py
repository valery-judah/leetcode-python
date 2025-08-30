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


if __name__ == "__main__":
    # Convenience: running this file executes tests for its task folder.
    import subprocess
    import sys
    from pathlib import Path

    task_dir = Path(__file__).parent
    subprocess.run([sys.executable, "-m", "pytest", "-q", str(task_dir)], check=False)
