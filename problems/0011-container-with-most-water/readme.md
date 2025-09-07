# 0011. Container With Most Water

## Quick Facts

- URL: [Container With Most Water](https://leetcode.com/problems/container-with-most-water/)
- Function: `maxArea`
- Signature: `(height: list[int])  -> int`
- Primary pattern: **Two Pointers**

## Constraints

- `n == height.length`
- `2 <= n <= 10^5`
- `0 <= height[i] <= 10^4`

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
- Run: `pytest -q -k "0011"`

## Common Pitfalls

- [pitfall 1]
- [pitfall 2]
- [pitfall 3]

## Similar Problems

| Number | Difficulty | Name | LeetCode |
|---|---|---|---|
| 0042 | Hard | [Trapping Rain Water](../0042-trapping-rain-water/readme.md) | [Trapping Rain Water](https://leetcode.com/problems/trapping-rain-water/) |
| 2600 | Medium | [Maximum Tastiness of Candy Basket](../2600-maximum-tastiness-of-candy-basket/readme.md) | [Maximum Tastiness of Candy Basket](https://leetcode.com/problems/maximum-tastiness-of-candy-basket/) |
| 2690 | Medium | [House Robber IV](../2690-house-robber-iv/readme.md) | [House Robber IV](https://leetcode.com/problems/house-robber-iv/) |

## Examples

### Example 1

```text
Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.
```

### Example 2

```text
Input: height = [1,1]
Output: 1
```

## References

- LeetCode problem and editorial links
