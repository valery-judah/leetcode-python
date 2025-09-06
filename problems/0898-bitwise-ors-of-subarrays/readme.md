# 0898. Bitwise ORs of Subarrays

## Quick Facts

- URL: https://leetcode.com/problems/bitwise-ors-of-subarrays/
- Signature: `arr: list[int]` → `int`
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
- Run: `pytest -q -k "0898"`

## Common Pitfalls

- [pitfall 1]
- [pitfall 2]
- [pitfall 3]

## Similar Problems

| Number | Difficulty | Name | LeetCode |
|---|---|---|---|
| 2401 | Medium | [Longest Nice Subarray](../2401-longest-nice-subarray/readme.md) | [link](https://leetcode.com/problems/longest-nice-subarray/) |
| 2411 | Medium | [Smallest Subarrays With Maximum Bitwise OR](../2411-smallest-subarrays-with-maximum-bitwise-or/readme.md) | [link](https://leetcode.com/problems/smallest-subarrays-with-maximum-bitwise-or/) |
| 2505 | Medium | [Bitwise OR of All Subsequence Sums](../2505-bitwise-or-of-all-subsequence-sums/readme.md) | [link](https://leetcode.com/problems/bitwise-or-of-all-subsequence-sums/) |
| 3287 | Hard | [Find the Maximum Sequence Value of Array](../3287-find-the-maximum-sequence-value-of-array/readme.md) | [link](https://leetcode.com/problems/find-the-maximum-sequence-value-of-array/) |

## References

- LeetCode problem and editorial links

## Changelog

- 2025-09-06T13:34:00Z: Created scaffold.
