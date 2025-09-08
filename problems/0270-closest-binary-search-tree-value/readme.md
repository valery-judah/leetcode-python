# 0270. Closest Binary Search Tree Value

## Quick Facts

- URL: [Closest Binary Search Tree Value](https://leetcode.com/problems/closest-binary-search-tree-value/)
- Function: `closestValue`
- Signature: `(root: TreeNode | None, target: float)  -> int`
- Primary pattern: **Binary Search**

## Constraints

- `The number of nodes in the tree is in the range [1, 10^4].`
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
- Run: `pytest -q -k "0270"`

## Common Pitfalls

- [pitfall 1]
- [pitfall 2]
- [pitfall 3]

## Similar Problems

| Number | Difficulty | Name | LeetCode |
|---|---|---|---|
| 0222 | Easy | [Count Complete Tree Nodes](../0222-count-complete-tree-nodes/readme.md) | [Count Complete Tree Nodes](https://leetcode.com/problems/count-complete-tree-nodes/) |
| 0272 | Hard | [Closest Binary Search Tree Value II](../0272-closest-binary-search-tree-value-ii/readme.md) | [Closest Binary Search Tree Value II](https://leetcode.com/problems/closest-binary-search-tree-value-ii/) |
| 0700 | Easy | [Search in a Binary Search Tree](../0700-search-in-a-binary-search-tree/readme.md) | [Search in a Binary Search Tree](https://leetcode.com/problems/search-in-a-binary-search-tree/) |
| 2476 | Medium | [Closest Nodes Queries in a Binary Search Tree](../2476-closest-nodes-queries-in-a-binary-search-tree/readme.md) | [Closest Nodes Queries in a Binary Search Tree](https://leetcode.com/problems/closest-nodes-queries-in-a-binary-search-tree/) |

## Examples

### Example 1

```text
Input: root = [4,2,5,1,3], target = 3.714286
Output: 4
```

### Example 2

```text
Input: root = [1], target = 4.428571
Output: 1
```

## References

- LeetCode problem and editorial links
