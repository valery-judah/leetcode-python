# 0247. Strobogrammatic Number II

## Quick Facts

- URL: [Strobogrammatic Number II](https://leetcode.com/problems/strobogrammatic-number-ii/)
- Function: `findStrobogrammatic`
- Signature: `(n: int)  -> list[str]`
- Primary pattern: **Array**

## Constraints

- `1 <= n <= 14`

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
- Run: `pytest -q -k "0247"`

## Common Pitfalls

- [pitfall 1]
- [pitfall 2]
- [pitfall 3]

## Similar Problems

| Number | Difficulty | Name                                                                       | LeetCode                                                                                |
| ------ | ---------- | -------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- |
| 0246   | Easy       | [Strobogrammatic Number](../0246-strobogrammatic-number/readme.md)         | [Strobogrammatic Number](https://leetcode.com/problems/strobogrammatic-number/)         |
| 0248   | Hard       | [Strobogrammatic Number III](../0248-strobogrammatic-number-iii/readme.md) | [Strobogrammatic Number III](https://leetcode.com/problems/strobogrammatic-number-iii/) |
| 2081   | Hard       | [Sum of k-Mirror Numbers](../2081-sum-of-k-mirror-numbers/readme.md)       | [Sum of k-Mirror Numbers](https://leetcode.com/problems/sum-of-k-mirror-numbers/)       |

## Examples

### Example 1

```text
Input: n = 2
Output: ["11","69","88","96"]
```

### Example 2

```text
Input: n = 1
Output: ["0","1","8"]
```

## References

- LeetCode problem and editorial links
