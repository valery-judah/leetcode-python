# 1650. Lowest Common Ancestor of a Binary Tree III

## Quick Facts

- URL:
  [Lowest Common Ancestor of a Binary Tree III](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree-iii/)
- Function: `lowestCommonAncestor`
- Signature: `(root: list[int], p: int, q: int)  -> TreeNode | None`
- Primary pattern: **Two Pointers**

## Constraints

- `The number of nodes in the tree is in the range [2, 10^5].`
- `-10^9 <= Node.val <= 10^9`
- `All Node.val are unique.`
- `p != q`
- `p and q exist in the tree.`

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
- Run: `pytest -q -k "1650"`

## Common Pitfalls

- [pitfall 1]
- [pitfall 2]
- [pitfall 3]

## Similar Problems

| Number | Difficulty | Name                                                                                                               | LeetCode                                                                                                                        |
| ------ | ---------- | ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------- |
| 0235   | Medium     | [Lowest Common Ancestor of a Binary Search Tree](../0235-lowest-common-ancestor-of-a-binary-search-tree/readme.md) | [Lowest Common Ancestor of a Binary Search Tree](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/) |
| 0236   | Medium     | [Lowest Common Ancestor of a Binary Tree](../0236-lowest-common-ancestor-of-a-binary-tree/readme.md)               | [Lowest Common Ancestor of a Binary Tree](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/)               |
| 1644   | Medium     | [Lowest Common Ancestor of a Binary Tree II](../1644-lowest-common-ancestor-of-a-binary-tree-ii/readme.md)         | [Lowest Common Ancestor of a Binary Tree II](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree-ii/)         |
| 1676   | Medium     | [Lowest Common Ancestor of a Binary Tree IV](../1676-lowest-common-ancestor-of-a-binary-tree-iv/readme.md)         | [Lowest Common Ancestor of a Binary Tree IV](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree-iv/)         |

## Examples

### Example 1

```text
class Node {{
    public int val;
    public Node left;
    public Node right;
    public Node parent;
}}
```

### Example 2

```text
Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
Output: 3
Explanation: The LCA of nodes 5 and 1 is 3.
```

### Example 3

```text
Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
Output: 5
Explanation: The LCA of nodes 5 and 4 is 5 since a node can be a descendant of itself according to the LCA definition.
```

### Example 4

```text
Input: root = [1,2], p = 1, q = 2
Output: 1
```

## References

- LeetCode problem and editorial links
