from __future__ import annotations

import copy

import pytest


class Baseline:
    def solve(self, height: list[int] | None = None) -> int:
        if not height:
            return 0
        max_area = 0
        for left, hl in enumerate(height):
            for right, hr in enumerate(height[left + 1 :], start=left + 1):
                area = (right - left) * min(hl, hr)
                max_area = max(max_area, area)
        return max_area


class Optimized:
    def solve(self, height: list[int] | None = None) -> int:
        if not height:
            return 0
        left, right = 0, len(height) - 1
        max_area = 0
        while left < right:
            area = (right - left) * min(height[left], height[right])
            max_area = max(max_area, area)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return max_area


# Explicit multi-export for test discovery
ALL_SOLUTIONS = [Baseline, Optimized]

TEST_CASES = [
    ("empty container", ([0, 0],), 0),
    ("example 1", ([1, 8, 6, 2, 5, 4, 8, 3, 7],), 49),
    ("example 2", ([1, 1],), 1),
    ("single element", ([1],), 0),
    ("two elements", ([1, 2],), 1),
    ("three elements", ([1, 2, 3],), 2),
    ("four elements", ([1, 2, 3, 4],), 4),
    ("five elements", ([1, 2, 3, 4, 5],), 6),
    ("six elements", ([1, 2, 3, 4, 5, 6],), 9),
    ("large values", ([10000, 10000],), 10000),
    ("large list", (list(range(1, 1001)),), 250000),
    ("descending heights", (list(range(1000, 0, -1)),), 250000),
    ("zigzag heights", ([1, 1000] * 500,), 998000),
    ("plateau heights", ([500] * 1000,), 499500),
    ("mixed heights", ([1, 3, 2, 5, 25, 24, 5],), 24),
    ("another mixed heights", ([3, 9, 3, 4, 7, 2, 12],), 45),
    ("all same heights", ([7] * 10,), 63),
    ("two high peaks", ([1] * 100 + [1000] + [1] * 100 + [1000] + [1] * 100,), 101000),
    ("increasing then decreasing", (list(range(1, 501)) + list(range(500, 0, -1)),), 125250),
    ("decreasing then increasing", (list(range(500, 0, -1)) + list(range(1, 501)),), 499500),
    ("single peak", (list(range(1, 501)) + list(range(499, 0, -1)),), 125000),
    ("empty_list", ([],), 0),
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
