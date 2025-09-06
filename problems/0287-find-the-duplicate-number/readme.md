# 0287. Find the Duplicate Number

## Quick Facts

- URL: https://leetcode.com/problems/find-the-duplicate-number/
- Signature: `nums: list[int]` → `int`
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
- Run: `pytest -q -k "0287"`

## Common Pitfalls

- [pitfall 1]
- [pitfall 2]
- [pitfall 3]

## Similar Problems

| Number | Difficulty | Name | LeetCode |
|---|---|---|---|
| 0041 | Hard | [First Missing Positive](../0041-first-missing-positive/readme.md) | [link](https://leetcode.com/problems/first-missing-positive/) |
| 0136 | Easy | [Single Number](../0136-single-number/readme.md) | [link](https://leetcode.com/problems/single-number/) |
| 0142 | Medium | [Linked List Cycle II](../0142-linked-list-cycle-ii/readme.md) | [link](https://leetcode.com/problems/linked-list-cycle-ii/) |
| 0268 | Easy | [Missing Number](../0268-missing-number/readme.md) | [link](https://leetcode.com/problems/missing-number/) |
| 0645 | Easy | [Set Mismatch](../0645-set-mismatch/readme.md) | [link](https://leetcode.com/problems/set-mismatch/) |

## References

- LeetCode problem and editorial links

## Changelog

- 2025-09-06T13:33:55Z: Created scaffold.
