# 0850. Rectangle Area II

## Quick Facts

- URL: [Rectangle Area II](https://leetcode.com/problems/rectangle-area-ii/)
- Function: `rectangleArea`
- Signature: `(rectangles: list[list[int]])  -> int`
- Primary pattern: **Array**

## Constraints

- `1 <= rectangles.length <= 200`
- `rectanges[i].length == 4`
- `0 <= xi1, yi1, xi2, yi2 <= 10^9`
- `xi1 <= xi2`
- `yi1 <= yi2`
- `All rectangles have non zero area.`

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
- Run: `pytest -q -k "0850"`

## Common Pitfalls

- [pitfall 1]
- [pitfall 2]
- [pitfall 3]

## Similar Problems

| Number | Difficulty | Name                                                         | LeetCode                                                                  |
| ------ | ---------- | ------------------------------------------------------------ | ------------------------------------------------------------------------- |
| 3454   | Hard       | [Separate Squares II](../3454-separate-squares-ii/readme.md) | [Separate Squares II](https://leetcode.com/problems/separate-squares-ii/) |

## Examples

### Example 1

```text
Input: rectangles = [[0,0,2,2],[1,0,2,3],[1,0,3,1]]
Output: 6
Explanation: A total area of 6 is covered by all three rectangles, as illustrated in the picture.
From (1,1) to (2,2), the green and red rectangles overlap.
From (1,0) to (2,3), all three rectangles overlap.
```

### Example 2

```text
Input: rectangles = [[0,0,1000000000,1000000000]]
Output: 49
Explanation: The answer is 1018 modulo (109 + 7), which is 49.
```

## References

- LeetCode problem and editorial links
