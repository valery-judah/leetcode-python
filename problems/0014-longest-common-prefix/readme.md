# 0014. Longest Common Prefix

## Quick Facts

- URL: https://leetcode.com/problems/longest-common-prefix/
- Signature: `strs: list[str]` → `str`
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
- Run: `pytest -q -k "0014"`

## Common Pitfalls

- [pitfall 1]
- [pitfall 2]
- [pitfall 3]

## Similar Problems

| Number | Difficulty | Name | LeetCode |
|---|---|---|---|
| 2996 | Easy | [Smallest Missing Integer Greater Than Sequential Prefix Sum](../2996-smallest-missing-integer-greater-than-sequential-prefix-sum/readme.md) | [link](https://leetcode.com/problems/smallest-missing-integer-greater-than-sequential-prefix-sum/) |
| 3043 | Medium | [Find the Length of the Longest Common Prefix](../3043-find-the-length-of-the-longest-common-prefix/readme.md) | [link](https://leetcode.com/problems/find-the-length-of-the-longest-common-prefix/) |
| 3093 | Hard | [Longest Common Suffix Queries](../3093-longest-common-suffix-queries/readme.md) | [link](https://leetcode.com/problems/longest-common-suffix-queries/) |
| 3460 | Medium | [Longest Common Prefix After at Most One Removal](../3460-longest-common-prefix-after-at-most-one-removal/readme.md) | [link](https://leetcode.com/problems/longest-common-prefix-after-at-most-one-removal/) |

## References

- LeetCode problem and editorial links

## Changelog

- 2025-09-06T13:33:46Z: Created scaffold.
