from __future__ import annotations


class Baseline:
    def solve(self, s: str = "", t: str = "") -> bool:
        if len(s) != len(t):
            return False
        return sorted(s) == sorted(t)


class Optimized:
    def solve(self, s: str = "", t: str = "") -> bool:
        if len(s) != len(t):
            return False

        count = [0] * 26
        char_to_index = lambda c: ord(c) - ord("a")

        for char in s:
            index = char_to_index(char)
            count[index] = count[index] + 1
            print(f"count after adding {char}: {count}")

        for char in t:
            index = char_to_index(char)
            print(f"count before deciding {char}: {count}")
            # specify decision logic for the step
            # first check if the count is already zero then we have an extra char in t
            if count[index] == 0:
                return False
            count[index] = count[index] - 1
            print(f"count after removing {char}: {count}")
            #
        return True


# Explicit multi-export for test discovery
ALL_SOLUTIONS = [Baseline, Optimized]

TEST_CASES = [
    ("usual case", ("anagram", "ramanag"), True),
    ("different lengths", ("nagram", "graamna"), False),
    ("different words", ("cat", "tar"), False),
    ("empty strings", ("", ""), True),
]

# Optional: when all default tests pass, auto-mark this problem as optimal in stats.json
# Uncomment to enable once you are satisfied with your solution quality.
# TEST_MARK_OPTIMAL_ON_PASS = True

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
