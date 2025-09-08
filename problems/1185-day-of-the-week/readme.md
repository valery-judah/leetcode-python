# 1185. Day of the Week

## Quick Facts

- URL: [Day of the Week](https://leetcode.com/problems/day-of-the-week/)
- Function: `dayOfTheWeek`
- Signature: `(day: int, month: int, year: int)  -> str`
- Primary pattern: **Math**

## Constraints

- `The given dates are valid dates between the years 1971 and 2100.`

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
- Run: `pytest -q -k "1185"`

## Common Pitfalls

- [pitfall 1]
- [pitfall 2]
- [pitfall 3]

## Similar Problems

None

## Examples

### Example 1

```text
Input: day = 31, month = 8, year = 2019
Output: "Saturday"
```

### Example 2

```text
Input: day = 18, month = 7, year = 1999
Output: "Sunday"
```

### Example 3

```text
Input: day = 15, month = 8, year = 1993
Output: "Sunday"
```

## References

- LeetCode problem and editorial links
