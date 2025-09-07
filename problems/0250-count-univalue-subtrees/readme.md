# 0250. Count Univalue Subtrees

## Quick Facts

- URL: [Count Univalue Subtrees](https://leetcode.com/problems/count-univalue-subtrees/)
- Function: `countUnivalSubtrees`
- Signature: `(root: TreeNode | None)  -> int`
- Primary pattern: **Tree**

## Constraints

- `The number of the node in the tree will be in the range [0, 1000].`
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
- Run: `pytest -q -k "0250"`

## Common Pitfalls

- [pitfall 1]
- [pitfall 2]
- [pitfall 3]

## Similar Problems

| Number | Difficulty | Name | LeetCode |
|---|---|---|---|
| 0572 | Easy | [Subtree of Another Tree](../0572-subtree-of-another-tree/readme.md) | [Subtree of Another Tree](https://leetcode.com/problems/subtree-of-another-tree/) |
| 0687 | Medium | [Longest Univalue Path](../0687-longest-univalue-path/readme.md) | [Longest Univalue Path](https://leetcode.com/problems/longest-univalue-path/) |

## Examples

### Example 1

```text
Input: root = [5,1,5,5,5,null,5]
Output: 4
```

### Example 2

```text
Input: root = []
Output: 0
```

### Example 3

```text
Input: root = [5,5,5,5,5,null,5]
Output: 6
```

## References

- LeetCode problem and editorial links
