# 0019. Remove Nth Node From End of List

## Quick Facts

- URL: [Remove Nth Node From End of List](https://leetcode.com/problems/remove-nth-node-from-end-of-list/)
- Function: `removeNthFromEnd`
- Signature: `(head: ListNode | None, n: int)  -> ListNode | None`
- Primary pattern: **Two Pointers**

## Constraints

- `The number of nodes in the list is sz.`
- `1 <= sz <= 30`
- `0 <= Node.val <= 100`
- `1 <= n <= sz`

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
- Run: `pytest -q -k "0019"`

## Common Pitfalls

- [pitfall 1]
- [pitfall 2]
- [pitfall 3]

## Similar Problems

| Number | Difficulty | Name | LeetCode |
|---|---|---|---|
| 0528 | Medium | [Swapping Nodes in a Linked List](../0528-swapping-nodes-in-a-linked-list/readme.md) | [Swapping Nodes in a Linked List](https://leetcode.com/problems/swapping-nodes-in-a-linked-list/) |
| 1618 | Easy | [Delete N Nodes After M Nodes of a Linked List](../1618-delete-n-nodes-after-m-nodes-of-a-linked-list/readme.md) | [Delete N Nodes After M Nodes of a Linked List](https://leetcode.com/problems/delete-n-nodes-after-m-nodes-of-a-linked-list/) |
| 2216 | Medium | [Delete the Middle Node of a Linked List](../2216-delete-the-middle-node-of-a-linked-list/readme.md) | [Delete the Middle Node of a Linked List](https://leetcode.com/problems/delete-the-middle-node-of-a-linked-list/) |

## Examples

### Example 1

```text
Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]
```

### Example 2

```text
Input: head = [1], n = 1
Output: []
```

### Example 3

```text
Input: head = [1,2], n = 1
Output: [1]
```

## References

- LeetCode problem and editorial links
