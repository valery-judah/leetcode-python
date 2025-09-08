# 0338. Counting Bits

## Quick Facts

- URL: [Counting Bits](https://leetcode.com/problems/counting-bits/)
- Function: `countBits`
- Signature: `(n: int)  -> list[int]`
- Primary pattern: **Dynamic Programming**

## Constraints

- `0 <= n <= 10^5`

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
- Run: `pytest -q -k "0338"`

## Common Pitfalls

- [pitfall 1]
- [pitfall 2]
- [pitfall 3]

## Similar Problems

| Number | Difficulty | Name | LeetCode |
|---|---|---|---|
| 0191 | Easy | [Number of 1 Bits](../0191-number-of-1-bits/readme.md) | [Number of 1 Bits](https://leetcode.com/problems/number-of-1-bits/) |
| 2859 | Easy | [Sum of Values at Indices With K Set Bits](../2859-sum-of-values-at-indices-with-k-set-bits/readme.md) | [Sum of Values at Indices With K Set Bits](https://leetcode.com/problems/sum-of-values-at-indices-with-k-set-bits/) |
| 2917 | Easy | [Find the K-or of an Array](../2917-find-the-k-or-of-an-array/readme.md) | [Find the K-or of an Array](https://leetcode.com/problems/find-the-k-or-of-an-array/) |

## Examples

### Example 1

```text
Input: n = 2
Output: [0,1,1]
Explanation:
0 --> 0
1 --> 1
2 --> 10
```

### Example 2

```text
Input: n = 5
Output: [0,1,1,2,1,2]
Explanation:
0 --> 0
1 --> 1
2 --> 10
3 --> 11
4 --> 100
5 --> 101
```

## References

- LeetCode problem and editorial links
