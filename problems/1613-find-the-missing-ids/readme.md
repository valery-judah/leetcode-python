# 1613. Find the Missing IDs

## Quick Facts

- URL: [Find the Missing IDs](https://leetcode.com/problems/find-the-missing-ids/)
- Function: `find_missing_ids`
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
- Run: `pytest -q -k "1613"`

## Common Pitfalls

- [pitfall 1]
- [pitfall 2]
- [pitfall 3]

## Similar Problems

| Number | Difficulty | Name | LeetCode |
|---|---|---|---|
| 1225 | Hard | [Report Contiguous Dates](../1225-report-contiguous-dates/readme.md) | [Report Contiguous Dates](https://leetcode.com/problems/report-contiguous-dates/) |
| 1285 | Medium | [Find the Start and End Number of Continuous Ranges](../1285-find-the-start-and-end-number-of-continuous-ranges/readme.md) | [Find the Start and End Number of Continuous Ranges](https://leetcode.com/problems/find-the-start-and-end-number-of-continuous-ranges/) |
| 1336 | Hard | [Number of Transactions per Visit](../1336-number-of-transactions-per-visit/readme.md) | [Number of Transactions per Visit](https://leetcode.com/problems/number-of-transactions-per-visit/) |

## Examples

### Example 1

```text
+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| customer_id   | int     |
| customer_name | varchar |
+---------------+---------+
customer_id is the column with unique values for this table.
Each row of this table contains the name and the id customer.
```

### Example 2

```text
Input: 
Customers table:
+-------------+---------------+
| customer_id | customer_name |
+-------------+---------------+
| 1           | Alice         |
| 4           | Bob           |
| 5           | Charlie       |
+-------------+---------------+
Output: 
+-----+
| ids |
+-----+
| 2   |
| 3   |
+-----+
Explanation: 
The maximum customer_id present in the table is 5, so in the range [1,5], IDs 2 and 3 are missing from the table.
```

## References

- LeetCode problem and editorial links
