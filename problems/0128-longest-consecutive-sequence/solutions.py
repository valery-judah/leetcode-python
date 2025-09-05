from __future__ import annotations

# Ensure repo root is on sys.path when running this file directly
import sys as _sys
from pathlib import Path as _Path

_root = str(_Path(__file__).resolve().parents[2])
if _root not in _sys.path:
    _sys.path.insert(0, _root)

# Common type stubs for annotations and simple local testing


class Baseline:
    def solve(self, nums: list[int]) -> int:
        """Replace with actual signature per problem."""
        raise NotImplementedError


# Optional default alias for single-export usage
Solution = Baseline

# Explicit multi-export for test discovery
ALL_SOLUTIONS = [Baseline]

# Canonical small test cases for generic stub tests
# Each entry: (label, args_tuple, kwargs_dict)
# TEST_CASES (typed placeholders for stub testing)
# Shape: (label: str, args_tuple: tuple, kwargs_dict: dict)
# While TEST_EXPECT_EXCEPTION is set, only label/args/kwargs are used; expected values are ignored.
# Signature preview: solve(self, nums: list[int])
# - nums: e.g., [0]
# To enable assertion-mode later: add expected to each case or switch to (label, *args, expected) shape.
# Includes basic empty-collection variant for list-typed parameters.
TEST_CASES = [
    ("types", ([0],), {}),
    ("empty_list", ([],), {}),
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
