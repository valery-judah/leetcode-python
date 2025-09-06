# 0235. Lowest Common Ancestor of a Binary Search Tree

## Quick Facts

- URL: https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/
- Signature: `root: TreeNode | None`, `p: int`, `q: int` → `TreeNode | None`
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
- Run: `pytest -q -k "0235"`

## Common Pitfalls

- [pitfall 1]
- [pitfall 2]
- [pitfall 3]

## Similar Problems

| Number | Difficulty | Name | LeetCode |
|---|---|---|---|
| 0236 | Medium | [Lowest Common Ancestor of a Binary Tree](../0236-lowest-common-ancestor-of-a-binary-tree/readme.md) | [link](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/) |
| 1257 | Medium | [Smallest Common Region](../1257-smallest-common-region/readme.md) | [link](https://leetcode.com/problems/smallest-common-region/) |
| 1644 | Medium | [Lowest Common Ancestor of a Binary Tree II](../1644-lowest-common-ancestor-of-a-binary-tree-ii/readme.md) | [link](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree-ii/) |
| 1650 | Medium | [Lowest Common Ancestor of a Binary Tree III](../1650-lowest-common-ancestor-of-a-binary-tree-iii/readme.md) | [link](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree-iii/) |
| 1676 | Medium | [Lowest Common Ancestor of a Binary Tree IV](../1676-lowest-common-ancestor-of-a-binary-tree-iv/readme.md) | [link](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree-iv/) |

## References

- LeetCode problem and editorial links

## Changelog

- 2025-09-06T13:33:53Z: Created scaffold.
