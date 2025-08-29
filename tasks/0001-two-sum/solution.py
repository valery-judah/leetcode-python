"""
Problem 1: Two Sum
https://leetcode.com/problems/two-sum/
Difficulty: easy
Tags: array,hash-map
"""

from __future__ import annotations

# Implement your solution in a class or functions.
# Keep APIs simple for testability. Fill signature as needed.


class Solution:
    def solve(self, nums: list[int], target: int) -> list[int]:
        """
        Finds two numbers in a list that add up to a specific target.

        This method uses a hash map to achieve a single-pass solution with
        O(n) time complexity, which is optimal. It iterates through the list,
        and for each element, it calculates the complement needed to reach
        the target. If the complement is already in the hash map, it means
        a solution has been found, and the indices are returned. Otherwise,
        the current number and its index are added to the map.

        Args:
            nums: A list of integers.
            target: The target sum.

        Returns:
            A list containing the indices of the two numbers that add up to
            the target.
        """
        num_map = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in num_map:
                return [num_map[complement], i]
            num_map[num] = i
        return []
