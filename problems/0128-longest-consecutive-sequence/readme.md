# 0128. Longest Consecutive Sequence

## Quick Facts

- URL: https://leetcode.com/problems/longest-consecutive-sequence/
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
- Run: `pytest -q -k "0128"`

## Common Pitfalls

- [pitfall 1]
- [pitfall 2]
- [pitfall 3]

## Similar Problems

| Number | Difficulty | Name | LeetCode |
|---|---|---|---|
| 0298 | Medium | [Binary Tree Longest Consecutive Sequence](../0298-binary-tree-longest-consecutive-sequence/readme.md) | [link](https://leetcode.com/problems/binary-tree-longest-consecutive-sequence/) |
| 2177 | Medium | [Find Three Consecutive Integers That Sum to a Given Number](../2177-find-three-consecutive-integers-that-sum-to-a-given-number/readme.md) | [link](https://leetcode.com/problems/find-three-consecutive-integers-that-sum-to-a-given-number/) |
| 2274 | Medium | [Maximum Consecutive Floors Without Special Floors](../2274-maximum-consecutive-floors-without-special-floors/readme.md) | [link](https://leetcode.com/problems/maximum-consecutive-floors-without-special-floors/) |
| 2414 | Medium | [Length of the Longest Alphabetical Continuous Substring](../2414-length-of-the-longest-alphabetical-continuous-substring/readme.md) | [link](https://leetcode.com/problems/length-of-the-longest-alphabetical-continuous-substring/) |
| 3020 | Medium | [Find the Maximum Number of Elements in Subset](../3020-find-the-maximum-number-of-elements-in-subset/readme.md) | [link](https://leetcode.com/problems/find-the-maximum-number-of-elements-in-subset/) |

## References

- LeetCode problem and editorial links

## Changelog

- 2025-09-06T13:33:50Z: Created scaffold.
