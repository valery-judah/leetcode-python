# 0052. N-Queens II

## Quick Facts

- URL: [N-Queens II](https://leetcode.com/problems/n-queens-ii/)
- Function: `totalNQueens`
- Signature: `(n: int)  -> int`
- Primary pattern: **Backtracking**

## Constraints

- `1 <= n <= 9`

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
- Run: `pytest -q -k "0052"`

## Common Pitfalls

- [pitfall 1]
- [pitfall 2]
- [pitfall 3]

## Similar Problems

| Number | Difficulty | Name                                   | LeetCode                                            |
| ------ | ---------- | -------------------------------------- | --------------------------------------------------- |
| 0051   | Hard       | [N-Queens](../0051-n-queens/readme.md) | [N-Queens](https://leetcode.com/problems/n-queens/) |

## Examples

### Example 1

```text
Input: n = 4
Output: 2
Explanation: There are two distinct solutions to the 4-queens puzzle as shown.
```

### Example 2

```text
Input: n = 1
Output: 1
```

## References

- LeetCode problem and editorial links
