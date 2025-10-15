# 0637. Average of Levels in Binary Tree

## Quick Facts

- URL: [Average of Levels in Binary Tree](https://leetcode.com/problems/average-of-levels-in-binary-tree/)
- Function: `averageOfLevels`
- Signature: `(root: TreeNode | None)  -> list[float]`
- Primary pattern: **Tree**

## Constraints

- `The number of nodes in the tree is in the range [1, 10^4].`
- `-2^31 <= Node.val <= 2^31 - 1`

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
- Run: `pytest -q -k "0637"`

## Common Pitfalls

- [pitfall 1]
- [pitfall 2]
- [pitfall 3]

## Similar Problems

| Number | Difficulty | Name                                                                                           | LeetCode                                                                                                    |
| ------ | ---------- | ---------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------- |
| 0102   | Medium     | [Binary Tree Level Order Traversal](../0102-binary-tree-level-order-traversal/readme.md)       | [Binary Tree Level Order Traversal](https://leetcode.com/problems/binary-tree-level-order-traversal/)       |
| 0107   | Medium     | [Binary Tree Level Order Traversal II](../0107-binary-tree-level-order-traversal-ii/readme.md) | [Binary Tree Level Order Traversal II](https://leetcode.com/problems/binary-tree-level-order-traversal-ii/) |

## Examples

### Example 1

```text
Input: root = [3,9,20,null,null,15,7]
Output: [3.00000,14.50000,11.00000]
Explanation: The average value of nodes on level 0 is 3, on level 1 is 14.5, and on level 2 is 11.
Hence return [3, 14.5, 11].
```

### Example 2

```text
Input: root = [3,9,20,15,7]
Output: [3.00000,14.50000,11.00000]
```

## References

- LeetCode problem and editorial links
