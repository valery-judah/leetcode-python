from __future__ import annotations


class Baseline:
    def solve(self, *args, **kwargs):
        """Replace with actual signature per problem."""
        raise NotImplementedError


# Optional default alias for single-export usage
Solution = Baseline

# Explicit multi-export for test discovery
ALL_SOLUTIONS = [Baseline]


if __name__ == "__main__":
    # Convenience: running this file executes tests for its task folder.
    import sys
    import subprocess
    from pathlib import Path

    task_dir = Path(__file__).parent
    subprocess.run([sys.executable, "-m", "pytest", "-q", str(task_dir)], check=False)
