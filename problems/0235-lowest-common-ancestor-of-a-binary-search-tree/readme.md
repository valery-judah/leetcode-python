# 0235. Lowest Common Ancestor of a Binary Search Tree

## Quick Facts

- URL:
  [Lowest Common Ancestor of a Binary Search Tree](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/)
- Function: `lowestCommonAncestor`
- Signature: `(root: TreeNode | None, p: int, q: int)  -> TreeNode | None`
- Primary pattern: **Tree**

## Constraints

- `The number of nodes in the tree is in the range [2, 10^5].`
- `-10^9 <= Node.val <= 10^9`
- `All Node.val are unique.`
- `p != q`
- `p and q will exist in the BST.`

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
- Run: `pytest -q -k "0235"`

## Common Pitfalls

- [pitfall 1]
- [pitfall 2]
- [pitfall 3]

## Similar Problems

| Number | Difficulty | Name                                                                                                         | LeetCode                                                                                                                  |
| ------ | ---------- | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------- |
| 0236   | Medium     | [Lowest Common Ancestor of a Binary Tree](../0236-lowest-common-ancestor-of-a-binary-tree/readme.md)         | [Lowest Common Ancestor of a Binary Tree](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/)         |
| 1257   | Medium     | [Smallest Common Region](../1257-smallest-common-region/readme.md)                                           | [Smallest Common Region](https://leetcode.com/problems/smallest-common-region/)                                           |
| 1644   | Medium     | [Lowest Common Ancestor of a Binary Tree II](../1644-lowest-common-ancestor-of-a-binary-tree-ii/readme.md)   | [Lowest Common Ancestor of a Binary Tree II](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree-ii/)   |
| 1650   | Medium     | [Lowest Common Ancestor of a Binary Tree III](../1650-lowest-common-ancestor-of-a-binary-tree-iii/readme.md) | [Lowest Common Ancestor of a Binary Tree III](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree-iii/) |
| 1676   | Medium     | [Lowest Common Ancestor of a Binary Tree IV](../1676-lowest-common-ancestor-of-a-binary-tree-iv/readme.md)   | [Lowest Common Ancestor of a Binary Tree IV](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree-iv/)   |

## Examples

### Example 1

```text
Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
Output: 6
Explanation: The LCA of nodes 2 and 8 is 6.
```

### Example 2

```text
Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 4
Output: 2
Explanation: The LCA of nodes 2 and 4 is 2, since a node can be a descendant of itself according to the LCA definition.
```

### Example 3

```text
Input: root = [2,1], p = 2, q = 1
Output: 2
```

## References

- LeetCode problem and editorial links
