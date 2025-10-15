# 0794. Valid Tic-Tac-Toe State

## Quick Facts

- URL: [Valid Tic-Tac-Toe State](https://leetcode.com/problems/valid-tic-tac-toe-state/)
- Function: `validTicTacToe`
- Signature: `(board: list[str])  -> bool`
- Primary pattern: **Array**

## Constraints

- `board.length == 3`
- `board[i].length == 3`
- `board[i][j] is either 'X', 'O', or ' '.`

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
- Run: `pytest -q -k "0794"`

## Common Pitfalls

- [pitfall 1]
- [pitfall 2]
- [pitfall 3]

## Similar Problems

| Number | Difficulty | Name                                                       | LeetCode                                                                |
| ------ | ---------- | ---------------------------------------------------------- | ----------------------------------------------------------------------- |
| 0348   | Medium     | [Design Tic-Tac-Toe](../0348-design-tic-tac-toe/readme.md) | [Design Tic-Tac-Toe](https://leetcode.com/problems/design-tic-tac-toe/) |

## Examples

### Example 1

```text
Input: board = ["O  ","   ","   "]
Output: false
Explanation: The first player always plays "X".
```

### Example 2

```text
Input: board = ["XOX"," X ","   "]
Output: false
Explanation: Players take turns making moves.
```

### Example 3

```text
Input: board = ["XOX","O O","XOX"]
Output: true
```

## References

- LeetCode problem and editorial links
