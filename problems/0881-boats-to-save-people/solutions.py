from __future__ import annotations

import copy

import pytest


class Straight:
    def solve(self, people: list[int], limit: int) -> int:
        people.sort()
        boats = 0
        left, right = 0, len(people) - 1
        while left <= right:
            if people[left] + people[right] <= limit:
                left += 1
                right -= 1
            else:
                right -= 1
            boats += 1
        return boats


class Optimized:
    def solve(self, people: list[int], limit: int) -> int:
        people.sort()
        res, left, right = 0, 0, len(people) - 1
        while left <= right:
            remain = limit - people[right]
            right -= 1
            res += 1
            if left <= right and remain >= people[left]:
                left += 1
        return res


# Explicit multi-export for test discovery
ALL_SOLUTIONS = [Straight, Optimized]

TEST_CASES = [
    ("example_1", ([1, 2], 3), 1),
    ("example_2", ([3, 2, 2, 1], 3), 3),
    ("example_3", ([3, 5, 3, 4], 5), 4),
    ("all_fit_in_pairs", ([1, 1, 1, 1], 2), 2),
    ("no_pairs_fit", ([3, 3, 3, 3], 4), 4),
    ("heaviest_is_limit", ([5, 1, 4], 5), 2),
    ("all_same_weight_pairs", ([2, 2, 2, 2], 5), 2),
    ("all_same_weight_no_pairs", ([3, 3, 3, 3], 5), 4),
    ("single_person", ([1], 1), 1),
    ("large_limit", ([1, 2, 3, 4, 5], 100), 3),
    ("all_equal_to_limit", ([5, 5, 5, 5], 5), 4),
    ("mixed_weights", ([2, 4, 1, 3], 5), 2),
    ("long_list", ([1] * 10, 2), 5),
    ("complex_case", ([3, 2, 3, 2, 2], 6), 3),
    ("empty_list", ([], 0), 0),
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
