from __future__ import annotations


class Baseline:
    def solve(self, *args, **kwargs):
        """Replace with actual signature per problem."""
        raise NotImplementedError


# Optional default alias for single-export usage
Solution = Baseline

# Explicit multi-export for test discovery
ALL_SOLUTIONS = [Baseline]

