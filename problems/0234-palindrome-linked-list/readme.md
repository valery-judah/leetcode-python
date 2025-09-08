# 0234. Palindrome Linked List

## Quick Facts

- URL: [Palindrome Linked List](https://leetcode.com/problems/palindrome-linked-list/)
- Function: `isPalindrome`
- Signature: `(head: ListNode | None)  -> bool`
- Primary pattern: **Two Pointers**

## Constraints

- `The number of nodes in the list is in the range [1, 10^5].`
- `0 <= Node.val <= 9`

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
- Run: `pytest -q -k "0234"`

## Common Pitfalls

- [pitfall 1]
- [pitfall 2]
- [pitfall 3]

## Similar Problems

| Number | Difficulty | Name | LeetCode |
|---|---|---|---|
| 0009 | Easy | [Palindrome Number](../0009-palindrome-number/readme.md) | [Palindrome Number](https://leetcode.com/problems/palindrome-number/) |
| 0125 | Easy | [Valid Palindrome](../0125-valid-palindrome/readme.md) | [Valid Palindrome](https://leetcode.com/problems/valid-palindrome/) |
| 0206 | Easy | [Reverse Linked List](../0206-reverse-linked-list/readme.md) | [Reverse Linked List](https://leetcode.com/problems/reverse-linked-list/) |
| 2130 | Medium | [Maximum Twin Sum of a Linked List](../2130-maximum-twin-sum-of-a-linked-list/readme.md) | [Maximum Twin Sum of a Linked List](https://leetcode.com/problems/maximum-twin-sum-of-a-linked-list/) |

## Examples

### Example 1

```text
Input: head = [1,2,2,1]
Output: true
```

### Example 2

```text
Input: head = [1,2]
Output: false
```

## References

- LeetCode problem and editorial links
