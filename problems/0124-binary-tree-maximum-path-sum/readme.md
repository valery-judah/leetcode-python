# 0124. Binary Tree Maximum Path Sum

## Quick Facts

- URL: [Binary Tree Maximum Path Sum](https://leetcode.com/problems/binary-tree-maximum-path-sum/)
- Function: `maxPathSum`
- Signature: `(root: TreeNode | None)  -> int`
- Primary pattern: **Tree**

## Constraints

- `The number of nodes in the tree is in the range [1, 3 * 10^4].`
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
- Run: `pytest -q -k "0124"`

## Common Pitfalls

- [pitfall 1]
- [pitfall 2]
- [pitfall 3]

## Similar Problems

| Number | Difficulty | Name                                                                                                                   | LeetCode                                                                                                                            |
| ------ | ---------- | ---------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------- |
| 0064   | Easy       | [Path Sum](../0064-path-sum/readme.md)                                                                                 | [Path Sum](https://leetcode.com/problems/path-sum/)                                                                                 |
| 0129   | Medium     | [Sum Root to Leaf Numbers](../0129-sum-root-to-leaf-numbers/readme.md)                                                 | [Sum Root to Leaf Numbers](https://leetcode.com/problems/sum-root-to-leaf-numbers/)                                                 |
| 0666   | Medium     | [Path Sum IV](../0666-path-sum-iv/readme.md)                                                                           | [Path Sum IV](https://leetcode.com/problems/path-sum-iv/)                                                                           |
| 0687   | Medium     | [Longest Univalue Path](../0687-longest-univalue-path/readme.md)                                                       | [Longest Univalue Path](https://leetcode.com/problems/longest-univalue-path/)                                                       |
| 1376   | Medium     | [Time Needed to Inform All Employees](../1376-time-needed-to-inform-all-employees/readme.md)                           | [Time Needed to Inform All Employees](https://leetcode.com/problems/time-needed-to-inform-all-employees/)                           |
| 2538   | Hard       | [Difference Between Maximum and Minimum Price Sum](../2538-difference-between-maximum-and-minimum-price-sum/readme.md) | [Difference Between Maximum and Minimum Price Sum](https://leetcode.com/problems/difference-between-maximum-and-minimum-price-sum/) |

## Examples

### Example 1

```text
Input: root = [1,2,3]
Output: 6
Explanation: The optimal path is 2 -> 1 -> 3 with a path sum of 2 + 1 + 3 = 6.
```

### Example 2

```text
Input: root = [-10,9,20,null,null,15,7]
Output: 42
Explanation: The optimal path is 15 -> 20 -> 7 with a path sum of 15 + 20 + 7 = 42.
```

## References

- LeetCode problem and editorial links
