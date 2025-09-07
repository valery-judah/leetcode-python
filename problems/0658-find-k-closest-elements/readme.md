# 0658. Find K Closest Elements

## Quick Facts

- URL: [Find K Closest Elements](https://leetcode.com/problems/find-k-closest-elements/)
- Function: `findClosestElements`
- Signature: `(arr: list[int], k: int, x: int)  -> list[int]`
- Primary pattern: **Sliding Window**

## Constraints

- `1 <= k <= arr.length`
- `1 <= arr.length <= 10^4`
- `arr is sorted in ascending order.`
- `-10^4 <= arr[i], x <= 10^4`

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
- Run: `pytest -q -k "0658"`

## Common Pitfalls

- [pitfall 1]
- [pitfall 2]
- [pitfall 3]

## Similar Problems

| Number | Difficulty | Name | LeetCode |
|---|---|---|---|
| 0374 | Easy | [Guess Number Higher or Lower](../0374-guess-number-higher-or-lower/readme.md) | [Guess Number Higher or Lower](https://leetcode.com/problems/guess-number-higher-or-lower/) |
| 0375 | Medium | [Guess Number Higher or Lower II](../0375-guess-number-higher-or-lower-ii/readme.md) | [Guess Number Higher or Lower II](https://leetcode.com/problems/guess-number-higher-or-lower-ii/) |
| 0719 | Hard | [Find K-th Smallest Pair Distance](../0719-find-k-th-smallest-pair-distance/readme.md) | [Find K-th Smallest Pair Distance](https://leetcode.com/problems/find-k-th-smallest-pair-distance/) |
| 2350 | Easy | [Find Closest Number to Zero](../2350-find-closest-number-to-zero/readme.md) | [Find Closest Number to Zero](https://leetcode.com/problems/find-closest-number-to-zero/) |

## Examples

None

## References

- LeetCode problem and editorial links
