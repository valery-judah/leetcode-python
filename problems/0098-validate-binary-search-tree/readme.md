# 0098. Validate Binary Search Tree

## Quick Facts

- URL: [Validate Binary Search Tree](https://leetcode.com/problems/validate-binary-search-tree/)
- Function: `isValidBST`
- Signature: `(root: TreeNode | None)  -> bool`
- Primary pattern: **Tree**

## Constraints

- `The number of nodes in the tree is in the range [1, 10^4].`
- `-2^31 <= Node.val <= 2^31 - 1`

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
- Run: `pytest -q -k "0098"`

## Common Pitfalls

- [pitfall 1]
- [pitfall 2]
- [pitfall 3]

## Similar Problems

| Number | Difficulty | Name                                                                                 | LeetCode                                                                                          |
| ------ | ---------- | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------- |
| 0094   | Easy       | [Binary Tree Inorder Traversal](../0094-binary-tree-inorder-traversal/readme.md)     | [Binary Tree Inorder Traversal](https://leetcode.com/problems/binary-tree-inorder-traversal/)     |
| 0501   | Easy       | [Find Mode in Binary Search Tree](../0501-find-mode-in-binary-search-tree/readme.md) | [Find Mode in Binary Search Tree](https://leetcode.com/problems/find-mode-in-binary-search-tree/) |

## Examples

### Example 1

```text
Input: root = [2,1,3]
Output: true
```

### Example 2

```text
Input: root = [5,1,4,null,null,3,6]
Output: false
Explanation: The root node's value is 5 but its right child's value is 4.
```

## References

- LeetCode problem and editorial links
