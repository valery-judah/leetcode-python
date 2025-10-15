# 0280. Wiggle Sort

## Quick Facts

- URL: [Wiggle Sort](https://leetcode.com/problems/wiggle-sort/)
- Function: `wiggleSort`
- Signature: `(nums: list[int])  -> None`
- Primary pattern: **Greedy**

## Constraints

- `1 <= nums.length <= 5 * 10^4`
- `0 <= nums[i] <= 10^4`
- `It is guaranteed that there will be an answer for the given input nums.`

## Problem Crux (1–2 sentences)

[state what must be detected/computed and key bound]

## Clarifying Questions (for interview)

- [input domain? ranges?]
- [edge-case semantics?]
- [any pair vs first pair? ties?]

## Reasoning Flow (notes-only)

[outline the logical steps that lead to the chosen approach]

## Approach Options

| #   | Idea           | When to use | Correctness invariant | Time       | Space |
| --- | -------------- | ----------- | --------------------- | ---------- | ----- |
| A   | [primary idea] | [scenario]  | [invariant]           | O(n)       | O(n)  |
| B   | [alternative]  | [scenario]  | [invariant]           | O(n log n) | O(1)  |
| C   | [reject]       | [why not]   | [violated invariant]  | -          | -     |

## Edge Cases Checklist

- [case 1]
- [case 2]
- [case 3]

## Correctness Sketch

[state the invariant and why it guarantees correctness]

## Implementation

- `solutions.py` should expose:
    - `ALL_SOLUTIONS = {"...": fn, "...": fn}`
    - Short notes on tradeoffs and pitfalls.

## Tests

- Deterministic cases covering all edge cases above
- Optional fuzz/property checks as applicable
- Run: `pytest -q -k "0280"`

## Common Pitfalls

- [pitfall 1]
- [pitfall 2]
- [pitfall 3]

## Similar Problems

| Number | Difficulty | Name                                                                                                                             | LeetCode                                                                                                                                      |
| ------ | ---------- | -------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------- |
| 0075   | Medium     | [Sort Colors](../0075-sort-colors/readme.md)                                                                                     | [Sort Colors](https://leetcode.com/problems/sort-colors/)                                                                                     |
| 0324   | Medium     | [Wiggle Sort II](../0324-wiggle-sort-ii/readme.md)                                                                               | [Wiggle Sort II](https://leetcode.com/problems/wiggle-sort-ii/)                                                                               |
| 1968   | Medium     | [Array With Elements Not Equal to Average of Neighbors](../1968-array-with-elements-not-equal-to-average-of-neighbors/readme.md) | [Array With Elements Not Equal to Average of Neighbors](https://leetcode.com/problems/array-with-elements-not-equal-to-average-of-neighbors/) |

## Examples

### Example 1

```text
Input: nums = [3,5,2,1,6,4]
Output: [3,5,1,6,2,4]
Explanation: [1,6,2,5,3,4] is also accepted.
```

### Example 2

```text
Input: nums = [6,6,5,6,3,8]
Output: [6,6,5,6,3,8]
```

## References

- LeetCode problem and editorial links
