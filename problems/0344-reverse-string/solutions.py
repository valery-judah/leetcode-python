from __future__ import annotations

import copy

import pytest


class Baseline:
    def solve(self, s: list[str]) -> None: 
        if len(s) < 2:
            return None
        left, right = 0, len(s) - 1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1


class Optimized:
    def solve(self, s: list[str]) -> None: ...


# Explicit multi-export for test discovery
ALL_SOLUTIONS = [Baseline, Optimized]

TEST_CASES = [
    ("egde_single", (["a"],), None),
    ("happy_path", (["a", "b", "c", "d"],), None),
]


@pytest.mark.parametrize(
    ("_", "args", "expected"),
    TEST_CASES,
)
def test_solutions(_, args, expected):
    for solution_class in ALL_SOLUTIONS:
        solution = solution_class()
        # Prevent test pollution by deep-copying mutable arguments
        args_copy = copy.deepcopy(args)
        actual = solution.solve(*args_copy)
        assert actual == expected


if __name__ == "__main__":
    pytest.main([__file__])
