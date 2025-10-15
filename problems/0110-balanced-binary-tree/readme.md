# 0110. Balanced Binary Tree

## Quick Facts

- URL: [Balanced Binary Tree](https://leetcode.com/problems/balanced-binary-tree/)
- Function: `isBalanced`
- Signature: `(root: TreeNode | None)  -> bool`
- Primary pattern: **Tree**

## Constraints

- `The number of nodes in the tree is in the range [0, 5000].`
- `-10^4 <= Node.val <= 10^4`

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
- Run: `pytest -q -k "0110"`

## Common Pitfalls

- [pitfall 1]
- [pitfall 2]
- [pitfall 3]

## Similar Problems

| Number | Difficulty | Name                                                                                                                   | LeetCode                                                                                                                            |
| ------ | ---------- | ---------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------- |
| 0104   | Easy       | [Maximum Depth of Binary Tree](../0104-maximum-depth-of-binary-tree/readme.md)                                         | [Maximum Depth of Binary Tree](https://leetcode.com/problems/maximum-depth-of-binary-tree/)                                         |
| 3319   | Medium     | [K-th Largest Perfect Subtree Size in Binary Tree](../3319-k-th-largest-perfect-subtree-size-in-binary-tree/readme.md) | [K-th Largest Perfect Subtree Size in Binary Tree](https://leetcode.com/problems/k-th-largest-perfect-subtree-size-in-binary-tree/) |
| 3340   | Easy       | [Check Balanced String](../3340-check-balanced-string/readme.md)                                                       | [Check Balanced String](https://leetcode.com/problems/check-balanced-string/)                                                       |

## Examples

### Example 1

```text
Input: root = [3,9,20,null,null,15,7]
Output: true
```

### Example 2

```text
Input: root = [1,2,2,3,3,null,null,4,4]
Output: false
```

### Example 3

```text
Input: root = []
Output: true
```

## References

- LeetCode problem and editorial links
