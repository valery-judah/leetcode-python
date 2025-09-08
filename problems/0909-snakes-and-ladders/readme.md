# 0909. Snakes and Ladders

## Quick Facts

- URL: [Snakes and Ladders](https://leetcode.com/problems/snakes-and-ladders/)
- Function: `snakesAndLadders`
- Signature: `(board: list[list[int]])  -> int`
- Primary pattern: **Array**

## Constraints

- `n == board.length == board[i].length`
- `2 <= n <= 20`
- `board[i][j] is either -1 or in the range [1, n^2].`
- `The squares labeled 1 and n^2 are not the starting points of any snake or ladder.`

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
- Run: `pytest -q -k "0909"`

## Common Pitfalls

- [pitfall 1]
- [pitfall 2]
- [pitfall 3]

## Similar Problems

| Number | Difficulty | Name | LeetCode |
|---|---|---|---|
| 2467 | Medium | [Most Profitable Path in a Tree](../2467-most-profitable-path-in-a-tree/readme.md) | [Most Profitable Path in a Tree](https://leetcode.com/problems/most-profitable-path-in-a-tree/) |

## Examples

### Example 1

```text
Input: board = [[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,35,-1,-1,13,-1],[-1,-1,-1,-1,-1,-1],[-1,15,-1,-1,-1,-1]]
Output: 4
Explanation: 
In the beginning, you start at square 1 (at row 5, column 0).
You decide to move to square 2 and must take the ladder to square 15.
You then decide to move to square 17 and must take the snake to square 13.
You then decide to move to square 14 and must take the ladder to square 35.
You then decide to move to square 36, ending the game.
This is the lowest possible number of moves to reach the last square, so return 4.
```

### Example 2

```text
Input: board = [[-1,-1],[-1,3]]
Output: 1
```

## References

- LeetCode problem and editorial links
