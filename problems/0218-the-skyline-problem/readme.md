# 0218. The Skyline Problem

## Quick Facts

- URL: [The Skyline Problem](https://leetcode.com/problems/the-skyline-problem/)
- Function: `getSkyline`
- Signature: `(buildings: list[list[int]])  -> list[list[int]]`
- Primary pattern: **Heap (Priority Queue)**

## Constraints

- `1 <= buildings.length <= 10^4`
- `0 <= lefti < righti <= 2^31 - 1`
- `1 <= heighti <= 2^31 - 1`
- `buildings is sorted by lefti in non-decreasing order.`

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
- Run: `pytest -q -k "0218"`

## Common Pitfalls

- [pitfall 1]
- [pitfall 2]
- [pitfall 3]

## Similar Problems

| Number | Difficulty | Name                                                         | LeetCode                                                                  |
| ------ | ---------- | ------------------------------------------------------------ | ------------------------------------------------------------------------- |
| 0699   | Hard       | [Falling Squares](../0699-falling-squares/readme.md)         | [Falling Squares](https://leetcode.com/problems/falling-squares/)         |
| 2381   | Medium     | [Shifting Letters II](../2381-shifting-letters-ii/readme.md) | [Shifting Letters II](https://leetcode.com/problems/shifting-letters-ii/) |

## Examples

### Example 1

```text
Input: buildings = [[2,9,10],[3,7,15],[5,12,12],[15,20,10],[19,24,8]]
Output: [[2,10],[3,15],[7,12],[12,0],[15,10],[20,8],[24,0]]
Explanation:
Figure A shows the buildings of the input.
Figure B shows the skyline formed by those buildings. The red points in figure B represent the key points in the output list.
```

### Example 2

```text
Input: buildings = [[0,2,3],[2,5,3]]
Output: [[0,3],[5,0]]
```

## References

- LeetCode problem and editorial links
