from __future__ import annotations


class Baseline:
    def solve(self, nums: list[int] | None = None) -> int:
        return 1


class Optimized:
    def solve(self, nums: list[int] | None = None) -> int:
        return 0


# Explicit multi-export for test discovery
ALL_SOLUTIONS = [Baseline, Optimized]

TEST_CASES = [
    ("non-empty", ([100, 3, 10, 2, 4],), 0),
    ("empty_list", ([],), 0),
    ("single-element", ([2],), 1),
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
