# 0144. Binary Tree Preorder Traversal

## Quick Facts

- URL: https://leetcode.com/problems/binary-tree-preorder-traversal/
- Signature: `root: TreeNode | None` → `list[int]`
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
- Run: `pytest -q -k "0144"`

## Common Pitfalls

- [pitfall 1]
- [pitfall 2]
- [pitfall 3]

## Similar Problems

| Number | Difficulty | Name | LeetCode |
|---|---|---|---|
| 0094 | Easy | [Binary Tree Inorder Traversal](../0094-binary-tree-inorder-traversal/readme.md) | [link](https://leetcode.com/problems/binary-tree-inorder-traversal/) |
| 0255 | Medium | [Verify Preorder Sequence in Binary Search Tree](../0255-verify-preorder-sequence-in-binary-search-tree/readme.md) | [link](https://leetcode.com/problems/verify-preorder-sequence-in-binary-search-tree/) |
| 0589 | Easy | [N-ary Tree Preorder Traversal](../0589-n-ary-tree-preorder-traversal/readme.md) | [link](https://leetcode.com/problems/n-ary-tree-preorder-traversal/) |
| 2583 | Medium | [Kth Largest Sum in a Binary Tree](../2583-kth-largest-sum-in-a-binary-tree/readme.md) | [link](https://leetcode.com/problems/kth-largest-sum-in-a-binary-tree/) |

## References

- LeetCode problem and editorial links

## Changelog

- 2025-09-06T13:33:51Z: Created scaffold.
