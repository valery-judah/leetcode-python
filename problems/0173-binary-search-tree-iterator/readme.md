# 0173. Binary Search Tree Iterator

## Quick Facts

- URL: https://leetcode.com/problems/binary-search-tree-iterator/
- Signature: `inputs: list[int]`, `inputs: list[int]` → `list[int]`
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
- Run: `pytest -q -k "0173"`

## Common Pitfalls

- [pitfall 1]
- [pitfall 2]
- [pitfall 3]

## Similar Problems

| Number | Difficulty | Name | LeetCode |
|---|---|---|---|
| 0094 | Easy | [Binary Tree Inorder Traversal](../0094-binary-tree-inorder-traversal/readme.md) | [link](https://leetcode.com/problems/binary-tree-inorder-traversal/) |
| 0251 | Medium | [Flatten 2D Vector](../0251-flatten-2d-vector/readme.md) | [link](https://leetcode.com/problems/flatten-2d-vector/) |
| 0281 | Medium | [Zigzag Iterator](../0281-zigzag-iterator/readme.md) | [link](https://leetcode.com/problems/zigzag-iterator/) |
| 0284 | Medium | [Peeking Iterator](../0284-peeking-iterator/readme.md) | [link](https://leetcode.com/problems/peeking-iterator/) |
| 0285 | Medium | [Inorder Successor in BST](../0285-inorder-successor-in-bst/readme.md) | [link](https://leetcode.com/problems/inorder-successor-in-bst/) |
| 1586 | Medium | [Binary Search Tree Iterator II](../1586-binary-search-tree-iterator-ii/readme.md) | [link](https://leetcode.com/problems/binary-search-tree-iterator-ii/) |

## References

- LeetCode problem and editorial links

## Changelog

- 2025-09-06T13:33:52Z: Created scaffold.
