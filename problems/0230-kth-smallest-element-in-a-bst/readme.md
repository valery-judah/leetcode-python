# 0230. Kth Smallest Element in a BST

## Quick Facts

- URL: [Kth Smallest Element in a BST](https://leetcode.com/problems/kth-smallest-element-in-a-bst/)
- Function: `kthSmallest`
- Signature: `(root: TreeNode | None, k: int)  -> int`
- Primary pattern: **Tree**

## Constraints

- `The number of nodes in the tree is n.`
- `1 <= k <= n <= 10^4`
- `0 <= Node.val <= 10^4`

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
- Run: `pytest -q -k "0230"`

## Common Pitfalls

- [pitfall 1]
- [pitfall 2]
- [pitfall 3]

## Similar Problems

| Number | Difficulty | Name | LeetCode |
|---|---|---|---|
| 0094 | Easy | [Binary Tree Inorder Traversal](../0094-binary-tree-inorder-traversal/readme.md) | [Binary Tree Inorder Traversal](https://leetcode.com/problems/binary-tree-inorder-traversal/) |
| 0671 | Easy | [Second Minimum Node In a Binary Tree](../0671-second-minimum-node-in-a-binary-tree/readme.md) | [Second Minimum Node In a Binary Tree](https://leetcode.com/problems/second-minimum-node-in-a-binary-tree/) |

## Examples

### Example 1

```text
Input: root = [3,1,4,null,2], k = 1
Output: 1
```

### Example 2

```text
Input: root = [5,3,6,2,4,null,null,1], k = 3
Output: 3
```

## References

- LeetCode problem and editorial links
