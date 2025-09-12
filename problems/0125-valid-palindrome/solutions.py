from __future__ import annotations

import re


def clean_string(s):
    s = s.lower()
    s = re.sub(r"[^a-z0-9]", "", s)
    return s


class Baseline:
    def solve(self, s: str = "") -> bool:
        cleaned = clean_string(s)
        if len(cleaned) <= 1:
            return True
        left, right = 0, len(cleaned) - 1
        while left < right:
            if cleaned[left] != cleaned[right]:
                return False
            # else we just going to center while checking validity
            left += 1
            right -= 1
        return True


class Optimized:
    def solve(self, s: str = "") -> bool:
        left, right = 0, len(s) - 1
        while left < right:
            # Move the left pointer forward until it finds an alphanumeric character
            while left < right and not s[left].isalnum():
                # important to have left < right to avoid overstepping
                left += 1

            # Move the right pointer backward until it finds an alphanumeric character
            while left < right and not s[right].isalnum():
                right -= 1

            # Compare the two alphanumeric characters (case-insensitive)
            if s[left].lower() != s[right].lower():
                return False

            # Move pointers inward for the next comparison
            left += 1
            right -= 1
        return True


# Explicit multi-export for test discovery
ALL_SOLUTIONS = [Baseline, Optimized]

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
