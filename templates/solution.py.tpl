
"""
Problem {number}: {title}
{url}
Difficulty: {difficulty}
Tags: {tags}
"""

from __future__ import annotations


class Solution:
    def solve(self, *args, **kwargs):
        """Replace with actual signature per problem."""
        raise NotImplementedError


# For consistency with multi-variant discovery
ALL_SOLUTIONS = [Solution]


if __name__ == "__main__":
    # Convenience: running this file executes tests for its task folder.
    import sys
    import subprocess
    from pathlib import Path

    task_dir = Path(__file__).parent
    subprocess.run([sys.executable, "-m", "pytest", "-q", str(task_dir)], check=False)
