# 1137. N-th Tribonacci Number

## Quick Facts

- URL: [N-th Tribonacci Number](https://leetcode.com/problems/n-th-tribonacci-number/)
- Function: `tribonacci`
- Signature: `(n: int)  -> int`
- Primary pattern: **Dynamic Programming**

## Constraints

- `0 <= n <= 37`
- `The answer is guaranteed to fit within a 32-bit integer, ie. answer <= 2^31 - 1.`

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
- Run: `pytest -q -k "1137"`

## Common Pitfalls

- [pitfall 1]
- [pitfall 2]
- [pitfall 3]

## Similar Problems

| Number | Difficulty | Name | LeetCode |
|---|---|---|---|
| 0070 | Easy | [Climbing Stairs](../0070-climbing-stairs/readme.md) | [Climbing Stairs](https://leetcode.com/problems/climbing-stairs/) |
| 0509 | Easy | [Fibonacci Number](../0509-fibonacci-number/readme.md) | [Fibonacci Number](https://leetcode.com/problems/fibonacci-number/) |

## Examples

### Example 1

```text
Input: n = 4
Output: 4
Explanation:
T_3 = 0 + 1 + 1 = 2
T_4 = 1 + 1 + 2 = 4
```

### Example 2

```text
Input: n = 25
Output: 1389537
```

## References

- LeetCode problem and editorial links
