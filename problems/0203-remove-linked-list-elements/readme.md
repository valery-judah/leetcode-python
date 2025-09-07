# 0203. Remove Linked List Elements

## Quick Facts

- URL: [Remove Linked List Elements](https://leetcode.com/problems/remove-linked-list-elements/)
- Function: `removeElements`
- Signature: `(head: ListNode | None, val: int)  -> ListNode | None`
- Primary pattern: **Linked List**

## Constraints

- `The number of nodes in the list is in the range [0, 10^4].`
- `1 <= Node.val <= 50`
- `0 <= val <= 50`

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
- Run: `pytest -q -k "0203"`

## Common Pitfalls

- [pitfall 1]
- [pitfall 2]
- [pitfall 3]

## Similar Problems

| Number | Difficulty | Name | LeetCode |
|---|---|---|---|
| 0027 | Easy | [Remove Element](../0027-remove-element/readme.md) | [Remove Element](https://leetcode.com/problems/remove-element/) |
| 0237 | Medium | [Delete Node in a Linked List](../0237-delete-node-in-a-linked-list/readme.md) | [Delete Node in a Linked List](https://leetcode.com/problems/delete-node-in-a-linked-list/) |
| 2216 | Medium | [Delete the Middle Node of a Linked List](../2216-delete-the-middle-node-of-a-linked-list/readme.md) | [Delete the Middle Node of a Linked List](https://leetcode.com/problems/delete-the-middle-node-of-a-linked-list/) |
| 3501 | Medium | [Delete Nodes From Linked List Present in Array](../3501-delete-nodes-from-linked-list-present-in-array/readme.md) | [Delete Nodes From Linked List Present in Array](https://leetcode.com/problems/delete-nodes-from-linked-list-present-in-array/) |
| 3263 | Easy | [Convert Doubly Linked List to Array I](../3263-convert-doubly-linked-list-to-array-i/readme.md) | [Convert Doubly Linked List to Array I](https://leetcode.com/problems/convert-doubly-linked-list-to-array-i/) |
| 3294 | Medium | [Convert Doubly Linked List to Array II](../3294-convert-doubly-linked-list-to-array-ii/readme.md) | [Convert Doubly Linked List to Array II](https://leetcode.com/problems/convert-doubly-linked-list-to-array-ii/) |

## Examples

### Example 1

```text
Input: head = [1,2,6,3,4,5,6], val = 6
Output: [1,2,3,4,5]
```

### Example 2

```text
Input: head = [], val = 1
Output: []
```

### Example 3

```text
Input: head = [7,7,7,7], val = 7
Output: []
```

## References

- LeetCode problem and editorial links
