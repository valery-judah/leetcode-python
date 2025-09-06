# 0281. Zigzag Iterator

## Quick Facts

- URL: https://leetcode.com/problems/zigzag-iterator/
- Signature: `v1: list[int]`, `v2: list[int]` → `list[int]`
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
- Run: `pytest -q -k "0281"`

## Common Pitfalls

- [pitfall 1]
- [pitfall 2]
- [pitfall 3]

## Similar Problems

| Number | Difficulty | Name | LeetCode |
|---|---|---|---|
| 0173 | Medium | [Binary Search Tree Iterator](../0173-binary-search-tree-iterator/readme.md) | [link](https://leetcode.com/problems/binary-search-tree-iterator/) |
| 0251 | Medium | [Flatten 2D Vector](../0251-flatten-2d-vector/readme.md) | [link](https://leetcode.com/problems/flatten-2d-vector/) |
| 0284 | Medium | [Peeking Iterator](../0284-peeking-iterator/readme.md) | [link](https://leetcode.com/problems/peeking-iterator/) |
| 0341 | Medium | [Flatten Nested List Iterator](../0341-flatten-nested-list-iterator/readme.md) | [link](https://leetcode.com/problems/flatten-nested-list-iterator/) |
| 1768 | Easy | [Merge Strings Alternately](../1768-merge-strings-alternately/readme.md) | [link](https://leetcode.com/problems/merge-strings-alternately/) |

## References

- LeetCode problem and editorial links

## Changelog

- 2025-09-06T13:33:55Z: Created scaffold.
