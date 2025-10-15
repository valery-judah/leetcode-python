# 1405. Longest Happy String

## Quick Facts

- URL: [Longest Happy String](https://leetcode.com/problems/longest-happy-string/)
- Function: `longestDiverseString`
- Signature: `(a: int, b: int, c: int)  -> str`
- Primary pattern: **Heap (Priority Queue)**

## Constraints

- `0 <= a, b, c <= 100`
- `a + b + c > 0`

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
- Run: `pytest -q -k "1405"`

## Common Pitfalls

- [pitfall 1]
- [pitfall 2]
- [pitfall 3]

## Similar Problems

| Number | Difficulty | Name                                                     | LeetCode                                                              |
| ------ | ---------- | -------------------------------------------------------- | --------------------------------------------------------------------- |
| 0767   | Medium     | [Reorganize String](../0767-reorganize-string/readme.md) | [Reorganize String](https://leetcode.com/problems/reorganize-string/) |

## Examples

### Example 1

```text
Input: a = 1, b = 1, c = 7
Output: "ccaccbcc"
Explanation: "ccbccacc" would also be a correct answer.
```

### Example 2

```text
Input: a = 7, b = 1, c = 0
Output: "aabaa"
Explanation: It is the only correct answer in this case.
```

## References

- LeetCode problem and editorial links
