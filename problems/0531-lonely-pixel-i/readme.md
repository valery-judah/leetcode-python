# 0531. Lonely Pixel I

## Quick Facts

- URL: [Lonely Pixel I](https://leetcode.com/problems/lonely-pixel-i/)
- Function: `findLonelyPixel`
- Signature: `(picture: list[list[str]])  -> int`
- Primary pattern: **Hash Table**

## Constraints

- `m == picture.length`
- `n == picture[i].length`
- `1 <= m, n <= 500`
- `picture[i][j] is 'W' or 'B'.`

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
- Run: `pytest -q -k "0531"`

## Common Pitfalls

- [pitfall 1]
- [pitfall 2]
- [pitfall 3]

## Similar Problems

| Number | Difficulty | Name                                                 | LeetCode                                                          |
| ------ | ---------- | ---------------------------------------------------- | ----------------------------------------------------------------- |
| 0533   | Medium     | [Lonely Pixel II](../0533-lonely-pixel-ii/readme.md) | [Lonely Pixel II](https://leetcode.com/problems/lonely-pixel-ii/) |

## Examples

### Example 1

```text
Input: picture = [["W","W","B"],["W","B","W"],["B","W","W"]]
Output: 3
Explanation: All the three 'B's are black lonely pixels.
```

### Example 2

```text
Input: picture = [["B","B","B"],["B","B","W"],["B","B","B"]]
Output: 0
```

## References

- LeetCode problem and editorial links
