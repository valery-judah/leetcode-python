# 1019. Next Greater Node In Linked List

## Quick Facts

- URL: [Next Greater Node In Linked List](https://leetcode.com/problems/next-greater-node-in-linked-list/)
- Function: `nextLargerNodes`
- Signature: `(head: ListNode | None)  -> list[int]`
- Primary pattern: **Stack**

## Constraints

- `The number of nodes in the list is n.`
- `1 <= n <= 10^4`
- `1 <= Node.val <= 10^9`

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
- Run: `pytest -q -k "1019"`

## Common Pitfalls

- [pitfall 1]
- [pitfall 2]
- [pitfall 3]

## Similar Problems

None

## Examples

### Example 1

```text
Input: head = [2,1,5]
Output: [5,5,0]
```

### Example 2

```text
Input: head = [2,7,4,3,5]
Output: [7,0,5,5,0]
```

## References

- LeetCode problem and editorial links
