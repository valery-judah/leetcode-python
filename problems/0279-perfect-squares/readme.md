# 0279. Perfect Squares

## Quick Facts

- URL: [Perfect Squares](https://leetcode.com/problems/perfect-squares/)
- Function: `numSquares`
- Signature: `(n: int)  -> int`
- Primary pattern: **Dynamic Programming**

## Constraints

- `1 <= n <= 10^4`

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
- Run: `pytest -q -k "0279"`

## Common Pitfalls

- [pitfall 1]
- [pitfall 2]
- [pitfall 3]

## Similar Problems

| Number | Difficulty | Name                                                                                                         | LeetCode                                                                                                                  |
| ------ | ---------- | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------- |
| 0204   | Medium     | [Count Primes](../0204-count-primes/readme.md)                                                               | [Count Primes](https://leetcode.com/problems/count-primes/)                                                               |
| 0264   | Medium     | [Ugly Number II](../0264-ugly-number-ii/readme.md)                                                           | [Ugly Number II](https://leetcode.com/problems/ugly-number-ii/)                                                           |
| 2787   | Medium     | [Ways to Express an Integer as Sum of Powers](../2787-ways-to-express-an-integer-as-sum-of-powers/readme.md) | [Ways to Express an Integer as Sum of Powers](https://leetcode.com/problems/ways-to-express-an-integer-as-sum-of-powers/) |

## Examples

### Example 1

```text
Input: n = 12
Output: 3
Explanation: 12 = 4 + 4 + 4.
```

### Example 2

```text
Input: n = 13
Output: 2
Explanation: 13 = 4 + 9.
```

## References

- LeetCode problem and editorial links
