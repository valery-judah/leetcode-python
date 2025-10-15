# 0069. Sqrt(x)

## Quick Facts

- URL: [Sqrt(x)](https://leetcode.com/problems/sqrtx/)
- Function: `mySqrt`
- Signature: `(x: int)  -> int`
- Primary pattern: **Binary Search**

## Constraints

- `0 <= x <= 2^31 - 1`

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
- Run: `pytest -q -k "0069"`

## Common Pitfalls

- [pitfall 1]
- [pitfall 2]
- [pitfall 3]

## Similar Problems

| Number | Difficulty | Name                                                           | LeetCode                                                                    |
| ------ | ---------- | -------------------------------------------------------------- | --------------------------------------------------------------------------- |
| 0050   | Medium     | [Pow(x, n)](../0050-powx-n/readme.md)                          | [Pow(x, n)](https://leetcode.com/problems/powx-n/)                          |
| 0367   | Easy       | [Valid Perfect Square](../0367-valid-perfect-square/readme.md) | [Valid Perfect Square](https://leetcode.com/problems/valid-perfect-square/) |

## Examples

### Example 1

```text
Input: x = 4
Output: 2
Explanation: The square root of 4 is 2, so we return 2.
```

### Example 2

```text
Input: x = 8
Output: 2
Explanation: The square root of 8 is 2.82842..., and since we round it down to the nearest integer, 2 is returned.
```

## References

- LeetCode problem and editorial links
