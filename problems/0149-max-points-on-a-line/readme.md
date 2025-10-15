# 0149. Max Points on a Line

## Quick Facts

- URL: [Max Points on a Line](https://leetcode.com/problems/max-points-on-a-line/)
- Function: `maxPoints`
- Signature: `(points: list[list[int]])  -> int`
- Primary pattern: **Hash Table**

## Constraints

- `1 <= points.length <= 300`
- `points[i].length == 2`
- `-10^4 <= xi, yi <= 10^4`
- `All the points are unique.`

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
- Run: `pytest -q -k "0149"`

## Common Pitfalls

- [pitfall 1]
- [pitfall 2]
- [pitfall 3]

## Similar Problems

| Number | Difficulty | Name                                                                                                 | LeetCode                                                                                                          |
| ------ | ---------- | ---------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------- |
| 0356   | Medium     | [Line Reflection](../0356-line-reflection/readme.md)                                                 | [Line Reflection](https://leetcode.com/problems/line-reflection/)                                                 |
| 2152   | Medium     | [Minimum Number of Lines to Cover Points](../2152-minimum-number-of-lines-to-cover-points/readme.md) | [Minimum Number of Lines to Cover Points](https://leetcode.com/problems/minimum-number-of-lines-to-cover-points/) |
| 2280   | Medium     | [Minimum Lines to Represent a Line Chart](../2280-minimum-lines-to-represent-a-line-chart/readme.md) | [Minimum Lines to Represent a Line Chart](https://leetcode.com/problems/minimum-lines-to-represent-a-line-chart/) |
| 3404   | Medium     | [Count Special Subsequences](../3404-count-special-subsequences/readme.md)                           | [Count Special Subsequences](https://leetcode.com/problems/count-special-subsequences/)                           |

## Examples

### Example 1

```text
Input: points = [[1,1],[2,2],[3,3]]
Output: 3
```

### Example 2

```text
Input: points = [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
Output: 4
```

## References

- LeetCode problem and editorial links
