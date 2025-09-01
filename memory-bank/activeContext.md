# Active Context

- Date: 2025-08-29 16:31
- Task: 0001-two-sum
- URL: <https://leetcode.com/problems/two-sum/>
- Difficulty: easy
- Constraints: Given an array of integers `nums` and an integer `target`, return indices of the two numbers such that they add up to `target`. You may assume that each input would have exactly one solution, and you may not use the same element twice.
- Approach: Hash map (dictionary in Python) to store seen numbers and their indices. This allows for a single-pass O(n) time complexity solution.
- Test Plan:
  - Base case: `[2, 7, 11, 15]`, target `9` -> `[0, 1]`
  - Solution not at the start: `[3, 2, 4]`, target `6` -> `[1, 2]`
  - Duplicates: `[3, 3]`, target `6` -> `[0, 1]`
  - Negative numbers: `[-10, 7, 19, 15]`, target `9` -> `[0, 2]`
  - Zeroes: `[0, 4, 3, 0]`, target `0` -> `[0, 3]`
- TODO:
  - [x] Write tests
  - [x] Implement
  - [x] Optimize
  - [x] Document
