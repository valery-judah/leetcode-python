# 0765. Couples Holding Hands

## Quick Facts

- URL: [Couples Holding Hands](https://leetcode.com/problems/couples-holding-hands/)
- Function: `minSwapsCouples`
- Signature: `(row: list[int])  -> int`
- Primary pattern: **Graph**

## Constraints

- `2n == row.length`
- `2 <= n <= 30`
- `n is even.`
- `0 <= row[i] < 2n`
- `All the elements of row are unique.`

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
- Run: `pytest -q -k "0765"`

## Common Pitfalls

- [pitfall 1]
- [pitfall 2]
- [pitfall 3]

## Similar Problems

| Number | Difficulty | Name | LeetCode |
|---|---|---|---|
| 0041 | Hard | [First Missing Positive](../0041-first-missing-positive/readme.md) | [First Missing Positive](https://leetcode.com/problems/first-missing-positive/) |
| 0268 | Easy | [Missing Number](../0268-missing-number/readme.md) | [Missing Number](https://leetcode.com/problems/missing-number/) |
| 0854 | Hard | [K-Similar Strings](../0854-k-similar-strings/readme.md) | [K-Similar Strings](https://leetcode.com/problems/k-similar-strings/) |

## Examples

### Example 1

```text
Input: row = [0,2,1,3]
Output: 1
Explanation: We only need to swap the second (row[1]) and third (row[2]) person.
```

### Example 2

```text
Input: row = [3,2,0,1]
Output: 0
Explanation: All couples are already seated side by side.
```

## References

- LeetCode problem and editorial links
