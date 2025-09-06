# 0239. Sliding Window Maximum

## Quick Facts

- URL: https://leetcode.com/problems/sliding-window-maximum/
- Signature: `nums: list[int]`, `k: int` → `list[int]`
- Constraints: [paste from LC]
- Primary pattern: [write primary pattern]

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
- Run: `pytest -q -k "0239"`

## Common Pitfalls

- [pitfall 1]
- [pitfall 2]
- [pitfall 3]

## Similar Problems

| Number | Difficulty | Name | LeetCode |
|---|---|---|---|
| 0076 | Hard | [Minimum Window Substring](../0076-minimum-window-substring/readme.md) | [link](https://leetcode.com/problems/minimum-window-substring/) |
| 0155 | Medium | [Min Stack](../0155-min-stack/readme.md) | [link](https://leetcode.com/problems/min-stack/) |
| 0159 | Medium | [Longest Substring with At Most Two Distinct Characters](../0159-longest-substring-with-at-most-two-distinct-characters/readme.md) | [link](https://leetcode.com/problems/longest-substring-with-at-most-two-distinct-characters/) |
| 0265 | Hard | [Paint House II](../0265-paint-house-ii/readme.md) | [link](https://leetcode.com/problems/paint-house-ii/) |
| 1696 | Medium | [Jump Game VI](../1696-jump-game-vi/readme.md) | [link](https://leetcode.com/problems/jump-game-vi/) |
| 2398 | Hard | [Maximum Number of Robots Within Budget](../2398-maximum-number-of-robots-within-budget/readme.md) | [link](https://leetcode.com/problems/maximum-number-of-robots-within-budget/) |
| 2517 | Medium | [Maximum Tastiness of Candy Basket](../2517-maximum-tastiness-of-candy-basket/readme.md) | [link](https://leetcode.com/problems/maximum-tastiness-of-candy-basket/) |
| 2530 | Medium | [Maximal Score After Applying K Operations](../2530-maximal-score-after-applying-k-operations/readme.md) | [link](https://leetcode.com/problems/maximal-score-after-applying-k-operations/) |

## References

- LeetCode problem and editorial links

## Changelog

- 2025-09-06T13:33:53Z: Created scaffold.
