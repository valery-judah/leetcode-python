from __future__ import annotations


class Baseline:
    def solve(self, nums: list[int], target: int = 0) -> list[int] | None:
        for i in range(len(nums or [])):
            for j in range(i + 1, len(nums)):
                # it's already optimized to not repeat pairs
                # because we already checked the pairs (k, i) for k < i
                if (nums)[i] + (nums)[j] == target:
                    return [i, j]
        return None


class Optimized:
    def solve(self, nums: list[int], target: int = 0) -> list[int] | None:
        targets = {}
        for i, n in enumerate(nums):
            if n in targets:
                return [i, targets[n]]
            else:
                targets[target - n] = i


# Explicit multi-export for test discovery
ALL_SOLUTIONS = [Baseline]

TEST_CASES = [
    # Happy path
    ("basic_case", ([2, 7, 11, 15], 9), [0, 1]),
    # Boundary cases
    ("solution_at_start", ([3, 5, -4, 8], 8), [0, 1]),
    ("solution_at_end", ([8, -4, 5, 3], 8), [2, 3]),
    # Problem-specific cases
    ("negative_numbers", ([-1, -3, 5, 90], 4), [0, 2]),
    ("zero_involvement", ([5, 0, -2, 4], 2), [2, 3]),
    ("duplicate_numbers_as_solution", ([6, 5, 3, 3], 6), [2, 3]),
]

if __name__ == "__main__":
    import subprocess
    from pathlib import Path

    problem_dir = Path(__file__).parent
    problem_name = problem_dir.name
    spec_path = problem_dir.parent / "all_problems_spec.py"

    subprocess.run(
        ["pytest", "-q", str(spec_path), "-k", problem_name],
        check=False,
    )
