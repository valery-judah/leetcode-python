from __future__ import annotations


class Baseline:
    def solve(
        self,
        starts: list[int] | None = None,
        ends: list[int] | None = None,
    ) -> list[bool]:
        raise NotImplementedError


class Optimized:
    def solve(
        self,
        starts: list[int] | None = None,
        ends: list[int] | None = None,
    ) -> list[bool]:
        raise NotImplementedError


# Explicit multi-export for test discovery
ALL_SOLUTIONS = [Baseline, Optimized]

TEST_CASES = [
    ("types", ([0], [0]), [False]),
    ("empty_list", ([], []), [False]),
]

# Opt-in for generic stub testing: assert .solve raises this exception.
TEST_EXPECT_EXCEPTION = NotImplementedError

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
