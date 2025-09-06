# 0637. Average of Levels in Binary Tree

## Quick Facts

- URL: https://leetcode.com/problems/average-of-levels-in-binary-tree/
- Signature: `root: TreeNode | None` → `list[float]`
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
- Run: `pytest -q -k "0637"`

## Common Pitfalls

- [pitfall 1]
- [pitfall 2]
- [pitfall 3]

## Similar Problems

| Number | Difficulty | Name | LeetCode |
|---|---|---|---|
| 0102 | Medium | [Binary Tree Level Order Traversal](../0102-binary-tree-level-order-traversal/readme.md) | [link](https://leetcode.com/problems/binary-tree-level-order-traversal/) |
| 0107 | Medium | [Binary Tree Level Order Traversal II](../0107-binary-tree-level-order-traversal-ii/readme.md) | [link](https://leetcode.com/problems/binary-tree-level-order-traversal-ii/) |

## References

- LeetCode problem and editorial links

## Changelog

- 2025-09-06T13:33:58Z: Created scaffold.
