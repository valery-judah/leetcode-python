# 0041. First Missing Positive

## Quick Facts

- URL: https://leetcode.com/problems/first-missing-positive/
- Signature: `nums: list[int]` → `int`
- Constraints: [paste from LC]
- Primary pattern: [write primary pattern]

## Problem Crux (1–2 sentences)

[state what must be detected/computed and key bound]

## Clarifying Questions (for interview)

- [input domain? ranges?]
- [edge-case semantics?]
- [any pair vs first pair? ties?]

## Reasoning Flow (notes-only)

[outline the logical steps that lead to the chosen approach]

## Approach Options

| # | Idea | When to use | Correctness invariant | Time | Space |
|---|------|-------------|-----------------------|------|-------|
| A | [primary idea] | [scenario] | [invariant] | O(n) | O(n) |
| B | [alternative] | [scenario] | [invariant] | O(n log n) | O(1) |
| C | [reject] | [why not] | [violated invariant] | - | - |

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
- Run: `pytest -q -k "0041"`

## Common Pitfalls

- [pitfall 1]
- [pitfall 2]
- [pitfall 3]

## Similar Problems

| Number | Difficulty | Name | LeetCode |
|---|---|---|---|
| 0268 | Easy | [Missing Number](../0268-missing-number/readme.md) | [link](https://leetcode.com/problems/missing-number/) |
| 0287 | Medium | [Find the Duplicate Number](../0287-find-the-duplicate-number/readme.md) | [link](https://leetcode.com/problems/find-the-duplicate-number/) |
| 0448 | Easy | [Find All Numbers Disappeared in an Array](../0448-find-all-numbers-disappeared-in-an-array/readme.md) | [link](https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/) |
| 0765 | Hard | [Couples Holding Hands](../0765-couples-holding-hands/readme.md) | [link](https://leetcode.com/problems/couples-holding-hands/) |
| 2336 | Medium | [Smallest Number in Infinite Set](../2336-smallest-number-in-infinite-set/readme.md) | [link](https://leetcode.com/problems/smallest-number-in-infinite-set/) |
| 2554 | Medium | [Maximum Number of Integers to Choose From a Range I](../2554-maximum-number-of-integers-to-choose-from-a-range-i/readme.md) | [link](https://leetcode.com/problems/maximum-number-of-integers-to-choose-from-a-range-i/) |
| 2598 | Medium | [Smallest Missing Non-negative Integer After Operations](../2598-smallest-missing-non-negative-integer-after-operations/readme.md) | [link](https://leetcode.com/problems/smallest-missing-non-negative-integer-after-operations/) |
| 2557 | Medium | [Maximum Number of Integers to Choose From a Range II](../2557-maximum-number-of-integers-to-choose-from-a-range-ii/readme.md) | [link](https://leetcode.com/problems/maximum-number-of-integers-to-choose-from-a-range-ii/) |
| 2996 | Easy | [Smallest Missing Integer Greater Than Sequential Prefix Sum](../2996-smallest-missing-integer-greater-than-sequential-prefix-sum/readme.md) | [link](https://leetcode.com/problems/smallest-missing-integer-greater-than-sequential-prefix-sum/) |

## References

- LeetCode problem and editorial links

## Changelog

- 2025-09-06T13:33:47Z: Created scaffold.
