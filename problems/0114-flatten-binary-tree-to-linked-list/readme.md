# 0114. Flatten Binary Tree to Linked List

## Quick Facts

- URL: [Flatten Binary Tree to Linked List](https://leetcode.com/problems/flatten-binary-tree-to-linked-list/)
- Function: `flatten`
- Signature: `(root: TreeNode | None)  -> None`
- Primary pattern: **Tree**

## Constraints

- `The number of nodes in the tree is in the range [0, 2000].`
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
- Run: `pytest -q -k "0114"`

## Common Pitfalls

- [pitfall 1]
- [pitfall 2]
- [pitfall 3]

## Similar Problems

| Number | Difficulty | Name | LeetCode |
|---|---|---|---|
| 0430 | Medium | [Flatten a Multilevel Doubly Linked List](../0430-flatten-a-multilevel-doubly-linked-list/readme.md) | [Flatten a Multilevel Doubly Linked List](https://leetcode.com/problems/flatten-a-multilevel-doubly-linked-list/) |
| 1660 | Medium | [Correct a Binary Tree](../1660-correct-a-binary-tree/readme.md) | [Correct a Binary Tree](https://leetcode.com/problems/correct-a-binary-tree/) |

## Examples

### Example 1

```text
Input: root = [1,2,5,3,4,null,6]
Output: [1,null,2,null,3,null,4,null,5,null,6]
```

### Example 2

```text
Input: root = []
Output: []
```

### Example 3

```text
Input: root = [0]
Output: [0]
```

## References

- LeetCode problem and editorial links
