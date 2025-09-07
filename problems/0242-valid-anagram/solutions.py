from __future__ import annotations

from typing import List


class Baseline:
    def solve(self, s: str = "", t: str = "") -> bool:
        if len(s) != len(t):
            return False
        return _count(s) == _count(t)


@staticmethod
def _count(s):
    counts = {}
    for ch in s:
        counts[ch] = counts.get(ch, 0) + 1
    return counts


# why brute force - it's because we don't need all the information about relative ordering of elements
# we're doing redundant job
class BrutForce:
    def solve(self, s: str = "", t: str = "") -> bool:
        if len(s) != len(t):
            return False
        return sorted(s) == sorted(t)


class DiffCounter:
    def solve(self, s: str = "", t: str = "") -> bool:
        if len(s) != len(t):
            return False

        counts = [0] * 26
        ord_a = ord("a")

        for char in s:
            counts[ord(char) - ord_a] += 1

        for char in t:
            counts[ord(char) - ord_a] -= 1
            # Optimization: If a count goes below zero, they can't be anagrams.
            if counts[ord(char) - ord_a] < 0:
                return False
        print(counts)
        # If all counts are zero, the final array will be all zeros.
        # This check is implicitly handled by the loop. If we finish, it's True.
        return True


class ArrayBased:
    def solve(self, s: str = "", t: str = "") -> bool:
        if len(s) != len(t):
            return False
        return _frequencies(s) == _frequencies(t)


# we're using 'lowercase English Letters' constraint
def _frequencies(s: str) -> List[int]:
    freqs = [0] * 26

    def convert_into_int(char):
        return ord(char) - ord("a")

    for letter in s:
        letter_index = convert_into_int(letter)
        freqs[letter_index] = freqs[letter_index] + 1
    return freqs


# Explicit multi-export for test discovery
ALL_SOLUTIONS = [Baseline, DiffCounter, BrutForce, ArrayBased]


TEST_CASES = [
    ("empty", ("", ""), True),
    ("simple positive", ("catt", "tact"), True),
    ("simple negative", ("a", "b"), False),
    ("simple negative", ("aa", "ab"), False),
    ("positive", ("anagram", "nagaram"), True),
    ("negative", ("rat", "car"), False),
    ("negative different length", ("rat", "cart"), False),
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
