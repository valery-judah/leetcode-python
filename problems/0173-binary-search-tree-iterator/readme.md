# 0173. Binary Search Tree Iterator

## Quick Facts

- URL: [Binary Search Tree Iterator](https://leetcode.com/problems/binary-search-tree-iterator/)
- Function: \`\`
- Signature: `(inputs: list[int], inputs: list[int])  -> list[int]`
- Primary pattern: **Tree**

## Constraints

- `The number of nodes in the tree is in the range [1, 10^5].`
- `0 <= Node.val <= 10^6`
- `At most 10^5 calls will be made to hasNext, and next.`

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
- Run: `pytest -q -k "0173"`

## Common Pitfalls

- [pitfall 1]
- [pitfall 2]
- [pitfall 3]

## Similar Problems

| Number | Difficulty | Name                                                                               | LeetCode                                                                                        |
| ------ | ---------- | ---------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- |
| 0094   | Easy       | [Binary Tree Inorder Traversal](../0094-binary-tree-inorder-traversal/readme.md)   | [Binary Tree Inorder Traversal](https://leetcode.com/problems/binary-tree-inorder-traversal/)   |
| 0251   | Medium     | [Flatten 2D Vector](../0251-flatten-2d-vector/readme.md)                           | [Flatten 2D Vector](https://leetcode.com/problems/flatten-2d-vector/)                           |
| 0281   | Medium     | [Zigzag Iterator](../0281-zigzag-iterator/readme.md)                               | [Zigzag Iterator](https://leetcode.com/problems/zigzag-iterator/)                               |
| 0284   | Medium     | [Peeking Iterator](../0284-peeking-iterator/readme.md)                             | [Peeking Iterator](https://leetcode.com/problems/peeking-iterator/)                             |
| 0285   | Medium     | [Inorder Successor in BST](../0285-inorder-successor-in-bst/readme.md)             | [Inorder Successor in BST](https://leetcode.com/problems/inorder-successor-in-bst/)             |
| 1586   | Medium     | [Binary Search Tree Iterator II](../1586-binary-search-tree-iterator-ii/readme.md) | [Binary Search Tree Iterator II](https://leetcode.com/problems/binary-search-tree-iterator-ii/) |

## Examples

### Example 1

```text
Input
["BSTIterator", "next", "next", "hasNext", "next", "hasNext", "next", "hasNext", "next", "hasNext"]
[[[7, 3, 15, null, null, 9, 20]], [], [], [], [], [], [], [], [], []]
Output
[null, 3, 7, true, 9, true, 15, true, 20, false]

Explanation
BSTIterator bSTIterator = new BSTIterator([7, 3, 15, null, null, 9, 20]);
bSTIterator.next();    // return 3
bSTIterator.next();    // return 7
bSTIterator.hasNext(); // return True
bSTIterator.next();    // return 9
bSTIterator.hasNext(); // return True
bSTIterator.next();    // return 15
bSTIterator.hasNext(); // return True
bSTIterator.next();    // return 20
bSTIterator.hasNext(); // return False
```

## References

- LeetCode problem and editorial links
