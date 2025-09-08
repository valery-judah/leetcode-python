# 0092. Reverse Linked List II

## Quick Facts

- URL: [Reverse Linked List II](https://leetcode.com/problems/reverse-linked-list-ii/)
- Function: `reverseBetween`
- Signature: `(head: ListNode | None, left: int, right: int)  -> ListNode | None`
- Primary pattern: **Linked List**

## Constraints

- `The number of nodes in the list is n.`
- `1 <= n <= 500`
- `-500 <= Node.val <= 500`
- `1 <= left <= right <= n`

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
- Run: `pytest -q -k "0092"`

## Common Pitfalls

- [pitfall 1]
- [pitfall 2]
- [pitfall 3]

## Similar Problems

| Number | Difficulty | Name | LeetCode |
|---|---|---|---|
| 0206 | Easy | [Reverse Linked List](../0206-reverse-linked-list/readme.md) | [Reverse Linked List](https://leetcode.com/problems/reverse-linked-list/) |

## Examples

### Example 1

```text
Input: head = [1,2,3,4,5], left = 2, right = 4
Output: [1,4,3,2,5]
```

### Example 2

```text
Input: head = [5], left = 1, right = 1
Output: [5]
```

## References

- LeetCode problem and editorial links
