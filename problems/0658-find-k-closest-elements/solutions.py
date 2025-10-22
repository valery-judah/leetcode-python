from __future__ import annotations

import copy

import pytest


class Baseline:
    def solve(self, arr: list[int], k: int, x: int) -> list[int]:
        # Sort the array based on distance from x. If distances are equal,
        # sort by the element's value.
        sorted_arr = sorted(arr, key=lambda num: (abs(num - x), num))

        # Take the first k elements from the sorted list.
        result = sorted_arr[:k]

        # The final result needs to be sorted in ascending order.
        return sorted(result)


class Optimized:
    def solve(self, arr: list[int], k: int, x: int) -> list[int]: ...


# Explicit multi-export for test discovery
ALL_SOLUTIONS = [Baseline, Optimized]

TEST_CASES = [
    ("example1", ([1, 2, 3, 4, 5], 4, 3), [1, 2, 3, 4]),
    ("example2", ([1, 2, 3, 4, 5], 4, -1), [1, 2, 3, 4]),
    ("x_smaller_than_all", ([10, 20, 30], 2, 0), [10, 20]),
    ("x_larger_than_all", ([10, 20, 30], 2, 40), [20, 30]),
    ("tie_breaking", ([1, 1, 1, 10, 10, 10], 3, 9), [10, 10, 10]),
    ("tie_breaking_prefer_smaller", ([1, 2, 4, 5], 2, 3), [2, 4]),
    ("k_equals_len", ([1, 2, 3, 4, 5], 5, 0), [1, 2, 3, 4, 5]),
    ("k_is_zero", ([1, 2, 3, 4, 5], 0, 3), []),
    ("empty_arr", ([], 5, 10), []),
    ("negative_numbers", ([-2, -1, 0, 1, 2], 3, 0), [-1, 0, 1]),
    ("x_is_in_array", ([1, 5, 10], 2, 5), [1, 5]),
    ("x_not_in_array", ([1, 5, 10], 2, 4), [1, 5]),
    ("from_leetcode_1", ([0, 0, 1, 2, 3, 3, 4, 7, 7, 8], 3, 5), [3, 3, 4]),
    ("from_leetcode_2", ([1, 2, 5, 10], 2, 4), [2, 5]),
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
