# 0347. Top K Frequent Elements

## Quick Facts

- URL: https://leetcode.com/problems/top-k-frequent-elements/
- Signature: `nums: list[int]`, `k: int` → `list[int]`
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
- Run: `pytest -q -k "0347"`

## Common Pitfalls

- [pitfall 1]
- [pitfall 2]
- [pitfall 3]

## Similar Problems

| Number | Difficulty | Name | LeetCode |
|---|---|---|---|
| 0192 | Medium | [Word Frequency](../0192-word-frequency/readme.md) | [link](https://leetcode.com/problems/word-frequency/) |
| 0215 | Medium | [Kth Largest Element in an Array](../0215-kth-largest-element-in-an-array/readme.md) | [link](https://leetcode.com/problems/kth-largest-element-in-an-array/) |
| 0451 | Medium | [Sort Characters By Frequency](../0451-sort-characters-by-frequency/readme.md) | [link](https://leetcode.com/problems/sort-characters-by-frequency/) |
| 0659 | Medium | [Split Array into Consecutive Subsequences](../0659-split-array-into-consecutive-subsequences/readme.md) | [link](https://leetcode.com/problems/split-array-into-consecutive-subsequences/) |
| 0692 | Medium | [Top K Frequent Words](../0692-top-k-frequent-words/readme.md) | [link](https://leetcode.com/problems/top-k-frequent-words/) |
| 0973 | Medium | [K Closest Points to Origin](../0973-k-closest-points-to-origin/readme.md) | [link](https://leetcode.com/problems/k-closest-points-to-origin/) |
| 1772 | Medium | [Sort Features by Popularity](../1772-sort-features-by-popularity/readme.md) | [link](https://leetcode.com/problems/sort-features-by-popularity/) |
| 2284 | Medium | [Sender With Largest Word Count](../2284-sender-with-largest-word-count/readme.md) | [link](https://leetcode.com/problems/sender-with-largest-word-count/) |
| 2404 | Easy | [Most Frequent Even Element](../2404-most-frequent-even-element/readme.md) | [link](https://leetcode.com/problems/most-frequent-even-element/) |
| 3063 | Easy | [Linked List Frequency](../3063-linked-list-frequency/readme.md) | [link](https://leetcode.com/problems/linked-list-frequency/) |

## References

- LeetCode problem and editorial links

## Changelog

- 2025-09-06T13:33:56Z: Created scaffold.
