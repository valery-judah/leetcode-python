# 0739. Daily Temperatures

## Quick Facts

- URL: [Daily Temperatures](https://leetcode.com/problems/daily-temperatures/)
- Function: `dailyTemperatures`
- Signature: `(temperatures: list[int])  -> list[int]`
- Primary pattern: **Stack**

## Constraints

- `1 <= temperatures.length <= 10^5`
- `30 <= temperatures[i] <= 100`

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
- Run: `pytest -q -k "0739"`

## Common Pitfalls

- [pitfall 1]
- [pitfall 2]
- [pitfall 3]

## Similar Problems

| Number | Difficulty | Name                                                               | LeetCode                                                                        |
| ------ | ---------- | ------------------------------------------------------------------ | ------------------------------------------------------------------------------- |
| 0496   | Easy       | [Next Greater Element I](../0496-next-greater-element-i/readme.md) | [Next Greater Element I](https://leetcode.com/problems/next-greater-element-i/) |
| 0901   | Medium     | [Online Stock Span](../0901-online-stock-span/readme.md)           | [Online Stock Span](https://leetcode.com/problems/online-stock-span/)           |

## Examples

### Example 1

```text
Input: temperatures = [73,74,75,71,69,72,76,73]
Output: [1,1,4,2,1,1,0,0]
```

### Example 2

```text
Input: temperatures = [30,40,50,60]
Output: [1,1,1,0]
```

### Example 3

```text
Input: temperatures = [30,60,90]
Output: [1,1,0]
```

## References

- LeetCode problem and editorial links
