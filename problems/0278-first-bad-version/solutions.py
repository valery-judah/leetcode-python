from __future__ import annotations

import pytest

# The isBadVersion API is defined for you.
# def isBadVersion(version: int) -> bool:
#     ...


class Baseline:
    def isBadVersion(self, version: int) -> bool:
        """Placeholder for the API provided by LeetCode."""
        raise NotImplementedError("This method should be mocked in tests.")

    def solve(self, n: int) -> int:
        """
        A straightforward binary search implementation.
        It searches for the first version that is bad.
        """
        left, right = 1, n
        while left < right:
            mid = left + (right - left) // 2
            if self.isBadVersion(mid):
                right = mid
            else:
                left = mid + 1
        return left


class Optimized:
    def isBadVersion(self, version: int) -> bool:
        """Placeholder for the API provided by LeetCode."""
        raise NotImplementedError("This method should be mocked in tests.")

    def solve(self, n: int) -> int:
        """
        This problem's optimal solution is already a binary search,
        so this implementation is identical to the baseline.
        """
        left, right = 1, n
        while left < right:
            mid = left + (right - left) // 2
            if self.isBadVersion(mid):
                right = mid
            else:
                left = mid + 1
        return left


# Explicit multi-export for test discovery
ALL_SOLUTIONS = [Baseline, Optimized]

# Test cases are defined as (n, bad_version)
TEST_CASES = [
    (5, 4),
    (1, 1),
    (2, 1),
    (2, 2),
    (10, 7),
    (2126753390, 1702766719),  # Large numbers
]


@pytest.mark.parametrize(
    ("n", "bad"),
    TEST_CASES,
)
def test_solutions(n, bad, monkeypatch):
    """
    Tests all solutions against the defined test cases.
    It uses monkeypatch to inject a mock `isBadVersion` API
    into each solution instance for isolated testing.
    """

    def mock_is_bad_version(version: int) -> bool:
        return version >= bad

    for solution_class in ALL_SOLUTIONS:
        solution = solution_class()
        monkeypatch.setattr(solution, "isBadVersion", mock_is_bad_version)
        actual = solution.solve(n)
        assert actual == bad


if __name__ == "__main__":
    pytest.main([__file__])
