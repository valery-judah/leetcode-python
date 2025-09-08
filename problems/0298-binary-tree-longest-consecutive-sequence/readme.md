# 0298. Binary Tree Longest Consecutive Sequence

## Quick Facts

- URL: [Binary Tree Longest Consecutive Sequence](https://leetcode.com/problems/binary-tree-longest-consecutive-sequence/)
- Function: `longestConsecutive`
- Signature: `(root: TreeNode | None)  -> int`
- Primary pattern: **Tree**

## Constraints

- `The number of nodes in the tree is in the range [1, 3 * 10^4].`
- `-3 * 10^4 <= Node.val <= 3 * 10^4`

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
- Run: `pytest -q -k "0298"`

## Common Pitfalls

- [pitfall 1]
- [pitfall 2]
- [pitfall 3]

## Similar Problems

| Number | Difficulty | Name | LeetCode |
|---|---|---|---|
| 0128 | Medium | [Longest Consecutive Sequence](../0128-longest-consecutive-sequence/readme.md) | [Longest Consecutive Sequence](https://leetcode.com/problems/longest-consecutive-sequence/) |
| 0549 | Medium | [Binary Tree Longest Consecutive Sequence II](../0549-binary-tree-longest-consecutive-sequence-ii/readme.md) | [Binary Tree Longest Consecutive Sequence II](https://leetcode.com/problems/binary-tree-longest-consecutive-sequence-ii/) |
| 2229 | Easy | [Check if an Array Is Consecutive](../2229-check-if-an-array-is-consecutive/readme.md) | [Check if an Array Is Consecutive](https://leetcode.com/problems/check-if-an-array-is-consecutive/) |

## Examples

### Example 1

```text
Input: root = [1,null,3,2,4,null,null,null,5]
Output: 3
Explanation: Longest consecutive sequence path is 3-4-5, so return 3.
```

### Example 2

```text
Input: root = [2,null,3,2,null,1]
Output: 2
Explanation: Longest consecutive sequence path is 2-3, not 3-2-1, so return 2.
```

## References

- LeetCode problem and editorial links
