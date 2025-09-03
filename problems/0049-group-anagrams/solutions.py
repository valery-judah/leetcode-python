"""
Problem 49: Group Anagrams
https://leetcode.com/problems/group-anagrams/
Difficulty: medium
Tags: array,hash-map
"""

from __future__ import annotations

from collections import defaultdict
from typing import Any, Callable


def _normalize_output(value: Any) -> Any:
    """Sorts list[list[Any]] for order-insensitive comparison."""
    if isinstance(value, list) and value and all(isinstance(x, list) for x in value):
        normalized_inner = [sorted(x) for x in value]
        try:
            return sorted(normalized_inner)
        except Exception:
            return sorted(normalized_inner, key=lambda x: str(x))
    return value


# Canonical small test cases for default generic tests
# Each entry: (label, strs, expected_groups)
TEST_CASES: list[tuple[str, list[str], list[list[str]]]] = [
    (
        "example",
        ["eat", "tea", "tan", "ate", "nat", "bat"],
        [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]],
    ),
    ("single", ["a"], [["a"]]),
    ("dupe_word", ["aa", "aa"], [["aa", "aa"]]),
    ("empties", ["", ""], [["", ""]]),
    (
        "mixed_lengths",
        ["ab", "ba", "abc", "bca", "cab", "zzz"],
        [["ab", "ba"], ["abc", "bca", "cab"], ["zzz"]],
    ),
    ("no_anagrams", ["abc", "def", "ghi"], [["abc"], ["def"], ["ghi"]]),
    ("empty_input", [], []),
]


def test(func: Callable[[list[str]], list[list[str]]]) -> None:
    """Decorator that runs the decorated function against all TEST_CASES."""
    print(f"\n--- Running tests for: {func.__name__} ---")
    for label, case_args, expected in TEST_CASES:
        actual = func(case_args)
        actual_norm = _normalize_output(actual)
        expected_norm = _normalize_output(expected)
        try:
            assert actual_norm == expected_norm
            print(f"  [PASS] {label}")
        except AssertionError:
            print(f"  [FAIL] {label}")
            print(f"    Expected: {expected_norm}")
            print(f"    Actual:   {actual_norm}")


@test
def solve_by_sort(strs: list[str]) -> list[list[str]]:
    """Group anagrams by sorting letters (O(n * k log k))."""
    groups: dict[tuple[str, ...], list[str]] = defaultdict(list)
    for s in strs:
        key = tuple(sorted(s))  # order-insensitive signature
        groups[key].append(s)
    return list(groups.values())


@test
def solve_by_count(strs: list[str]) -> list[list[str]]:
    """Group anagrams by 26-count signature (O(n * (k + A))).

    A is alphabet size (26 for lowercase). Avoids per-string sort.
    """
    groups: dict[tuple[int, tuple], list[str]] = defaultdict(list)
    for s in strs:
        counts: list[int] | None = [0] * 26
        for ch in s:
            idx = ord(ch) - 97  # assumes 'a'..'z'
            if 0 <= idx < 26:
                assert counts is not None
                counts[idx] += 1
            else:
                counts = None
                break
        if counts is None:
            key = (1, tuple(sorted(s)))
            groups[key].append(s)
        else:
            key = (0, tuple(counts))
            groups[key].append(s)
    return list(groups.values())
