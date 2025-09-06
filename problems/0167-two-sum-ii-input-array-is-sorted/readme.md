# 0167. Two Sum II - Input Array Is Sorted

## Quick Facts

- URL: https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
- Signature: `numbers: list[int]`, `target: int` → `list[int]`
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
- Run: `pytest -q -k "0167"`

## Common Pitfalls

- [pitfall 1]
- [pitfall 2]
- [pitfall 3]

## Similar Problems

| Number | Difficulty | Name | LeetCode |
|---|---|---|---|
| 0001 | Easy | [Two Sum](../0001-two-sum/readme.md) | [link](https://leetcode.com/problems/two-sum/) |
| 0653 | Easy | [Two Sum IV - Input is a BST](../0653-two-sum-iv-input-is-a-bst/readme.md) | [link](https://leetcode.com/problems/two-sum-iv-input-is-a-bst/) |
| 1099 | Easy | [Two Sum Less Than K](../1099-two-sum-less-than-k/readme.md) | [link](https://leetcode.com/problems/two-sum-less-than-k/) |

## References

- LeetCode problem and editorial links

## Changelog

- 2025-09-06T13:33:51Z: Created scaffold.
