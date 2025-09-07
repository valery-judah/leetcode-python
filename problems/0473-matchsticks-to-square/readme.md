# 0473. Matchsticks to Square

## Quick Facts

- URL: [Matchsticks to Square](https://leetcode.com/problems/matchsticks-to-square/)
- Function: `makesquare`
- Signature: `(matchsticks: list[int])  -> bool`
- Primary pattern: **Dynamic Programming**

## Constraints

- `1 <= matchsticks.length <= 15`
- `1 <= matchsticks[i] <= 10^8`

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
- Run: `pytest -q -k "0473"`

## Common Pitfalls

- [pitfall 1]
- [pitfall 2]
- [pitfall 3]

## Similar Problems

| Number | Difficulty | Name | LeetCode |
|---|---|---|---|
| 2482 | Medium | [Maximum Rows Covered by Columns](../2482-maximum-rows-covered-by-columns/readme.md) | [Maximum Rows Covered by Columns](https://leetcode.com/problems/maximum-rows-covered-by-columns/) |

## Examples

### Example 1

```text
Input: matchsticks = [1,1,2,2,2]
Output: true
Explanation: You can form a square with length 2, one side of the square came two sticks with length 1.
```

### Example 2

```text
Input: matchsticks = [3,3,3,3,4]
Output: false
Explanation: You cannot find a way to form a square with all the matchsticks.
```

## References

- LeetCode problem and editorial links
