from __future__ import annotations


class Solution:
    def solve(self, nums: list[int], k: int) -> bool:
        """
        Returns True if there exist indices i != j such that
        nums[i] == nums[j] and abs(i - j) <= k.

        Single-pass O(n) using a hashmap of last seen index per value.
        """
        last_index: dict[int, int] = {}
        for i, v in enumerate(nums):
            if v in last_index and i - last_index[v] <= k:
                return True
            last_index[v] = i
        return False
