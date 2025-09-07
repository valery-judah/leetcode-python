# 0272. Closest Binary Search Tree Value II

## Quick Facts

- URL: [Closest Binary Search Tree Value II](https://leetcode.com/problems/closest-binary-search-tree-value-ii/)
- Function: `closestKValues`
- Signature: `(root: TreeNode | None, target: float, k: int)  -> list[int]`
- Primary pattern: **Two Pointers**

## Constraints

- `The number of nodes in the tree is n.`
- `1 <= k <= n <= 10^4.`
- `0 <= Node.val <= 10^9`
- `-10^9 <= target <= 10^9`

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
- Run: `pytest -q -k "0272"`

## Common Pitfalls

- [pitfall 1]
- [pitfall 2]
- [pitfall 3]

## Similar Problems

| Number | Difficulty | Name | LeetCode |
|---|---|---|---|
| 0094 | Easy | [Binary Tree Inorder Traversal](../0094-binary-tree-inorder-traversal/readme.md) | [Binary Tree Inorder Traversal](https://leetcode.com/problems/binary-tree-inorder-traversal/) |
| 0270 | Easy | [Closest Binary Search Tree Value](../0270-closest-binary-search-tree-value/readme.md) | [Closest Binary Search Tree Value](https://leetcode.com/problems/closest-binary-search-tree-value/) |
| 2476 | Medium | [Closest Nodes Queries in a Binary Search Tree](../2476-closest-nodes-queries-in-a-binary-search-tree/readme.md) | [Closest Nodes Queries in a Binary Search Tree](https://leetcode.com/problems/closest-nodes-queries-in-a-binary-search-tree/) |

## Examples

### Example 1

```text
Input: root = [4,2,5,1,3], target = 3.714286, k = 2
Output: [4,3]
```

### Example 2

```text
Input: root = [1], target = 0.000000, k = 1
Output: [1]
```

## References

- LeetCode problem and editorial links
