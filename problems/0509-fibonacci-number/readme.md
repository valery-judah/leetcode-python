# 0509. Fibonacci Number

## Quick Facts

- URL: [Fibonacci Number](https://leetcode.com/problems/fibonacci-number/)
- Function: `fib`
- Signature: `(n: int)  -> int`
- Primary pattern: **Dynamic Programming**

## Constraints

- `0 <= n <= 30`

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
- Run: `pytest -q -k "0509"`

## Common Pitfalls

- [pitfall 1]
- [pitfall 2]
- [pitfall 3]

## Similar Problems

| Number | Difficulty | Name                                                                                                 | LeetCode                                                                                                          |
| ------ | ---------- | ---------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------- |
| 0070   | Easy       | [Climbing Stairs](../0070-climbing-stairs/readme.md)                                                 | [Climbing Stairs](https://leetcode.com/problems/climbing-stairs/)                                                 |
| 0842   | Medium     | [Split Array into Fibonacci Sequence](../0842-split-array-into-fibonacci-sequence/readme.md)         | [Split Array into Fibonacci Sequence](https://leetcode.com/problems/split-array-into-fibonacci-sequence/)         |
| 0873   | Medium     | [Length of Longest Fibonacci Subsequence](../0873-length-of-longest-fibonacci-subsequence/readme.md) | [Length of Longest Fibonacci Subsequence](https://leetcode.com/problems/length-of-longest-fibonacci-subsequence/) |
| 1137   | Easy       | [N-th Tribonacci Number](../1137-n-th-tribonacci-number/readme.md)                                   | [N-th Tribonacci Number](https://leetcode.com/problems/n-th-tribonacci-number/)                                   |

## Examples

### Example 1

```text
F(0) = 0, F(1) = 1
F(n) = F(n - 1) + F(n - 2), for n > 1.
```

### Example 2

```text
Input: n = 2
Output: 1
Explanation: F(2) = F(1) + F(0) = 1 + 0 = 1.
```

### Example 3

```text
Input: n = 3
Output: 2
Explanation: F(3) = F(2) + F(1) = 1 + 1 = 2.
```

### Example 4

```text
Input: n = 4
Output: 3
Explanation: F(4) = F(3) + F(2) = 2 + 1 = 3.
```

## References

- LeetCode problem and editorial links
