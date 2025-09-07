# 0297. Serialize and Deserialize Binary Tree

## Quick Facts

- URL: [Serialize and Deserialize Binary Tree](https://leetcode.com/problems/serialize-and-deserialize-binary-tree/)
- Function: `Codec`
- Signature: `(root: TreeNode | None)  -> str`
- Primary pattern: **Tree**

## Constraints

- `The number of nodes in the tree is in the range [0, 10^4].`
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
- Run: `pytest -q -k "0297"`

## Common Pitfalls

- [pitfall 1]
- [pitfall 2]
- [pitfall 3]

## Similar Problems

| Number | Difficulty | Name | LeetCode |
|---|---|---|---|
| 0271 | Medium | [Encode and Decode Strings](../0271-encode-and-decode-strings/readme.md) | [Encode and Decode Strings](https://leetcode.com/problems/encode-and-decode-strings/) |
| 0449 | Medium | [Serialize and Deserialize BST](../0449-serialize-and-deserialize-bst/readme.md) | [Serialize and Deserialize BST](https://leetcode.com/problems/serialize-and-deserialize-bst/) |
| 0652 | Medium | [Find Duplicate Subtrees](../0652-find-duplicate-subtrees/readme.md) | [Find Duplicate Subtrees](https://leetcode.com/problems/find-duplicate-subtrees/) |
| 0765 | Hard | [Serialize and Deserialize N-ary Tree](../0765-serialize-and-deserialize-n-ary-tree/readme.md) | [Serialize and Deserialize N-ary Tree](https://leetcode.com/problems/serialize-and-deserialize-n-ary-tree/) |

## Examples

### Example 1

```text
Input: root = [1,2,3,null,null,4,5]
Output: [1,2,3,null,null,4,5]
```

### Example 2

```text
Input: root = []
Output: []
```

## References

- LeetCode problem and editorial links
