# 1171. Remove Zero Sum Consecutive Nodes from Linked List

## Quick Facts

- URL: [Remove Zero Sum Consecutive Nodes from Linked List](https://leetcode.com/problems/remove-zero-sum-consecutive-nodes-from-linked-list/)
- Function: `removeZeroSumSublists`
- Signature: `(head: ListNode | None)  -> ListNode | None`
- Primary pattern: **Hash Table**

## Constraints

- `The given linked list will contain between 1 and 1000 nodes.`
- `Each node in the linked list has -1000 <= node.val <= 1000.`

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
- Run: `pytest -q -k "1171"`

## Common Pitfalls

- [pitfall 1]
- [pitfall 2]
- [pitfall 3]

## Similar Problems

| Number | Difficulty | Name | LeetCode |
|---|---|---|---|
| 1618 | Easy | [Delete N Nodes After M Nodes of a Linked List](../1618-delete-n-nodes-after-m-nodes-of-a-linked-list/readme.md) | [Delete N Nodes After M Nodes of a Linked List](https://leetcode.com/problems/delete-n-nodes-after-m-nodes-of-a-linked-list/) |

## Examples

### Example 1

```text
Input: head = [1,2,-3,3,1]
Output: [3,1]
Note: The answer [1,2,1] would also be accepted.
```

### Example 2

```text
Input: head = [1,2,3,-3,4]
Output: [1,2,4]
```

### Example 3

```text
Input: head = [1,2,3,-3,-2]
Output: [1]
```

## References

- LeetCode problem and editorial links
