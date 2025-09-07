# 0572. Subtree of Another Tree

## Quick Facts

- URL: [Subtree of Another Tree](https://leetcode.com/problems/subtree-of-another-tree/)
- Function: `isSubtree`
- Signature: `(root: TreeNode | None, subRoot: TreeNode | None)  -> bool`
- Primary pattern: **Tree**

## Constraints

- `The number of nodes in the root tree is in the range [1, 2000].`
- `The number of nodes in the subRoot tree is in the range [1, 1000].`
- `-10^4 <= root.val <= 10^4`
- `-10^4 <= subRoot.val <= 10^4`

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
- Run: `pytest -q -k "0572"`

## Common Pitfalls

- [pitfall 1]
- [pitfall 2]
- [pitfall 3]

## Similar Problems

| Number | Difficulty | Name | LeetCode |
|---|---|---|---|
| 0250 | Medium | [Count Univalue Subtrees](../0250-count-univalue-subtrees/readme.md) | [Count Univalue Subtrees](https://leetcode.com/problems/count-univalue-subtrees/) |
| 0508 | Medium | [Most Frequent Subtree Sum](../0508-most-frequent-subtree-sum/readme.md) | [Most Frequent Subtree Sum](https://leetcode.com/problems/most-frequent-subtree-sum/) |

## Examples

### Example 1

```text
Input: root = [3,4,5,1,2], subRoot = [4,1,2]
Output: true
```

### Example 2

```text
Input: root = [3,4,5,1,2,null,null,null,null,0], subRoot = [4,1,2]
Output: false
```

## References

- LeetCode problem and editorial links
