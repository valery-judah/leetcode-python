# 1977. Number of Ways to Separate Numbers

## Quick Facts

- URL: [Number of Ways to Separate Numbers](https://leetcode.com/problems/number-of-ways-to-separate-numbers/)
- Function: `numberOfCombinations`
- Signature: `(num: str)  -> int`
- Primary pattern: **Dynamic Programming**

## Constraints

- `1 <= num.length <= 3500`
- `num consists of digits '0' through '9'.`

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
- Run: `pytest -q -k "1977"`

## Common Pitfalls

- [pitfall 1]
- [pitfall 2]
- [pitfall 3]

## Similar Problems

| Number | Difficulty | Name | LeetCode |
|---|---|---|---|
| 0091 | Medium | [Decode Ways](../0091-decode-ways/readme.md) | [Decode Ways](https://leetcode.com/problems/decode-ways/) |
| 0639 | Hard | [Decode Ways II](../0639-decode-ways-ii/readme.md) | [Decode Ways II](https://leetcode.com/problems/decode-ways-ii/) |
| 1416 | Hard | [Restore The Array](../1416-restore-the-array/readme.md) | [Restore The Array](https://leetcode.com/problems/restore-the-array/) |
| 2478 | Hard | [Number of Beautiful Partitions](../2478-number-of-beautiful-partitions/readme.md) | [Number of Beautiful Partitions](https://leetcode.com/problems/number-of-beautiful-partitions/) |

## Examples

### Example 1

```text
Input: num = "327"
Output: 2
Explanation: You could have written down the numbers:
3, 27
327
```

### Example 2

```text
Input: num = "094"
Output: 0
Explanation: No numbers can have leading zeros and all numbers must be positive.
```

### Example 3

```text
Input: num = "0"
Output: 0
Explanation: No numbers can have leading zeros and all numbers must be positive.
```

## References

- LeetCode problem and editorial links
