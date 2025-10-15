# 1240. Tiling a Rectangle with the Fewest Squares

## Quick Facts

- URL:
  [Tiling a Rectangle with the Fewest Squares](https://leetcode.com/problems/tiling-a-rectangle-with-the-fewest-squares/)
- Function: `tilingRectangle`
- Signature: `(n: int, m: int)  -> int`
- Primary pattern: **Backtracking**

## Constraints

- `1 <= n, m <= 13`

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
- Run: `pytest -q -k "1240"`

## Common Pitfalls

- [pitfall 1]
- [pitfall 2]
- [pitfall 3]

## Similar Problems

| Number | Difficulty | Name                                                               | LeetCode                                                                        |
| ------ | ---------- | ------------------------------------------------------------------ | ------------------------------------------------------------------------------- |
| 2312   | Hard       | [Selling Pieces of Wood](../2312-selling-pieces-of-wood/readme.md) | [Selling Pieces of Wood](https://leetcode.com/problems/selling-pieces-of-wood/) |

## Examples

### Example 1

```text
Input: n = 2, m = 3
Output: 3
Explanation: 3 squares are necessary to cover the rectangle.
2 (squares of 1x1)
1 (square of 2x2)
```

### Example 2

```text
Input: n = 5, m = 8
Output: 5
```

### Example 3

```text
Input: n = 11, m = 13
Output: 6
```

## References

- LeetCode problem and editorial links
