# 1126. Active Businesses

## Quick Facts

- URL: [Active Businesses](https://leetcode.com/problems/active-businesses/)
- Function: `active_businesses`
- Signature: `()  -> object`
- Primary pattern: **Database**

## Constraints

None

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
- Run: `pytest -q -k "1126"`

## Common Pitfalls

- [pitfall 1]
- [pitfall 2]
- [pitfall 3]

## Similar Problems

None

## Examples

### Example 1

```text
+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| business_id   | int     |
| event_type    | varchar |
| occurrences   | int     |
+---------------+---------+
(business_id, event_type) is the primary key (combination of columns with unique values) of this table.
Each row in the table logs the info that an event of some type occurred at some business for a number of times.
```

### Example 2

```text
Input:
Events table:
+-------------+------------+-------------+
| business_id | event_type | occurrences |
+-------------+------------+-------------+
| 1           | reviews    | 7           |
| 3           | reviews    | 3           |
| 1           | ads        | 11          |
| 2           | ads        | 7           |
| 3           | ads        | 6           |
| 1           | page views | 3           |
| 2           | page views | 12          |
+-------------+------------+-------------+
Output:
+-------------+
| business_id |
+-------------+
| 1           |
+-------------+
Explanation:
The average activity for each event can be calculated as follows:
- 'reviews': (7+3)/2 = 5
- 'ads': (11+7+6)/3 = 8
- 'page views': (3+12)/2 = 7.5
The business with id=1 has 7 'reviews' events (more than 5) and 11 'ads' events (more than 8), so it is an active business.
```

## References

- LeetCode problem and editorial links
