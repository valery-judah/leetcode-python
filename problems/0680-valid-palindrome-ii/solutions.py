from __future__ import annotations


class Baseline:
    def solve(self, s: str = "") -> bool:
        def is_palindrome(left, right, s: str) -> bool:
            while left < right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1
            return True

        if len(s) < 2:
            return True
        left, right = 0, len(s) - 1
        while left < right:
            if s[left] != s[right]:
                return is_palindrome(left + 1, right, s) or is_palindrome(left, right - 1, s)
            left += 1
            right -= 1
        # all symbols checked
        return True


class Optimized:
    def solve(self, s: str = "") -> bool: ...


# Explicit multi-export for test discovery
ALL_SOLUTIONS = [Baseline]

TEST_CASES = [
    ("types", ("ab",), True),
    ("two", ("babc",), True),
    ("fls", ("babcd",), False),
    ("strong", ("aba",), True),
]


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
