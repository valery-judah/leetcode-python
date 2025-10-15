# 1052. Grumpy Bookstore Owner

## Quick Facts

- URL: [Grumpy Bookstore Owner](https://leetcode.com/problems/grumpy-bookstore-owner/)
- Function: `maxSatisfied`
- Signature: `(customers: list[int], grumpy: list[int], minutes: int)  -> int`
- Primary pattern: **Sliding Window**

## Constraints

- `n == customers.length == grumpy.length`
- `1 <= minutes <= n <= 2 * 10^4`
- `0 <= customers[i] <= 1000`
- `grumpy[i] is either 0 or 1.`

## Problem Crux (1–2 sentences)

[state what must be detected/computed and key bound]

## Clarifying Questions (for interview)

- [input domain? ranges?]
- [edge-case semantics?]
- [any pair vs first pair? ties?]

## Reasoning Flow (notes-only)

[outline the logical steps that lead to the chosen approach]

## Approach Options

| #   | Idea           | When to use | Correctness invariant | Time       | Space |
| --- | -------------- | ----------- | --------------------- | ---------- | ----- |
| A   | [primary idea] | [scenario]  | [invariant]           | O(n)       | O(n)  |
| B   | [alternative]  | [scenario]  | [invariant]           | O(n log n) | O(1)  |
| C   | [reject]       | [why not]   | [violated invariant]  | -          | -     |

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
- Run: `pytest -q -k "1052"`

## Common Pitfalls

- [pitfall 1]
- [pitfall 2]
- [pitfall 3]

## Similar Problems

None

## Examples

None

## References

- LeetCode problem and editorial links
