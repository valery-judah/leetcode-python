# 0094. Binary Tree Inorder Traversal

## Quick Facts

- URL: [Binary Tree Inorder Traversal](https://leetcode.com/problems/binary-tree-inorder-traversal/)
- Function: `inorderTraversal`
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

| #   | Idea           | When to use | Correctness invariant | Time       | Space |
| --- | -------------- | ----------- | --------------------- | ---------- | ----- |
| A   | [primary idea] | [scenario]  | [invariant]           | O(n)       | O(n)  |
| B   | [alternative]  | [scenario]  | [invariant]           | O(n log n) | O(1)  |
| C   | [reject]       | [why not]   | [violated invariant]  | -          | -     |

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
- Run: `pytest -q -k "0094"`

## Common Pitfalls

- [pitfall 1]
- [pitfall 2]
- [pitfall 3]

## Similar Problems

| Number | Difficulty | Name                                                                                                                                 | LeetCode                                                                                                                                          |
| ------ | ---------- | ------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------- |
| 0098   | Medium     | [Validate Binary Search Tree](../0098-validate-binary-search-tree/readme.md)                                                         | [Validate Binary Search Tree](https://leetcode.com/problems/validate-binary-search-tree/)                                                         |
| 0144   | Easy       | [Binary Tree Preorder Traversal](../0144-binary-tree-preorder-traversal/readme.md)                                                   | [Binary Tree Preorder Traversal](https://leetcode.com/problems/binary-tree-preorder-traversal/)                                                   |
| 0145   | Easy       | [Binary Tree Postorder Traversal](../0145-binary-tree-postorder-traversal/readme.md)                                                 | [Binary Tree Postorder Traversal](https://leetcode.com/problems/binary-tree-postorder-traversal/)                                                 |
| 0173   | Medium     | [Binary Search Tree Iterator](../0173-binary-search-tree-iterator/readme.md)                                                         | [Binary Search Tree Iterator](https://leetcode.com/problems/binary-search-tree-iterator/)                                                         |
| 0230   | Medium     | [Kth Smallest Element in a BST](../0230-kth-smallest-element-in-a-bst/readme.md)                                                     | [Kth Smallest Element in a BST](https://leetcode.com/problems/kth-smallest-element-in-a-bst/)                                                     |
| 0272   | Hard       | [Closest Binary Search Tree Value II](../0272-closest-binary-search-tree-value-ii/readme.md)                                         | [Closest Binary Search Tree Value II](https://leetcode.com/problems/closest-binary-search-tree-value-ii/)                                         |
| 0285   | Medium     | [Inorder Successor in BST](../0285-inorder-successor-in-bst/readme.md)                                                               | [Inorder Successor in BST](https://leetcode.com/problems/inorder-successor-in-bst/)                                                               |
| 0426   | Medium     | [Convert Binary Search Tree to Sorted Doubly Linked List](../0426-convert-binary-search-tree-to-sorted-doubly-linked-list/readme.md) | [Convert Binary Search Tree to Sorted Doubly Linked List](https://leetcode.com/problems/convert-binary-search-tree-to-sorted-doubly-linked-list/) |
| 0783   | Easy       | [Minimum Distance Between BST Nodes](../0783-minimum-distance-between-bst-nodes/readme.md)                                           | [Minimum Distance Between BST Nodes](https://leetcode.com/problems/minimum-distance-between-bst-nodes/)                                           |

## Examples

None

## References

- LeetCode problem and editorial links
