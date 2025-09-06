# 0206. Reverse Linked List

## Quick Facts

- URL: https://leetcode.com/problems/reverse-linked-list/
- Signature: `head: ListNode | None` → `ListNode | None`
- Constraints: [paste from LC]
- Primary pattern: [write primary pattern]

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
- Run: `pytest -q -k "0206"`

## Common Pitfalls

- [pitfall 1]
- [pitfall 2]
- [pitfall 3]

## Similar Problems

| Number | Difficulty | Name | LeetCode |
|---|---|---|---|
| 0092 | Medium | [Reverse Linked List II](../0092-reverse-linked-list-ii/readme.md) | [link](https://leetcode.com/problems/reverse-linked-list-ii/) |
| 0156 | Medium | [Binary Tree Upside Down](../0156-binary-tree-upside-down/readme.md) | [link](https://leetcode.com/problems/binary-tree-upside-down/) |
| 0234 | Easy | [Palindrome Linked List](../0234-palindrome-linked-list/readme.md) | [link](https://leetcode.com/problems/palindrome-linked-list/) |
| 2074 | Medium | [Reverse Nodes in Even Length Groups](../2074-reverse-nodes-in-even-length-groups/readme.md) | [link](https://leetcode.com/problems/reverse-nodes-in-even-length-groups/) |
| 2130 | Medium | [Maximum Twin Sum of a Linked List](../2130-maximum-twin-sum-of-a-linked-list/readme.md) | [link](https://leetcode.com/problems/maximum-twin-sum-of-a-linked-list/) |
| 2487 | Medium | [Remove Nodes From Linked List](../2487-remove-nodes-from-linked-list/readme.md) | [link](https://leetcode.com/problems/remove-nodes-from-linked-list/) |
| 2807 | Medium | [Insert Greatest Common Divisors in Linked List](../2807-insert-greatest-common-divisors-in-linked-list/readme.md) | [link](https://leetcode.com/problems/insert-greatest-common-divisors-in-linked-list/) |

## References

- LeetCode problem and editorial links

## Changelog

- 2025-09-06T13:33:52Z: Created scaffold.
