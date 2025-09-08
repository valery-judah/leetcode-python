# 0430. Flatten a Multilevel Doubly Linked List

## Quick Facts

- URL: [Flatten a Multilevel Doubly Linked List](https://leetcode.com/problems/flatten-a-multilevel-doubly-linked-list/)
- Function: `flatten`
- Signature: `(head: ListNode | None)  -> ListNode | None`
- Primary pattern: **Linked List**

## Constraints

- `The number of Nodes will not exceed 1000.`
- `1 <= Node.val <= 10^5`

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
- Run: `pytest -q -k "0430"`

## Common Pitfalls

- [pitfall 1]
- [pitfall 2]
- [pitfall 3]

## Similar Problems

| Number | Difficulty | Name | LeetCode |
|---|---|---|---|
| 0114 | Medium | [Flatten Binary Tree to Linked List](../0114-flatten-binary-tree-to-linked-list/readme.md) | [Flatten Binary Tree to Linked List](https://leetcode.com/problems/flatten-binary-tree-to-linked-list/) |
| 1660 | Medium | [Correct a Binary Tree](../1660-correct-a-binary-tree/readme.md) | [Correct a Binary Tree](https://leetcode.com/problems/correct-a-binary-tree/) |

## Examples

### Example 1

```text
Input: head = [1,2,3,4,5,6,null,null,null,7,8,9,10,null,null,11,12]
Output: [1,2,3,7,8,11,12,9,10,4,5,6]
Explanation: The multilevel linked list in the input is shown.
After flattening the multilevel linked list it becomes:
```

### Example 2

```text
Input: head = [1,2,null,3]
Output: [1,3,2]
Explanation: The multilevel linked list in the input is shown.
After flattening the multilevel linked list it becomes:
```

### Example 3

```text
Input: head = []
Output: []
Explanation: There could be empty list in the input.
```

### Example 4

```text
1---2---3---4---5---6--NULL
         |
         7---8---9---10--NULL
             |
             11--12--NULL
```

### Example 5

```text
[1,2,3,4,5,6,null]
[7,8,9,10,null]
[11,12,null]
```

### Example 6

```text
[1,    2,    3, 4, 5, 6, null]
             |
[null, null, 7,    8, 9, 10, null]
                   |
[            null, 11, 12, null]
```

### Example 7

```text
[1,2,3,4,5,6,null,null,null,7,8,9,10,null,null,11,12]
```

## References

- LeetCode problem and editorial links
