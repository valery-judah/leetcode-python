from __future__ import annotations

import copy

import pytest


class Baseline:
    def solve(self, weights: list[int], days: int) -> int:
        def is_feasible(capacity: int) -> bool:
            needed_days = 1
            current_load = 0

            for weight in weights:
                if weight > capacity:
                    return False

                if current_load + weight > capacity:
                    needed_days += 1
                    current_load = 0
                    if needed_days > days:
                        return False

                current_load += weight

            return True

        lo = max(weights)
        hi = sum(weights)

        while lo < hi:
            mid = (lo + hi) // 2
            if is_feasible(mid):
                hi = mid
            else:
                lo = mid + 1

        return lo


class Optimized:
    def solve(self, weights: list[int], days: int) -> int: ...


# Explicit multi-export for test discovery
ALL_SOLUTIONS = [Baseline, Optimized]

TEST_CASES = [
    ("example1", ([2, 4, 6, 1, 3, 10], 4), 10),
    ("example2", ([1, 2, 3, 4, 5], 5), 5),
    ("example3", ([1, 5, 4, 4, 2, 3], 3), 8),
    ("single_day", ([1, 2, 3, 4, 5], 1), 15),
    ("more_days_than_weights", ([1, 2, 3], 4), 3),
    ("all_weights_same", ([5, 5, 5, 5], 2), 10),
    ("single_heavy_package", ([10, 1, 1, 1, 1], 2), 10),
    ("minimum_capacity", ([1, 1, 1, 1, 1], 2), 3),
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
