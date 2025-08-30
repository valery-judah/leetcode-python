from __future__ import annotations


class Solution:
    def solve(self, nums: list[int]) -> bool:
        nums_sorted = sorted(nums)
        return any(nums_sorted[i] == nums_sorted[i - 1] for i in range(1, len(nums_sorted)))
