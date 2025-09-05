from collections import Counter


class Baseline:
    def solve(self, s: str = "", t: str = "") -> bool:
        if len(s) != len(t):
            return False
        
        s_counter = Counter(s)
        t_counter = Counter(t)
        
        return s_counter == t_counter


# Optional default alias for single-export usage
Solution = Baseline

# Explicit multi-export for test discovery
ALL_SOLUTIONS = [Baseline]

# Canonical small test cases for generic stub tests
# Each entry: (label, args_tuple, expected_output)
TEST_CASES = [
    ("simple positive", ("a", "a"), True),
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
        [sys.executable, "-m", "pytest", "-q", str(root), "-k", problem_name],
        check=False,
    )
