# 0236. Lowest Common Ancestor of a Binary Tree

## Quick Facts

- URL: https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/
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
- Run: `pytest -q -k "0236"`

## Common Pitfalls

- [pitfall 1]
- [pitfall 2]
- [pitfall 3]

## Similar Problems

| Number | Difficulty | Name | LeetCode |
|---|---|---|---|
| 0235 | Medium | [Lowest Common Ancestor of a Binary Search Tree](../0235-lowest-common-ancestor-of-a-binary-search-tree/readme.md) | [link](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/) |
| 1257 | Medium | [Smallest Common Region](../1257-smallest-common-region/readme.md) | [link](https://leetcode.com/problems/smallest-common-region/) |
| 2225 | Medium | [Find Players With Zero or One Losses](../2225-find-players-with-zero-or-one-losses/readme.md) | [link](https://leetcode.com/problems/find-players-with-zero-or-one-losses/) |
| 1644 | Medium | [Lowest Common Ancestor of a Binary Tree II](../1644-lowest-common-ancestor-of-a-binary-tree-ii/readme.md) | [link](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree-ii/) |
| 1650 | Medium | [Lowest Common Ancestor of a Binary Tree III](../1650-lowest-common-ancestor-of-a-binary-tree-iii/readme.md) | [link](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree-iii/) |
| 1676 | Medium | [Lowest Common Ancestor of a Binary Tree IV](../1676-lowest-common-ancestor-of-a-binary-tree-iv/readme.md) | [link](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree-iv/) |
| 2096 | Medium | [Step-By-Step Directions From a Binary Tree Node to Another](../2096-step-by-step-directions-from-a-binary-tree-node-to-another/readme.md) | [link](https://leetcode.com/problems/step-by-step-directions-from-a-binary-tree-node-to-another/) |
| 2509 | Hard | [Cycle Length Queries in a Tree](../2509-cycle-length-queries-in-a-tree/readme.md) | [link](https://leetcode.com/problems/cycle-length-queries-in-a-tree/) |

## References

- LeetCode problem and editorial links

## Changelog

- 2025-09-06T13:33:53Z: Created scaffold.
