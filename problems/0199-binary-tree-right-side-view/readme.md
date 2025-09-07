# 0199. Binary Tree Right Side View

## Quick Facts

- URL: [Binary Tree Right Side View](https://leetcode.com/problems/binary-tree-right-side-view/)
- Function: `rightSideView`
- Signature: `(root: TreeNode | None)  -> list[int]`
- Primary pattern: **Tree**

## Constraints

- `The number of nodes in the tree is in the range [0, 100].`
- `-100 <= Node.val <= 100`

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
- Run: `pytest -q -k "0199"`

## Common Pitfalls

- [pitfall 1]
- [pitfall 2]
- [pitfall 3]

## Similar Problems

| Number | Difficulty | Name | LeetCode |
|---|---|---|---|
| 0116 | Medium | [Populating Next Right Pointers in Each Node](../0116-populating-next-right-pointers-in-each-node/readme.md) | [Populating Next Right Pointers in Each Node](https://leetcode.com/problems/populating-next-right-pointers-in-each-node/) |
| 0545 | Medium | [Boundary of Binary Tree](../0545-boundary-of-binary-tree/readme.md) | [Boundary of Binary Tree](https://leetcode.com/problems/boundary-of-binary-tree/) |

## Examples

None

## References

- LeetCode problem and editorial links
