"""
Problem {number}: {title}
{url}
Difficulty: {difficulty}
Tags: {tags}
"""

from __future__ import annotations


class Baseline:
    def solve(self, *args, **kwargs):
        """Replace with actual signature per problem."""
        raise NotImplementedError


# Optional default alias for single-export usage
Solution = Baseline

# Explicit multi-export for test discovery
ALL_SOLUTIONS = [Baseline]

# Canonical small test cases for generic stub tests
# Each entry: (label, args_tuple, kwargs_dict)
TEST_CASES = [
    ("example", (), {{}}),  # replace with concrete inputs
]

# Opt-in for generic stub testing: assert .solve raises this exception.
TEST_EXPECT_EXCEPTION = NotImplementedError


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
