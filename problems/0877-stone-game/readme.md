# 0877. Stone Game

## Quick Facts

- URL: [Stone Game](https://leetcode.com/problems/stone-game/)
- Function: `stoneGame`
- Signature: `(piles: list[int])  -> bool`
- Primary pattern: **Dynamic Programming**

## Constraints

- `2 <= piles.length <= 500`
- `piles.length is even.`
- `1 <= piles[i] <= 500`
- `sum(piles[i]) is odd.`

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
- Run: `pytest -q -k "0877"`

## Common Pitfalls

- [pitfall 1]
- [pitfall 2]
- [pitfall 3]

## Similar Problems

| Number | Difficulty | Name | LeetCode |
|---|---|---|---|
| 1563 | Hard | [Stone Game V](../1563-stone-game-v/readme.md) | [Stone Game V](https://leetcode.com/problems/stone-game-v/) |
| 1686 | Medium | [Stone Game VI](../1686-stone-game-vi/readme.md) | [Stone Game VI](https://leetcode.com/problems/stone-game-vi/) |
| 1690 | Medium | [Stone Game VII](../1690-stone-game-vii/readme.md) | [Stone Game VII](https://leetcode.com/problems/stone-game-vii/) |
| 1872 | Hard | [Stone Game VIII](../1872-stone-game-viii/readme.md) | [Stone Game VIII](https://leetcode.com/problems/stone-game-viii/) |
| 2029 | Medium | [Stone Game IX](../2029-stone-game-ix/readme.md) | [Stone Game IX](https://leetcode.com/problems/stone-game-ix/) |
| 2396 | Medium | [Strictly Palindromic Number](../2396-strictly-palindromic-number/readme.md) | [Strictly Palindromic Number](https://leetcode.com/problems/strictly-palindromic-number/) |
| 2786 | Medium | [Visit Array Positions to Maximize Score](../2786-visit-array-positions-to-maximize-score/readme.md) | [Visit Array Positions to Maximize Score](https://leetcode.com/problems/visit-array-positions-to-maximize-score/) |

## Examples

### Example 1

```text
Input: piles = [5,3,4,5]
Output: true
Explanation:
Alice starts first, and can only take the first 5 or the last 5.
Say she takes the first 5, so that the row becomes [3, 4, 5].
If Bob takes 3, then the board is [4, 5], and Alice takes 5 to win with 10 points.
If Bob takes the last 5, then the board is [3, 4], and Alice takes 4 to win with 9 points.
This demonstrated that taking the first 5 was a winning move for Alice, so we return true.
```

### Example 2

```text
Input: piles = [3,7,2,3]
Output: true
```

## References

- LeetCode problem and editorial links
