# 0272. Closest Binary Search Tree Value II

## Quick Facts

- URL: https://leetcode.com/problems/closest-binary-search-tree-value-ii/
- Signature: `root: TreeNode | None`, `target: float`, `k: int` → `list[int]`
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
- Run: `pytest -q -k "0272"`

## Common Pitfalls

- [pitfall 1]
- [pitfall 2]
- [pitfall 3]

## Similar Problems

| Number | Difficulty | Name | LeetCode |
|---|---|---|---|
| 0094 | Easy | [Binary Tree Inorder Traversal](../0094-binary-tree-inorder-traversal/readme.md) | [link](https://leetcode.com/problems/binary-tree-inorder-traversal/) |
| 0270 | Easy | [Closest Binary Search Tree Value](../0270-closest-binary-search-tree-value/readme.md) | [link](https://leetcode.com/problems/closest-binary-search-tree-value/) |
| 2476 | Medium | [Closest Nodes Queries in a Binary Search Tree](../2476-closest-nodes-queries-in-a-binary-search-tree/readme.md) | [link](https://leetcode.com/problems/closest-nodes-queries-in-a-binary-search-tree/) |

## References

- LeetCode problem and editorial links

## Changelog

- 2025-09-06T13:33:54Z: Created scaffold.
