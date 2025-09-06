# 0104. Maximum Depth of Binary Tree

## Quick Facts

- URL: https://leetcode.com/problems/maximum-depth-of-binary-tree/
- Signature: `root: TreeNode | None` → `int`
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
- Run: `pytest -q -k "0104"`

## Common Pitfalls

- [pitfall 1]
- [pitfall 2]
- [pitfall 3]

## Similar Problems

| Number | Difficulty | Name | LeetCode |
|---|---|---|---|
| 0110 | Easy | [Balanced Binary Tree](../0110-balanced-binary-tree/readme.md) | [link](https://leetcode.com/problems/balanced-binary-tree/) |
| 0111 | Easy | [Minimum Depth of Binary Tree](../0111-minimum-depth-of-binary-tree/readme.md) | [link](https://leetcode.com/problems/minimum-depth-of-binary-tree/) |
| 0559 | Easy | [Maximum Depth of N-ary Tree](../0559-maximum-depth-of-n-ary-tree/readme.md) | [link](https://leetcode.com/problems/maximum-depth-of-n-ary-tree/) |
| 1376 | Medium | [Time Needed to Inform All Employees](../1376-time-needed-to-inform-all-employees/readme.md) | [link](https://leetcode.com/problems/time-needed-to-inform-all-employees/) |
| 2385 | Medium | [Amount of Time for Binary Tree to Be Infected](../2385-amount-of-time-for-binary-tree-to-be-infected/readme.md) | [link](https://leetcode.com/problems/amount-of-time-for-binary-tree-to-be-infected/) |
| 2458 | Hard | [Height of Binary Tree After Subtree Removal Queries](../2458-height-of-binary-tree-after-subtree-removal-queries/readme.md) | [link](https://leetcode.com/problems/height-of-binary-tree-after-subtree-removal-queries/) |

## References

- LeetCode problem and editorial links

## Changelog

- 2025-09-06T13:33:49Z: Created scaffold.
