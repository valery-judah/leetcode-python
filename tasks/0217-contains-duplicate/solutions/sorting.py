from __future__ import annotations

from typing import List


class Solution:
    def solve(self, nums: List[int]) -> bool:
        if len(nums) < 2:
            return False
        nums_sorted = sorted(nums)
        for i in range(1, len(nums_sorted)):
            if nums_sorted[i] == nums_sorted[i - 1]:
                return True
        return False

