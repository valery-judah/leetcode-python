# 0222. Count Complete Tree Nodes

## Quick Facts

- URL: [Count Complete Tree Nodes](https://leetcode.com/problems/count-complete-tree-nodes/)
- Function: `countNodes`
- Signature: `(root: TreeNode | None)  -> int`
- Primary pattern: **Binary Search**

## Constraints

- `The number of nodes in the tree is in the range [0, 5 * 10^4].`
- `0 <= Node.val <= 5 * 10^4`
- `The tree is guaranteed to be complete.`

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
- Run: `pytest -q -k "0222"`

## Common Pitfalls

- [pitfall 1]
- [pitfall 2]
- [pitfall 3]

## Similar Problems

| Number | Difficulty | Name | LeetCode |
|---|---|---|---|
| 0270 | Easy | [Closest Binary Search Tree Value](../0270-closest-binary-search-tree-value/readme.md) | [Closest Binary Search Tree Value](https://leetcode.com/problems/closest-binary-search-tree-value/) |

## Examples

### Example 1

```text
Input: root = [1,2,3,4,5,6]
Output: 6
```

### Example 2

```text
Input: root = []
Output: 0
```

### Example 3

```text
Input: root = [1]
Output: 1
```

## References

- LeetCode problem and editorial links
