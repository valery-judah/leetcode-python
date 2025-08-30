from __future__ import annotations


class Solution:
    def solve(self, nums: list[int]) -> bool:
        seen: set[int] = set()
        for n in nums:
            if n in seen:
                return True
            seen.add(n)
        return False
