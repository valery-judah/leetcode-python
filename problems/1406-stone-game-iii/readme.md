# 1406. Stone Game III

## Quick Facts

- URL: [Stone Game III](https://leetcode.com/problems/stone-game-iii/)
- Function: `stoneGameIII`
- Signature: `(stoneValue: list[int])  -> str`
- Primary pattern: **Dynamic Programming**

## Constraints

- `1 <= stoneValue.length <= 5 * 10^4`
- `-1000 <= stoneValue[i] <= 1000`

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
- Run: `pytest -q -k "1406"`

## Common Pitfalls

- [pitfall 1]
- [pitfall 2]
- [pitfall 3]

## Similar Problems

| Number | Difficulty | Name                                                 | LeetCode                                                          |
| ------ | ---------- | ---------------------------------------------------- | ----------------------------------------------------------------- |
| 1563   | Hard       | [Stone Game V](../1563-stone-game-v/readme.md)       | [Stone Game V](https://leetcode.com/problems/stone-game-v/)       |
| 1686   | Medium     | [Stone Game VI](../1686-stone-game-vi/readme.md)     | [Stone Game VI](https://leetcode.com/problems/stone-game-vi/)     |
| 1690   | Medium     | [Stone Game VII](../1690-stone-game-vii/readme.md)   | [Stone Game VII](https://leetcode.com/problems/stone-game-vii/)   |
| 1872   | Hard       | [Stone Game VIII](../1872-stone-game-viii/readme.md) | [Stone Game VIII](https://leetcode.com/problems/stone-game-viii/) |
| 2029   | Medium     | [Stone Game IX](../2029-stone-game-ix/readme.md)     | [Stone Game IX](https://leetcode.com/problems/stone-game-ix/)     |

## Examples

### Example 1

```text
Input: stoneValue = [1,2,3,7]
Output: "Bob"
Explanation: Alice will always lose. Her best move will be to take three piles and the score become 6. Now the score of Bob is 7 and Bob wins.
```

### Example 2

```text
Input: stoneValue = [1,2,3,-9]
Output: "Alice"
Explanation: Alice must choose all the three piles at the first move to win and leave Bob with negative score.
If Alice chooses one pile her score will be 1 and the next move Bob's score becomes 5. In the next move, Alice will take the pile with value = -9 and lose.
If Alice chooses two piles her score will be 3 and the next move Bob's score becomes 3. In the next move, Alice will take the pile with value = -9 and also lose.
Remember that both play optimally so here Alice will choose the scenario that makes her win.
```

### Example 3

```text
Input: stoneValue = [1,2,3,6]
Output: "Tie"
Explanation: Alice cannot win this game. She can end the game in a draw if she decided to choose all the first three piles, otherwise she will lose.
```

## References

- LeetCode problem and editorial links
