from __future__ import annotations


class Baseline:
    def solve(self, nums: list[int] | None = None, target: int = 0) -> list[int]:
        for i in range(len(nums or [])):
            for j in range(i + 1, len(nums)): # it's already optimized to not repeat pairs
                # because we already checked the pairs (k, i) for k < i
                if (nums or [])[i] + (nums)[j] == target:
                    return [i, j]


class Optimized:
    def solve(self, nums: list[int] | None = None, target: int = 0) -> list[int]:
        return 0


# Explicit multi-export for test discovery
ALL_SOLUTIONS = [Baseline, Optimized]

TEST_CASES = [
    ("types", ([0], 0), [0]),
    ("empty_list", ([], 0), [0]),
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
