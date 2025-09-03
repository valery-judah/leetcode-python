
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

- Brute force O(n^2): check all pairs `(i, j)` and return at the first match.
- Optimal O(n) single pass using a hash map of seen values to indices:
  - For each `num` at index `i`, compute `need = target - num`.
  - If `need` is in the map, return `[map[need], i]`.
  - Otherwise store `map[num] = i` and continue.
- Correctness: when a complement exists earlier, it is returned immediately; otherwise, the current value becomes available as a complement for future elements.

- If the complement is already in the hash map, it means a solution has been found, and the indices of the complement and the current number are returned.
- If the complement is not in the map, the current number and its index are added to the map for future reference.

This approach avoids the need for a nested loop, which would result in an O(n^2) time complexity, and instead provides a more efficient O(n) solution.

## Complexity

- Time: O(n) — each element processed once with O(1) average lookups.
- Space: O(n) — worst case stores all elements in the hash map.

## Checklist

- [ ] Restate problem
- [ ] Small example walkthrough
- [ ] Choose DS/algorithm
- [ ] Dry-run core loop
- [ ] Code cleanly
- [ ] Test edge cases

See also: `docs/interview-framework.md`.
