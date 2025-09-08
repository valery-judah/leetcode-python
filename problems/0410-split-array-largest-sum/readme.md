# 0410. Split Array Largest Sum

## Quick Facts

- URL: [Split Array Largest Sum](https://leetcode.com/problems/split-array-largest-sum/)
- Function: `splitArray`
- Signature: `(nums: list[int], k: int)  -> int`
- Primary pattern: **Binary Search**

## Constraints

- `1 <= nums.length <= 1000`
- `0 <= nums[i] <= 10^6`
- `1 <= k <= min(50, nums.length)`

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
- Run: `pytest -q -k "0410"`

## Common Pitfalls

- [pitfall 1]
- [pitfall 2]
- [pitfall 3]

## Similar Problems

| Number | Difficulty | Name | LeetCode |
|---|---|---|---|
| 1011 | Medium | [Capacity To Ship Packages Within D Days](../1011-capacity-to-ship-packages-within-d-days/readme.md) | [Capacity To Ship Packages Within D Days](https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/) |
| 1231 | Hard | [Divide Chocolate](../1231-divide-chocolate/readme.md) | [Divide Chocolate](https://leetcode.com/problems/divide-chocolate/) |
| 2305 | Medium | [Fair Distribution of Cookies](../2305-fair-distribution-of-cookies/readme.md) | [Fair Distribution of Cookies](https://leetcode.com/problems/fair-distribution-of-cookies/) |
| 2098 | Medium | [Subsequence of Size K With the Largest Even Sum](../2098-subsequence-of-size-k-with-the-largest-even-sum/readme.md) | [Subsequence of Size K With the Largest Even Sum](https://leetcode.com/problems/subsequence-of-size-k-with-the-largest-even-sum/) |
| 2234 | Hard | [Maximum Total Beauty of the Gardens](../2234-maximum-total-beauty-of-the-gardens/readme.md) | [Maximum Total Beauty of the Gardens](https://leetcode.com/problems/maximum-total-beauty-of-the-gardens/) |
| 2270 | Medium | [Number of Ways to Split Array](../2270-number-of-ways-to-split-array/readme.md) | [Number of Ways to Split Array](https://leetcode.com/problems/number-of-ways-to-split-array/) |
| 2547 | Hard | [Minimum Cost to Split an Array](../2547-minimum-cost-to-split-an-array/readme.md) | [Minimum Cost to Split an Array](https://leetcode.com/problems/minimum-cost-to-split-an-array/) |
| 3069 | Easy | [Distribute Elements Into Two Arrays I](../3069-distribute-elements-into-two-arrays-i/readme.md) | [Distribute Elements Into Two Arrays I](https://leetcode.com/problems/distribute-elements-into-two-arrays-i/) |
| 3072 | Hard | [Distribute Elements Into Two Arrays II](../3072-distribute-elements-into-two-arrays-ii/readme.md) | [Distribute Elements Into Two Arrays II](https://leetcode.com/problems/distribute-elements-into-two-arrays-ii/) |

## Examples

### Example 1

```text
Input: nums = [7,2,5,10,8], k = 2
Output: 18
Explanation: There are four ways to split nums into two subarrays.
The best way is to split it into [7,2,5] and [10,8], where the largest sum among the two subarrays is only 18.
```

### Example 2

```text
Input: nums = [1,2,3,4,5], k = 2
Output: 9
Explanation: There are four ways to split nums into two subarrays.
The best way is to split it into [1,2,3] and [4,5], where the largest sum among the two subarrays is only 9.
```

## References

- LeetCode problem and editorial links
