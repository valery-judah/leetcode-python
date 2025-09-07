# 0002. Add Two Numbers

## Quick Facts

- URL: [Add Two Numbers](https://leetcode.com/problems/add-two-numbers/)
- Function: `addTwoNumbers`
- Signature: `(l1: ListNode | None, l2: ListNode | None)  -> ListNode | None`
- Primary pattern: **Linked List**

## Constraints

- `The number of nodes in each linked list is in the range [1, 100].`
- `0 <= Node.val <= 9`
- `It is guaranteed that the list represents a number that does not have leading zeros.`

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
- Run: `pytest -q -k "0002"`

## Common Pitfalls

- [pitfall 1]
- [pitfall 2]
- [pitfall 3]

## Similar Problems

| Number | Difficulty | Name | LeetCode |
|---|---|---|---|
| 0043 | Medium | [Multiply Strings](../0043-multiply-strings/readme.md) | [Multiply Strings](https://leetcode.com/problems/multiply-strings/) |
| 0067 | Easy | [Add Binary](../0067-add-binary/readme.md) | [Add Binary](https://leetcode.com/problems/add-binary/) |
| 0371 | Medium | [Sum of Two Integers](../0371-sum-of-two-integers/readme.md) | [Sum of Two Integers](https://leetcode.com/problems/sum-of-two-integers/) |
| 0415 | Easy | [Add Strings](../0415-add-strings/readme.md) | [Add Strings](https://leetcode.com/problems/add-strings/) |
| 0445 | Medium | [Add Two Numbers II](../0445-add-two-numbers-ii/readme.md) | [Add Two Numbers II](https://leetcode.com/problems/add-two-numbers-ii/) |
| 0989 | Easy | [Add to Array-Form of Integer](../0989-add-to-array-form-of-integer/readme.md) | [Add to Array-Form of Integer](https://leetcode.com/problems/add-to-array-form-of-integer/) |
| 1634 | Medium | [Add Two Polynomials Represented as Linked Lists](../1634-add-two-polynomials-represented-as-linked-lists/readme.md) | [Add Two Polynomials Represented as Linked Lists](https://leetcode.com/problems/add-two-polynomials-represented-as-linked-lists/) |
| 2816 | Medium | [Double a Number Represented as a Linked List](../2816-double-a-number-represented-as-a-linked-list/readme.md) | [Double a Number Represented as a Linked List](https://leetcode.com/problems/double-a-number-represented-as-a-linked-list/) |

## Examples

### Example 1

```text
Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.
```

### Example 2

```text
Input: l1 = [0], l2 = [0]
Output: [0]
```

### Example 3

```text
Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]
```

## References

- LeetCode problem and editorial links
