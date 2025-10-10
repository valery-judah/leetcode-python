from __future__ import annotations

{import_types}
import pytest


class Baseline:
    {solve_signature}
        ...


class Optimized:
    {solve_signature}
        ...


# Explicit multi-export for test discovery
ALL_SOLUTIONS = [Baseline, Optimized]

{generated_cases}


# Optional: when all default tests pass, auto-mark this problem as optimal in stats.json
# Uncomment to enable once you are satisfied with your solution quality.
# TEST_MARK_OPTIMAL_ON_PASS = True

if __name__ == "__main__":
    pytest.main([__file__])
