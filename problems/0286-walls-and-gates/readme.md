# 0286. Walls and Gates

## Quick Facts

- URL: [Walls and Gates](https://leetcode.com/problems/walls-and-gates/)
- Function: `wallsAndGates`
- Signature: `(rooms: list[list[int]])  -> None`
- Primary pattern: **Array**

## Constraints

- `m == rooms.length`
- `n == rooms[i].length`
- `1 <= m, n <= 250`
- `rooms[i][j] is -1, 0, or 2^31 - 1.`

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
- Run: `pytest -q -k "0286"`

## Common Pitfalls

- [pitfall 1]
- [pitfall 2]
- [pitfall 3]

## Similar Problems

| Number | Difficulty | Name                                                                                                                         | LeetCode                                                                                                                                  |
| ------ | ---------- | ---------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------- |
| 0130   | Medium     | [Surrounded Regions](../0130-surrounded-regions/readme.md)                                                                   | [Surrounded Regions](https://leetcode.com/problems/surrounded-regions/)                                                                   |
| 0200   | Medium     | [Number of Islands](../0200-number-of-islands/readme.md)                                                                     | [Number of Islands](https://leetcode.com/problems/number-of-islands/)                                                                     |
| 0317   | Hard       | [Shortest Distance from All Buildings](../0317-shortest-distance-from-all-buildings/readme.md)                               | [Shortest Distance from All Buildings](https://leetcode.com/problems/shortest-distance-from-all-buildings/)                               |
| 0419   | Medium     | [Battleships in a Board](../0419-battleships-in-a-board/readme.md)                                                           | [Battleships in a Board](https://leetcode.com/problems/battleships-in-a-board/)                                                           |
| 0489   | Hard       | [Robot Room Cleaner](../0489-robot-room-cleaner/readme.md)                                                                   | [Robot Room Cleaner](https://leetcode.com/problems/robot-room-cleaner/)                                                                   |
| 0994   | Medium     | [Rotting Oranges](../0994-rotting-oranges/readme.md)                                                                         | [Rotting Oranges](https://leetcode.com/problems/rotting-oranges/)                                                                         |
| 3015   | Medium     | [Count the Number of Houses at a Certain Distance I](../3015-count-the-number-of-houses-at-a-certain-distance-i/readme.md)   | [Count the Number of Houses at a Certain Distance I](https://leetcode.com/problems/count-the-number-of-houses-at-a-certain-distance-i/)   |
| 3017   | Hard       | [Count the Number of Houses at a Certain Distance II](../3017-count-the-number-of-houses-at-a-certain-distance-ii/readme.md) | [Count the Number of Houses at a Certain Distance II](https://leetcode.com/problems/count-the-number-of-houses-at-a-certain-distance-ii/) |

## Examples

### Example 1

```text
Input: rooms = [[2147483647,-1,0,2147483647],[2147483647,2147483647,2147483647,-1],[2147483647,-1,2147483647,-1],[0,-1,2147483647,2147483647]]
Output: [[3,-1,0,1],[2,2,1,-1],[1,-1,2,-1],[0,-1,3,4]]
```

### Example 2

```text
Input: rooms = [[-1]]
Output: [[-1]]
```

## References

- LeetCode problem and editorial links
