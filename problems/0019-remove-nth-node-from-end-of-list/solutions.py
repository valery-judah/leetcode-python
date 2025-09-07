from __future__ import annotations

from common.types import ListNode


class Baseline:
    def solve(
        self,
        head: ListNode | None = None,
        n: int = 0,
    ) -> ListNode | None:
        raise NotImplementedError


class Optimized:
    def solve(
        self,
        head: ListNode | None = None,
        n: int = 0,
    ) -> ListNode | None:
        raise NotImplementedError


# Explicit multi-export for test discovery
ALL_SOLUTIONS = [Baseline, Optimized]

TEST_CASES = [
    ("types", (ListNode(1, ListNode(2)), 0), ListNode(1, ListNode(2))),
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
