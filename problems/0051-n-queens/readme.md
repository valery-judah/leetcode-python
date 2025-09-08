# 0051. N-Queens

## Quick Facts

- URL: [N-Queens](https://leetcode.com/problems/n-queens/)
- Function: `solveNQueens`
- Signature: `(n: int)  -> list[list[str]]`
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
- Run: `pytest -q -k "0051"`

## Common Pitfalls

- [pitfall 1]
- [pitfall 2]
- [pitfall 3]

## Similar Problems

| Number | Difficulty | Name | LeetCode |
|---|---|---|---|
| 0052 | Hard | [N-Queens II](../0052-n-queens-ii/readme.md) | [N-Queens II](https://leetcode.com/problems/n-queens-ii/) |
| 1001 | Hard | [Grid Illumination](../1001-grid-illumination/readme.md) | [Grid Illumination](https://leetcode.com/problems/grid-illumination/) |

## Examples

### Example 1

```text
Input: n = 4
Output: [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
Explanation: There exist two distinct solutions to the 4-queens puzzle as shown above
```

### Example 2

```text
Input: n = 1
Output: [["Q"]]
```

## References

- LeetCode problem and editorial links
