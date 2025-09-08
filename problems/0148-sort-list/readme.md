# 0148. Insertion Sort List

## Quick Facts

- URL: [Insertion Sort List](https://leetcode.com/problems/insertion-sort-list/)
- Function: `insertionSortList`
- Signature: `(head: ListNode | None)  -> ListNode | None`
- Primary pattern: **Sorting**

## Constraints

- `The number of nodes in the list is in the range [1, 5000].`
- `-5000 <= Node.val <= 5000`

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
- Run: `pytest -q -k "0148"`

## Common Pitfalls

- [pitfall 1]
- [pitfall 2]
- [pitfall 3]

## Similar Problems

| Number | Difficulty | Name | LeetCode |
|---|---|---|---|
| 0147 | Medium | [Sort List](../0147-sort-list/readme.md) | [Sort List](https://leetcode.com/problems/sort-list/) |
| 0708 | Medium | [Insert into a Sorted Circular Linked List](../0708-insert-into-a-sorted-circular-linked-list/readme.md) | [Insert into a Sorted Circular Linked List](https://leetcode.com/problems/insert-into-a-sorted-circular-linked-list/) |

## Examples

### Example 1

```text
Input: head = [4,2,1,3]
Output: [1,2,3,4]
```

### Example 2

```text
Input: head = [-1,5,3,4,0]
Output: [-1,0,3,4,5]
```

## References

- LeetCode problem and editorial links
