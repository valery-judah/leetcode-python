# 0112. Path Sum

## Quick Facts

- URL: [Path Sum](https://leetcode.com/problems/path-sum/)
- Function: `hasPathSum`
- Signature: `(root: TreeNode | None, targetSum: int)  -> bool`
- Primary pattern: **Tree**

## Constraints

- `The number of nodes in the tree is in the range [0, 5000].`
- `-1000 <= Node.val <= 1000`
- `-1000 <= targetSum <= 1000`

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
- Run: `pytest -q -k "0112"`

## Common Pitfalls

- [pitfall 1]
- [pitfall 2]
- [pitfall 3]

## Similar Problems

| Number | Difficulty | Name | LeetCode |
|---|---|---|---|
| 0113 | Medium | [Path Sum II](../0113-path-sum-ii/readme.md) | [Path Sum II](https://leetcode.com/problems/path-sum-ii/) |
| 0124 | Hard | [Binary Tree Maximum Path Sum](../0124-binary-tree-maximum-path-sum/readme.md) | [Binary Tree Maximum Path Sum](https://leetcode.com/problems/binary-tree-maximum-path-sum/) |
| 0129 | Medium | [Sum Root to Leaf Numbers](../0129-sum-root-to-leaf-numbers/readme.md) | [Sum Root to Leaf Numbers](https://leetcode.com/problems/sum-root-to-leaf-numbers/) |
| 0437 | Medium | [Path Sum III](../0437-path-sum-iii/readme.md) | [Path Sum III](https://leetcode.com/problems/path-sum-iii/) |
| 0666 | Medium | [Path Sum IV](../0666-path-sum-iv/readme.md) | [Path Sum IV](https://leetcode.com/problems/path-sum-iv/) |

## Examples

### Example 1

```text
Input: root = [5,4,8,11,null,13,4,7,2,null,null,null,1], targetSum = 22
Output: true
Explanation: The root-to-leaf path with the target sum is shown.
```

### Example 2

```text
Input: root = [1,2,3], targetSum = 5
Output: false
Explanation: There are two root-to-leaf paths in the tree:
(1 --> 2): The sum is 3.
(1 --> 3): The sum is 4.
There is no root-to-leaf path with sum = 5.
```

### Example 3

```text
Input: root = [], targetSum = 0
Output: false
Explanation: Since the tree is empty, there are no root-to-leaf paths.
```

## References

- LeetCode problem and editorial links
