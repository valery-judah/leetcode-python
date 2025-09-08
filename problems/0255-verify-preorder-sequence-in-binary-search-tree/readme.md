# 0255. Verify Preorder Sequence in Binary Search Tree

## Quick Facts

- URL: [Verify Preorder Sequence in Binary Search Tree](https://leetcode.com/problems/verify-preorder-sequence-in-binary-search-tree/)
- Function: `verifyPreorder`
- Signature: `(preorder: list[int])  -> bool`
- Primary pattern: **Tree**

## Constraints

- `1 <= preorder.length <= 10^4`
- `1 <= preorder[i] <= 10^4`
- `All the elements of preorder are unique.`

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
- Run: `pytest -q -k "0255"`

## Common Pitfalls

- [pitfall 1]
- [pitfall 2]
- [pitfall 3]

## Similar Problems

| Number | Difficulty | Name | LeetCode |
|---|---|---|---|
| 0144 | Easy | [Binary Tree Preorder Traversal](../0144-binary-tree-preorder-traversal/readme.md) | [Binary Tree Preorder Traversal](https://leetcode.com/problems/binary-tree-preorder-traversal/) |

## Examples

### Example 1

```text
Input: preorder = [5,2,1,3,6]
Output: true
```

### Example 2

```text
Input: preorder = [5,2,6,1,3]
Output: false
```

## References

- LeetCode problem and editorial links
