# 0102. Binary Tree Level Order Traversal

## Quick Facts

- URL: [Binary Tree Level Order Traversal](https://leetcode.com/problems/binary-tree-level-order-traversal/)
- Function: `levelOrder`
- Signature: `(root: TreeNode | None)  -> list[list[int]]`
- Primary pattern: **Tree**

## Constraints

- `The number of nodes in the tree is in the range [0, 2000].`
- `-1000 <= Node.val <= 1000`

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
- Run: `pytest -q -k "0102"`

## Common Pitfalls

- [pitfall 1]
- [pitfall 2]
- [pitfall 3]

## Similar Problems

| Number | Difficulty | Name | LeetCode |
|---|---|---|---|
| 0103 | Medium | [Binary Tree Zigzag Level Order Traversal](../0103-binary-tree-zigzag-level-order-traversal/readme.md) | [Binary Tree Zigzag Level Order Traversal](https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/) |
| 0107 | Medium | [Binary Tree Level Order Traversal II](../0107-binary-tree-level-order-traversal-ii/readme.md) | [Binary Tree Level Order Traversal II](https://leetcode.com/problems/binary-tree-level-order-traversal-ii/) |
| 0111 | Easy | [Minimum Depth of Binary Tree](../0111-minimum-depth-of-binary-tree/readme.md) | [Minimum Depth of Binary Tree](https://leetcode.com/problems/minimum-depth-of-binary-tree/) |
| 0314 | Medium | [Binary Tree Vertical Order Traversal](../0314-binary-tree-vertical-order-traversal/readme.md) | [Binary Tree Vertical Order Traversal](https://leetcode.com/problems/binary-tree-vertical-order-traversal/) |
| 0637 | Easy | [Average of Levels in Binary Tree](../0637-average-of-levels-in-binary-tree/readme.md) | [Average of Levels in Binary Tree](https://leetcode.com/problems/average-of-levels-in-binary-tree/) |
| 0429 | Medium | [N-ary Tree Level Order Traversal](../0429-n-ary-tree-level-order-traversal/readme.md) | [N-ary Tree Level Order Traversal](https://leetcode.com/problems/n-ary-tree-level-order-traversal/) |
| 0993 | Easy | [Cousins in Binary Tree](../0993-cousins-in-binary-tree/readme.md) | [Cousins in Binary Tree](https://leetcode.com/problems/cousins-in-binary-tree/) |
| 2471 | Medium | [Minimum Number of Operations to Sort a Binary Tree by Level](../2471-minimum-number-of-operations-to-sort-a-binary-tree-by-level/readme.md) | [Minimum Number of Operations to Sort a Binary Tree by Level](https://leetcode.com/problems/minimum-number-of-operations-to-sort-a-binary-tree-by-level/) |
| 2493 | Hard | [Divide Nodes Into the Maximum Number of Groups](../2493-divide-nodes-into-the-maximum-number-of-groups/readme.md) | [Divide Nodes Into the Maximum Number of Groups](https://leetcode.com/problems/divide-nodes-into-the-maximum-number-of-groups/) |

## Examples

### Example 1

```text
Input: root = [3,9,20,null,null,15,7]
Output: [[3],[9,20],[15,7]]
```

### Example 2

```text
Input: root = [1]
Output: [[1]]
```

### Example 3

```text
Input: root = []
Output: []
```

## References

- LeetCode problem and editorial links
