from __future__ import annotations

from typing import List


class Solution:
    def solve(self, nums: List[int]) -> bool:
        for i, v in enumerate(nums):
            for j in range(i + 1, len(nums)):
                if v == nums[j]:
                    return True
        return False

