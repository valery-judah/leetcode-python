# 1056. Confusing Number

## Quick Facts

- URL: [Confusing Number](https://leetcode.com/problems/confusing-number/)
- Function: `confusingNumber`
- Signature: `(n: int)  -> bool`
- Primary pattern: **Math**

## Constraints

- `0 <= n <= 10^9`

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
- Run: `pytest -q -k "1056"`

## Common Pitfalls

- [pitfall 1]
- [pitfall 2]
- [pitfall 3]

## Similar Problems

| Number | Difficulty | Name                                                               | LeetCode                                                                        |
| ------ | ---------- | ------------------------------------------------------------------ | ------------------------------------------------------------------------------- |
| 0246   | Easy       | [Strobogrammatic Number](../0246-strobogrammatic-number/readme.md) | [Strobogrammatic Number](https://leetcode.com/problems/strobogrammatic-number/) |
| 1088   | Hard       | [Confusing Number II](../1088-confusing-number-ii/readme.md)       | [Confusing Number II](https://leetcode.com/problems/confusing-number-ii/)       |

## Examples

### Example 1

```text
Input: n = 6
Output: true
Explanation: We get 9 after rotating 6, 9 is a valid number, and 9 != 6.
```

### Example 2

```text
Input: n = 89
Output: true
Explanation: We get 68 after rotating 89, 68 is a valid number and 68 != 89.
```

### Example 3

```text
Input: n = 11
Output: false
Explanation: We get 11 after rotating 11, 11 is a valid number but the value remains the same, thus 11 is not a confusing number
```

## References

- LeetCode problem and editorial links
