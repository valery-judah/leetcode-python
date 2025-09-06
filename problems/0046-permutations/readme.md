# 0046. Permutations

## Quick Facts

- URL: https://leetcode.com/problems/permutations/
- Signature: `nums: list[int]` → `list[list[int]]`
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
- Run: `pytest -q -k "0046"`

## Common Pitfalls

- [pitfall 1]
- [pitfall 2]
- [pitfall 3]

## Similar Problems

| Number | Difficulty | Name | LeetCode |
|---|---|---|---|
| 0031 | Medium | [Next Permutation](../0031-next-permutation/readme.md) | [link](https://leetcode.com/problems/next-permutation/) |
| 0047 | Medium | [Permutations II](../0047-permutations-ii/readme.md) | [link](https://leetcode.com/problems/permutations-ii/) |
| 0060 | Hard | [Permutation Sequence](../0060-permutation-sequence/readme.md) | [link](https://leetcode.com/problems/permutation-sequence/) |
| 0077 | Medium | [Combinations](../0077-combinations/readme.md) | [link](https://leetcode.com/problems/combinations/) |

## References

- LeetCode problem and editorial links

## Changelog

- 2025-09-06T13:33:47Z: Created scaffold.
