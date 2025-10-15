# 0701. Insert into a Binary Search Tree

## Quick Facts

- URL: [Insert into a Binary Search Tree](https://leetcode.com/problems/insert-into-a-binary-search-tree/)
- Function: `insertIntoBST`
- Signature: `(root: TreeNode | None, val: int)  -> TreeNode | None`
- Primary pattern: **Tree**

## Constraints

- `The number of nodes in the tree will be in the range [0, 10^4].`
- `-10^8 <= Node.val <= 10^8`
- `All the values Node.val are unique.`
- `-10^8 <= val <= 10^8`
- `It's guaranteed that val does not exist in the original BST.`

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
- Run: `pytest -q -k "0701"`

## Common Pitfalls

- [pitfall 1]
- [pitfall 2]
- [pitfall 3]

## Similar Problems

| Number | Difficulty | Name                                                                               | LeetCode                                                                                        |
| ------ | ---------- | ---------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- |
| 0700   | Easy       | [Search in a Binary Search Tree](../0700-search-in-a-binary-search-tree/readme.md) | [Search in a Binary Search Tree](https://leetcode.com/problems/search-in-a-binary-search-tree/) |

## Examples

### Example 1

```text
Input: root = [4,2,7,1,3], val = 5
Output: [4,2,7,1,3,5]
Explanation: Another accepted tree is:
```

### Example 2

```text
Input: root = [40,20,60,10,30,50,70], val = 25
Output: [40,20,60,10,30,50,70,null,null,25]
```

### Example 3

```text
Input: root = [4,2,7,1,3,null,null,null,null,null,null], val = 5
Output: [4,2,7,1,3,5]
```

## References

- LeetCode problem and editorial links
