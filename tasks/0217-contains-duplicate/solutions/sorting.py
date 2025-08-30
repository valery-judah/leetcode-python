from __future__ import annotations


class Solution:
    def solve(self, nums: list[int]) -> bool:
        if len(nums) < 2:
            return False
        nums_sorted = sorted(nums)
        for i in range(1, len(nums_sorted)):
            if nums_sorted[i] == nums_sorted[i - 1]:
                return True
        return False

