# 0530. Minimum Absolute Difference in BST

## Quick Facts

- URL: [Minimum Absolute Difference in BST](https://leetcode.com/problems/minimum-absolute-difference-in-bst/)
- Function: `getMinimumDifference`
- Signature: `(root: TreeNode | None)  -> int`
- Primary pattern: **Tree**

## Constraints

- `The number of nodes in the tree is in the range [2, 10^4].`
- `0 <= Node.val <= 10^5`

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
- Run: `pytest -q -k "0530"`

## Common Pitfalls

- [pitfall 1]
- [pitfall 2]
- [pitfall 3]

## Similar Problems

| Number | Difficulty | Name                                                                   | LeetCode                                                                            |
| ------ | ---------- | ---------------------------------------------------------------------- | ----------------------------------------------------------------------------------- |
| 0532   | Medium     | [K-diff Pairs in an Array](../0532-k-diff-pairs-in-an-array/readme.md) | [K-diff Pairs in an Array](https://leetcode.com/problems/k-diff-pairs-in-an-array/) |

## Examples

### Example 1

```text
Input: root = [4,2,6,1,3]
Output: 1
```

### Example 2

```text
Input: root = [1,0,48,null,null,12,49]
Output: 1
```

## References

- LeetCode problem and editorial links
