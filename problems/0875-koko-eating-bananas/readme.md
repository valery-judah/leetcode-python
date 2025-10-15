# 0875. Koko Eating Bananas

## Quick Facts

- URL: [Koko Eating Bananas](https://leetcode.com/problems/koko-eating-bananas/)
- Function: `minEatingSpeed`
- Signature: `(piles: list[int], h: int)  -> int`
- Primary pattern: **Binary Search**

## Constraints

- `1 <= piles.length <= 10^4`
- `piles.length <= h <= 10^9`
- `1 <= piles[i] <= 10^9`

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
- Run: `pytest -q -k "0875"`

## Common Pitfalls

- [pitfall 1]
- [pitfall 2]
- [pitfall 3]

## Similar Problems

| Number | Difficulty | Name                                                                                                                               | LeetCode                                                                                                                                        |
| ------ | ---------- | ---------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------- |
| 0774   | Hard       | [Minimize Max Distance to Gas Station](../0774-minimize-max-distance-to-gas-station/readme.md)                                     | [Minimize Max Distance to Gas Station](https://leetcode.com/problems/minimize-max-distance-to-gas-station/)                                     |
| 2226   | Medium     | [Maximum Candies Allocated to K Children](../2226-maximum-candies-allocated-to-k-children/readme.md)                               | [Maximum Candies Allocated to K Children](https://leetcode.com/problems/maximum-candies-allocated-to-k-children/)                               |
| 2064   | Medium     | [Minimized Maximum of Products Distributed to Any Store](../2064-minimized-maximum-of-products-distributed-to-any-store/readme.md) | [Minimized Maximum of Products Distributed to Any Store](https://leetcode.com/problems/minimized-maximum-of-products-distributed-to-any-store/) |
| 2498   | Medium     | [Frog Jump II](../2498-frog-jump-ii/readme.md)                                                                                     | [Frog Jump II](https://leetcode.com/problems/frog-jump-ii/)                                                                                     |
| 2594   | Medium     | [Minimum Time to Repair Cars](../2594-minimum-time-to-repair-cars/readme.md)                                                       | [Minimum Time to Repair Cars](https://leetcode.com/problems/minimum-time-to-repair-cars/)                                                       |

## Examples

### Example 1

```text
Input: piles = [3,6,7,11], h = 8
Output: 4
```

### Example 2

```text
Input: piles = [30,11,23,4,20], h = 5
Output: 30
```

### Example 3

```text
Input: piles = [30,11,23,4,20], h = 6
Output: 23
```

## References

- LeetCode problem and editorial links
