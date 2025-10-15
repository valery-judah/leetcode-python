# 0130. Surrounded Regions

## Quick Facts

- URL: [Surrounded Regions](https://leetcode.com/problems/surrounded-regions/)
- Function: `solve`
- Signature: `(board: list[list[str]])  -> None`
- Primary pattern: **Array**

## Constraints

- `m == board.length`
- `n == board[i].length`
- `1 <= m, n <= 200`
- `board[i][j] is 'X' or 'O'.`

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
- Run: `pytest -q -k "0130"`

## Common Pitfalls

- [pitfall 1]
- [pitfall 2]
- [pitfall 3]

## Similar Problems

| Number | Difficulty | Name                                                     | LeetCode                                                              |
| ------ | ---------- | -------------------------------------------------------- | --------------------------------------------------------------------- |
| 0200   | Medium     | [Number of Islands](../0200-number-of-islands/readme.md) | [Number of Islands](https://leetcode.com/problems/number-of-islands/) |
| 0286   | Medium     | [Walls and Gates](../0286-walls-and-gates/readme.md)     | [Walls and Gates](https://leetcode.com/problems/walls-and-gates/)     |

## Examples

None

## References

- LeetCode problem and editorial links
