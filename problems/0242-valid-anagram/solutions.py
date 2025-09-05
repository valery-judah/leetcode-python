from collections import Counter


class Baseline:
    def solve(self, s: str = "", t: str = "") -> bool:
        return self._count(s) == self._count(t)

    def _count(self, s):
        counts = {}
        for ch in s:
            counts[ch] = counts.get(ch, 0) + 1
        return counts


class LibraryUse:
    def solve(self, s: str = "", t: str = "") -> bool:
        return Counter(s) == Counter(t)


# Explicit multi-export for test discovery
ALL_SOLUTIONS = [Baseline, LibraryUse]
SOLUTIONS = ALL_SOLUTIONS

__all__ = [
    "Baseline",
    "LibraryUse",
    "ALL_SOLUTIONS",
    "SOLUTIONS",
    "TEST_CASES",
    "TEST_EXPECT_EXCEPTION",
]

# Canonical small test cases for generic stub tests
# Each entry: (label, args_tuple, expected_output)
TEST_CASES = [
    ("simple positive", ("catt", "tact"), True),
    ("simple negative", ("a", "b"), False),
    ("positive", ("anagram", "nagaram"), True),
    ("negative", ("rat", "car"), False),
    ("negative different length", ("rat", "cart"), False),
    ("empty", ("", ""), True),
]

# Opt-in for generic stub testing: assert .solve raises this exception.
TEST_EXPECT_EXCEPTION = None


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
        [sys.executable, "-m", "pytest", "-q", "-s", str(root), "-k", problem_name],
        check=False,
    )
