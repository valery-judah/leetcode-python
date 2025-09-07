# 0369. Plus One Linked List

## Quick Facts

- URL: [Plus One Linked List](https://leetcode.com/problems/plus-one-linked-list/)
- Function: `plusOne`
- Signature: `(head: ListNode | None)  -> ListNode | None`
- Primary pattern: **Linked List**

## Constraints

- `The number of nodes in the linked list is in the range [1, 100].`
- `0 <= Node.val <= 9`
- `The number represented by the linked list does not contain leading zeros except for the zero itself.`

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
- Run: `pytest -q -k "0369"`

## Common Pitfalls

- [pitfall 1]
- [pitfall 2]
- [pitfall 3]

## Similar Problems

| Number | Difficulty | Name | LeetCode |
|---|---|---|---|
| 0066 | Easy | [Plus One](../0066-plus-one/readme.md) | [Plus One](https://leetcode.com/problems/plus-one/) |
| 2816 | Medium | [Double a Number Represented as a Linked List](../2816-double-a-number-represented-as-a-linked-list/readme.md) | [Double a Number Represented as a Linked List](https://leetcode.com/problems/double-a-number-represented-as-a-linked-list/) |

## Examples

### Example 1

```text
Input: head = [1,2,3]
Output: [1,2,4]
```

### Example 2

```text
Input: head = [0]
Output: [1]
```

## References

- LeetCode problem and editorial links
