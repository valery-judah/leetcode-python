
# 1. Two Sum

**URL**: <https://leetcode.com/problems/two-sum/>
**Difficulty**: easy
**Tags**: array,hash-map

## Clarifying questions

- Input shape, ranges, constraints?
- Duplicates, negatives, empty input?
- Mutations allowed? Sorted? Streaming?

## Examples

- Add 2–3 examples and edge cases.

## Approach

The problem was solved using a hash map (`dict` in Python) to achieve an optimal single-pass solution. The algorithm iterates through the list of numbers, and for each number, it calculates the required complement to reach the target (`complement = target - num`).

- If the complement is already in the hash map, it means a solution has been found, and the indices of the complement and the current number are returned.
- If the complement is not in the map, the current number and its index are added to the map for future reference.

This approach avoids the need for a nested loop, which would result in an O(n^2) time complexity, and instead provides a more efficient O(n) solution.

## Complexity

- Time: O(n), because in the worst case, we will iterate through the entire list once.
- Space: O(n), because in the worst case, we will store all the numbers in the hash map.

## Checklist

- [ ] Restate problem
- [ ] Small example walkthrough
- [ ] Choose DS/algorithm
- [ ] Dry-run core loop
- [ ] Code cleanly
- [ ] Test edge cases

See also: `docs/interview-framework.md`.
