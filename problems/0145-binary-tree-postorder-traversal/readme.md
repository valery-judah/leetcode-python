# 0145. Binary Tree Postorder Traversal

## Quick Facts

- URL: https://leetcode.com/problems/binary-tree-postorder-traversal/
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
- Run: `pytest -q -k "0145"`

## Common Pitfalls

- [pitfall 1]
- [pitfall 2]
- [pitfall 3]

## Similar Problems

| Number | Difficulty | Name | LeetCode |
|---|---|---|---|
| 0094 | Easy | [Binary Tree Inorder Traversal](../0094-binary-tree-inorder-traversal/readme.md) | [link](https://leetcode.com/problems/binary-tree-inorder-traversal/) |
| 0590 | Easy | [N-ary Tree Postorder Traversal](../0590-n-ary-tree-postorder-traversal/readme.md) | [link](https://leetcode.com/problems/n-ary-tree-postorder-traversal/) |
| 2477 | Medium | [Minimum Fuel Cost to Report to the Capital](../2477-minimum-fuel-cost-to-report-to-the-capital/readme.md) | [link](https://leetcode.com/problems/minimum-fuel-cost-to-report-to-the-capital/) |

## References

- LeetCode problem and editorial links

## Changelog

- 2025-09-06T13:33:51Z: Created scaffold.
