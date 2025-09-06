# 0055. Jump Game

## Quick Facts

- URL: https://leetcode.com/problems/jump-game/
- Signature: `nums: list[int]` → `bool`
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
- Run: `pytest -q -k "0055"`

## Common Pitfalls

- [pitfall 1]
- [pitfall 2]
- [pitfall 3]

## Similar Problems

| Number | Difficulty | Name | LeetCode |
|---|---|---|---|
| 0045 | Medium | [Jump Game II](../0045-jump-game-ii/readme.md) | [link](https://leetcode.com/problems/jump-game-ii/) |
| 1306 | Medium | [Jump Game III](../1306-jump-game-iii/readme.md) | [link](https://leetcode.com/problems/jump-game-iii/) |
| 1871 | Medium | [Jump Game VII](../1871-jump-game-vii/readme.md) | [link](https://leetcode.com/problems/jump-game-vii/) |
| 2297 | Medium | [Jump Game VIII](../2297-jump-game-viii/readme.md) | [link](https://leetcode.com/problems/jump-game-viii/) |
| 2617 | Hard | [Minimum Number of Visited Cells in a Grid](../2617-minimum-number-of-visited-cells-in-a-grid/readme.md) | [link](https://leetcode.com/problems/minimum-number-of-visited-cells-in-a-grid/) |
| 2789 | Medium | [Largest Element in an Array after Merge Operations](../2789-largest-element-in-an-array-after-merge-operations/readme.md) | [link](https://leetcode.com/problems/largest-element-in-an-array-after-merge-operations/) |

## References

- LeetCode problem and editorial links

## Changelog

- 2025-09-06T13:33:47Z: Created scaffold.
