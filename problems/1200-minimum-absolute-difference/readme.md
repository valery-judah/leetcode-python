# 1200. Minimum Absolute Difference

## Quick Facts

- URL: [Minimum Absolute Difference](https://leetcode.com/problems/minimum-absolute-difference/)
- Function: `minimumAbsDifference`
- Signature: `(arr: list[int])  -> list[list[int]]`
- Primary pattern: **Sorting**

## Constraints

- `2 <= arr.length <= 10^5`
- `-10^6 <= arr[i] <= 10^6`

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
- Run: `pytest -q -k "1200"`

## Common Pitfalls

- [pitfall 1]
- [pitfall 2]
- [pitfall 3]

## Similar Problems

| Number | Difficulty | Name | LeetCode |
|---|---|---|---|
| 2144 | Easy | [Minimum Cost of Buying Candies With Discount](../2144-minimum-cost-of-buying-candies-with-discount/readme.md) | [Minimum Cost of Buying Candies With Discount](https://leetcode.com/problems/minimum-cost-of-buying-candies-with-discount/) |
| 2616 | Medium | [Minimize the Maximum Difference of Pairs](../2616-minimize-the-maximum-difference-of-pairs/readme.md) | [Minimize the Maximum Difference of Pairs](https://leetcode.com/problems/minimize-the-maximum-difference-of-pairs/) |

## Examples

### Example 1

```text
Input: arr = [4,2,1,3]
Output: [[1,2],[2,3],[3,4]]
Explanation: The minimum absolute difference is 1. List all pairs with difference equal to 1 in ascending order.
```

### Example 2

```text
Input: arr = [1,3,6,10,15]
Output: [[1,3]]
```

### Example 3

```text
Input: arr = [3,8,-10,23,19,-4,-14,27]
Output: [[-14,-10],[19,23],[23,27]]
```

## References

- LeetCode problem and editorial links
