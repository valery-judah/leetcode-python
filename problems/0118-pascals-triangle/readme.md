# 0118. Pascal's Triangle

## Quick Facts

- URL: [Pascal's Triangle](https://leetcode.com/problems/pascals-triangle/)
- Function: `generate`
- Signature: `(numRows: int)  -> list[list[int]]`
- Primary pattern: **Dynamic Programming**

## Constraints

- `1 <= numRows <= 30`

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
- Run: `pytest -q -k "0118"`

## Common Pitfalls

- [pitfall 1]
- [pitfall 2]
- [pitfall 3]

## Similar Problems

| Number | Difficulty | Name | LeetCode |
|---|---|---|---|
| 0119 | Easy | [Pascal's Triangle II](../0119-pascals-triangle-ii/readme.md) | [Pascal's Triangle II](https://leetcode.com/problems/pascals-triangle-ii/) |
| 3463 | Hard | [Check If Digits Are Equal in String After Operations II](../3463-check-if-digits-are-equal-in-string-after-operations-ii/readme.md) | [Check If Digits Are Equal in String After Operations II](https://leetcode.com/problems/check-if-digits-are-equal-in-string-after-operations-ii/) |

## Examples

### Example 1

```text
Input: numRows = 5
Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
```

### Example 2

```text
Input: numRows = 1
Output: [[1]]
```

## References

- LeetCode problem and editorial links
