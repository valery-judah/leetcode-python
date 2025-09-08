# 0337. House Robber III

## Quick Facts

- URL: [House Robber III](https://leetcode.com/problems/house-robber-iii/)
- Function: `rob`
- Signature: `(root: TreeNode | None)  -> int`
- Primary pattern: **Tree**

## Constraints

- `The number of nodes in the tree is in the range [1, 10^4].`
- `0 <= Node.val <= 10^4`

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
- Run: `pytest -q -k "0337"`

## Common Pitfalls

- [pitfall 1]
- [pitfall 2]
- [pitfall 3]

## Similar Problems

| Number | Difficulty | Name | LeetCode |
|---|---|---|---|
| 0198 | Medium | [House Robber](../0198-house-robber/readme.md) | [House Robber](https://leetcode.com/problems/house-robber/) |
| 0213 | Medium | [House Robber II](../0213-house-robber-ii/readme.md) | [House Robber II](https://leetcode.com/problems/house-robber-ii/) |

## Examples

### Example 1

```text
Input: root = [3,2,3,null,3,null,1]
Output: 7
Explanation: Maximum amount of money the thief can rob = 3 + 3 + 1 = 7.
```

### Example 2

```text
Input: root = [3,4,5,1,3,null,1]
Output: 9
Explanation: Maximum amount of money the thief can rob = 4 + 5 = 9.
```

## References

- LeetCode problem and editorial links
