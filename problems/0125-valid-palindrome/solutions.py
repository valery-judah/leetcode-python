from __future__ import annotations

import re


def clean_string(s):
    s = s.lower()
    s = re.sub(r"[^a-z0-9]", "", s)
    return s


class Baseline:
    def solve(self, s: str = "") -> bool:
        if s is None or len(s) == 1:
            return True

        s = s.lower()

        left, right = 0, len(s) - 1

        while left < right:

            while not s[left].isalnum() and left < right:
                left += 1
            while not s[right].isalnum() and left < right:
                right -= 1

            if left >= right:
                break

            if s[left] != s[right]:
                return False

            left += 1
            right -= 1

        # all symbols are verified
        return True


class Optimized:
    def solve(self, s: str = "") -> bool: ...


# Explicit multi-export for test discovery
ALL_SOLUTIONS = [Baseline]

TEST_CASES = [
    # Category: Standard Palindromes (Basic functionality)
    ("standard_palindrome_odd", ("racecar",), True),
    ("standard_palindrome_even", ("noon",), True),
    ("standard_mixed_case", ("LeVEl",), True),
    ("standard_with_punctuation_and_spaces", ("A man, a plan, a canal: Panama",), True),
    ("standard_with_numbers", ("1a2b3b2a1",), True),
    # Category: Standard Non-Palindromes
    ("standard_non_palindrome", ("hello",), False),
    ("subtle_non_palindrome", ("race a car",), False),
    ("almost_palindrome", ("abac",), False),
    # Category: Edge Cases (Testing logical boundaries)
    ("edge_empty_string", ("",), True),  # Sanitizes to "", a valid palindrome.
    ("edge_single_alphanumeric_char", ("a",), True),
    ("edge_single_char_with_noise", ("-b-",), True),  # Sanitizes to "b".
    ("edge_all_non_alphanumeric", (",.!@#$%",), True),  # Sanitizes to "".
    ("edge_all_same_chars", ("AAAAA",), True),
    # Category: Pointer Challenges (Specifically for the in-place algorithm)
    ("pointer_symmetric_noise", (".,a,b,a,.",), True),
    ("pointer_asymmetric_noise_fail", ("a,b,c,a",), False),
    ("pointer_noise_at_ends", ("-madam-",), True),
    ("pointer_noise_in_middle", ("abc...cba",), True),
    # Category: Alphanumeric and Numeric Variations
    ("numeric_palindrome", ("12321",), True),
    ("numeric_non_palindrome", ("12345",), False),
    ("alphanumeric_mix_palindrome", ("A1b22b1A",), True),
    ("alphanumeric_mix_fail", ("0P",), False),  # Sanitizes to "0p".
    # Category: Whitespace Variations
    ("whitespace_palindrome", ("taco cat",), True),
    ("whitespace_only", ("  ",), True),  # Sanitizes to "".
    ("punctuation only", (".,",), True),  # Sanitizes to "".
    ("leading_trailing_whitespace", ("  a b a  ",), True),
    # Category: Long Run
    ("long_run_in_middle", ("ab,,,,,,,,,,,,,,,,cd",), False),
    ("long_run_palindrome", ("a,,,,,,,,,,,,,,,,a",), True),
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
