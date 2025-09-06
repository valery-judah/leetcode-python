# 0023. Merge k Sorted Lists

## Quick Facts

- URL: https://leetcode.com/problems/merge-k-sorted-lists/
- Signature: `lists: list[ListNode | None]` → `ListNode | None`
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
- Run: `pytest -q -k "0023"`

## Common Pitfalls

- [pitfall 1]
- [pitfall 2]
- [pitfall 3]

## Similar Problems

| Number | Difficulty | Name | LeetCode |
|---|---|---|---|
| 0021 | Easy | [Merge Two Sorted Lists](../0021-merge-two-sorted-lists/readme.md) | [link](https://leetcode.com/problems/merge-two-sorted-lists/) |
| 0264 | Medium | [Ugly Number II](../0264-ugly-number-ii/readme.md) | [link](https://leetcode.com/problems/ugly-number-ii/) |
| 2411 | Medium | [Smallest Subarrays With Maximum Bitwise OR](../2411-smallest-subarrays-with-maximum-bitwise-or/readme.md) | [link](https://leetcode.com/problems/smallest-subarrays-with-maximum-bitwise-or/) |

## References

- LeetCode problem and editorial links

## Changelog

- 2025-09-06T13:33:46Z: Created scaffold.
