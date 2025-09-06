# 0070. Climbing Stairs

## Quick Facts

- URL: https://leetcode.com/problems/climbing-stairs/
- Signature: `n: int` → `int`
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
- Run: `pytest -q -k "0070"`

## Common Pitfalls

- [pitfall 1]
- [pitfall 2]
- [pitfall 3]

## Similar Problems

| Number | Difficulty | Name | LeetCode |
|---|---|---|---|
| 0746 | Easy | [Min Cost Climbing Stairs](../0746-min-cost-climbing-stairs/readme.md) | [link](https://leetcode.com/problems/min-cost-climbing-stairs/) |
| 0509 | Easy | [Fibonacci Number](../0509-fibonacci-number/readme.md) | [link](https://leetcode.com/problems/fibonacci-number/) |
| 1137 | Easy | [N-th Tribonacci Number](../1137-n-th-tribonacci-number/readme.md) | [link](https://leetcode.com/problems/n-th-tribonacci-number/) |
| 2244 | Medium | [Minimum Rounds to Complete All Tasks](../2244-minimum-rounds-to-complete-all-tasks/readme.md) | [link](https://leetcode.com/problems/minimum-rounds-to-complete-all-tasks/) |
| 2320 | Medium | [Count Number of Ways to Place Houses](../2320-count-number-of-ways-to-place-houses/readme.md) | [link](https://leetcode.com/problems/count-number-of-ways-to-place-houses/) |
| 2400 | Medium | [Number of Ways to Reach a Position After Exactly k Steps](../2400-number-of-ways-to-reach-a-position-after-exactly-k-steps/readme.md) | [link](https://leetcode.com/problems/number-of-ways-to-reach-a-position-after-exactly-k-steps/) |
| 2466 | Medium | [Count Ways To Build Good Strings](../2466-count-ways-to-build-good-strings/readme.md) | [link](https://leetcode.com/problems/count-ways-to-build-good-strings/) |
| 2498 | Medium | [Frog Jump II](../2498-frog-jump-ii/readme.md) | [link](https://leetcode.com/problems/frog-jump-ii/) |
| 3154 | Hard | [Find Number of Ways to Reach the K-th Stair](../3154-find-number-of-ways-to-reach-the-k-th-stair/readme.md) | [link](https://leetcode.com/problems/find-number-of-ways-to-reach-the-k-th-stair/) |
| 3183 | Medium | [The Number of Ways to Make the Sum](../3183-the-number-of-ways-to-make-the-sum/readme.md) | [link](https://leetcode.com/problems/the-number-of-ways-to-make-the-sum/) |

## References

- LeetCode problem and editorial links

## Changelog

- 2025-09-06T13:33:48Z: Created scaffold.
