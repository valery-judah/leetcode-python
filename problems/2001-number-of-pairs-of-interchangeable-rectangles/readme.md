# 2001. Number of Pairs of Interchangeable Rectangles

## Quick Facts

- URL:
  [Number of Pairs of Interchangeable Rectangles](https://leetcode.com/problems/number-of-pairs-of-interchangeable-rectangles/)
- Function: `interchangeableRectangles`
- Signature: `(rectangles: list[list[int]])  -> int`
- Primary pattern: **Hash Table**

## Constraints

- `n == rectangles.length`
- `1 <= n <= 10^5`
- `rectangles[i].length == 2`
- `1 <= widthi, heighti <= 10^5`

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
- Run: `pytest -q -k "2001"`

## Common Pitfalls

- [pitfall 1]
- [pitfall 2]
- [pitfall 3]

## Similar Problems

| Number | Difficulty | Name                                                                                           | LeetCode                                                                                                    |
| ------ | ---------- | ---------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------- |
| 1512   | Easy       | [Number of Good Pairs](../1512-number-of-good-pairs/readme.md)                                 | [Number of Good Pairs](https://leetcode.com/problems/number-of-good-pairs/)                                 |
| 1814   | Medium     | [Count Nice Pairs in an Array](../1814-count-nice-pairs-in-an-array/readme.md)                 | [Count Nice Pairs in an Array](https://leetcode.com/problems/count-nice-pairs-in-an-array/)                 |
| 2197   | Hard       | [Replace Non-Coprime Numbers in Array](../2197-replace-non-coprime-numbers-in-array/readme.md) | [Replace Non-Coprime Numbers in Array](https://leetcode.com/problems/replace-non-coprime-numbers-in-array/) |

## Examples

### Example 1

```text
Input: rectangles = [[4,8],[3,6],[10,20],[15,30]]
Output: 6
Explanation: The following are the interchangeable pairs of rectangles by index (0-indexed):
- Rectangle 0 with rectangle 1: 4/8 == 3/6.
- Rectangle 0 with rectangle 2: 4/8 == 10/20.
- Rectangle 0 with rectangle 3: 4/8 == 15/30.
- Rectangle 1 with rectangle 2: 3/6 == 10/20.
- Rectangle 1 with rectangle 3: 3/6 == 15/30.
- Rectangle 2 with rectangle 3: 10/20 == 15/30.
```

### Example 2

```text
Input: rectangles = [[4,5],[7,8]]
Output: 0
Explanation: There are no interchangeable pairs of rectangles.
```

## References

- LeetCode problem and editorial links
