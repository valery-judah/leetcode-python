from __future__ import annotations

# Common type stubs for annotations and simple local testing


class Baseline:
    def solve(self, ghosts: list[list[int]], target: list[int]) -> bool:
        """Check with actual signature per problem."""
        raise NotImplementedError


# Optional default alias for single-export usage
Solution = Baseline

# Explicit multi-export for test discovery
ALL_SOLUTIONS = [Baseline]

# Signature preview: solve(self, ghosts: list[list[int]], target: list[int])
# - ghosts: e.g., [[0]]
# - target: e.g., [0]
# Includes basic empty-collection variant for list-typed parameters.
TEST_CASES = [
    ("types", ([[0]], [0]), {}),
    ("empty_list", ([], []), {}),
]

# Opt-in for generic stub testing: assert .solve raises this exception.
TEST_EXPECT_EXCEPTION = NotImplementedError


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
