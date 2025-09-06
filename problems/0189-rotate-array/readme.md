# 0189. Rotate Array

## Quick Facts

- URL: https://leetcode.com/problems/rotate-array/
- Signature: `nums: list[int]`, `k: int` → `None`
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
- Run: `pytest -q -k "0189"`

## Common Pitfalls

- [pitfall 1]
- [pitfall 2]
- [pitfall 3]

## Similar Problems

| Number | Difficulty | Name | LeetCode |
|---|---|---|---|
| 0061 | Medium | [Rotate List](../0061-rotate-list/readme.md) | [link](https://leetcode.com/problems/rotate-list/) |
| 0186 | Medium | [Reverse Words in a String II](../0186-reverse-words-in-a-string-ii/readme.md) | [link](https://leetcode.com/problems/reverse-words-in-a-string-ii/) |
| 2607 | Medium | [Make K-Subarray Sums Equal](../2607-make-k-subarray-sums-equal/readme.md) | [link](https://leetcode.com/problems/make-k-subarray-sums-equal/) |
| 3400 | Medium | [Maximum Number of Matching Indices After Right Shifts](../3400-maximum-number-of-matching-indices-after-right-shifts/readme.md) | [link](https://leetcode.com/problems/maximum-number-of-matching-indices-after-right-shifts/) |

## References

- LeetCode problem and editorial links

## Changelog

- 2025-09-06T13:33:52Z: Created scaffold.
