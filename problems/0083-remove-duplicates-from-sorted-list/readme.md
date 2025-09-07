# 0083. Remove Duplicates from Sorted List

## Quick Facts

- URL: [Remove Duplicates from Sorted List](https://leetcode.com/problems/remove-duplicates-from-sorted-list/)
- Function: `deleteDuplicates`
- Signature: `(head: ListNode | None)  -> ListNode | None`
- Primary pattern: **Linked List**

## Constraints

- `The number of nodes in the list is in the range [0, 300].`
- `-100 <= Node.val <= 100`
- `The list is guaranteed to be sorted in ascending order.`

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
- Run: `pytest -q -k "0083"`

## Common Pitfalls

- [pitfall 1]
- [pitfall 2]
- [pitfall 3]

## Similar Problems

| Number | Difficulty | Name | LeetCode |
|---|---|---|---|
| 0082 | Medium | [Remove Duplicates from Sorted List II](../0082-remove-duplicates-from-sorted-list-ii/readme.md) | [Remove Duplicates from Sorted List II](https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/) |
| 1836 | Medium | [Remove Duplicates From an Unsorted Linked List](../1836-remove-duplicates-from-an-unsorted-linked-list/readme.md) | [Remove Duplicates From an Unsorted Linked List](https://leetcode.com/problems/remove-duplicates-from-an-unsorted-linked-list/) |

## Examples

### Example 1

```text
Input: head = [1,1,2]
Output: [1,2]
```

### Example 2

```text
Input: head = [1,1,2,3,3]
Output: [1,2,3]
```

## References

- LeetCode problem and editorial links
