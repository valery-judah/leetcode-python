from __future__ import annotations


class Baseline:
    def solve(
        self,
        customers: list[int] | None = None,
        grumpy: list[int] | None = None,
        minutes: int = 0,
    ) -> int:
        raise NotImplementedError


class Optimized:
    def solve(
        self,
        customers: list[int] | None = None,
        grumpy: list[int] | None = None,
        minutes: int = 0,
    ) -> int:
        raise NotImplementedError


# Explicit multi-export for test discovery
ALL_SOLUTIONS = [Baseline, Optimized]

TEST_CASES = [
    ("types", ([0], [0], 0), 0),
    ("empty_list", ([], [], 0), 0),
]

# Opt-in for generic stub testing: assert .solve raises this exception.
TEST_EXPECT_EXCEPTION = NotImplementedError

# Optional: when all default tests pass, auto-mark this problem as optimal in stats.json
# Uncomment to enable once you are satisfied with your solution quality.
# TEST_MARK_OPTIMAL_ON_PASS = True

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
