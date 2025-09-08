# 1004. Max Consecutive Ones III

## Quick Facts

- URL: [Max Consecutive Ones III](https://leetcode.com/problems/max-consecutive-ones-iii/)
- Function: `longestOnes`
- Signature: `(nums: list[int], k: int)  -> int`
- Primary pattern: **Sliding Window**

## Constraints

- `1 <= nums.length <= 10^5`
- `nums[i] is either 0 or 1.`
- `0 <= k <= nums.length`

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
- Run: `pytest -q -k "1004"`

## Common Pitfalls

- [pitfall 1]
- [pitfall 2]
- [pitfall 3]

## Similar Problems

| Number | Difficulty | Name | LeetCode |
|---|---|---|---|
| 0340 | Medium | [Longest Substring with At Most K Distinct Characters](../0340-longest-substring-with-at-most-k-distinct-characters/readme.md) | [Longest Substring with At Most K Distinct Characters](https://leetcode.com/problems/longest-substring-with-at-most-k-distinct-characters/) |
| 0424 | Medium | [Longest Repeating Character Replacement](../0424-longest-repeating-character-replacement/readme.md) | [Longest Repeating Character Replacement](https://leetcode.com/problems/longest-repeating-character-replacement/) |
| 0485 | Easy | [Max Consecutive Ones](../0485-max-consecutive-ones/readme.md) | [Max Consecutive Ones](https://leetcode.com/problems/max-consecutive-ones/) |
| 0487 | Medium | [Max Consecutive Ones II](../0487-max-consecutive-ones-ii/readme.md) | [Max Consecutive Ones II](https://leetcode.com/problems/max-consecutive-ones-ii/) |
| 1493 | Medium | [Longest Subarray of 1's After Deleting One Element](../1493-longest-subarray-of-1s-after-deleting-one-element/readme.md) | [Longest Subarray of 1's After Deleting One Element](https://leetcode.com/problems/longest-subarray-of-1s-after-deleting-one-element/) |
| 2024 | Medium | [Maximize the Confusion of an Exam](../2024-maximize-the-confusion-of-an-exam/readme.md) | [Maximize the Confusion of an Exam](https://leetcode.com/problems/maximize-the-confusion-of-an-exam/) |
| 2379 | Easy | [Minimum Recolors to Get K Consecutive Black Blocks](../2379-minimum-recolors-to-get-k-consecutive-black-blocks/readme.md) | [Minimum Recolors to Get K Consecutive Black Blocks](https://leetcode.com/problems/minimum-recolors-to-get-k-consecutive-black-blocks/) |
| 2401 | Medium | [Longest Nice Subarray](../2401-longest-nice-subarray/readme.md) | [Longest Nice Subarray](https://leetcode.com/problems/longest-nice-subarray/) |
| 2461 | Medium | [Maximum Sum of Distinct Subarrays With Length K](../2461-maximum-sum-of-distinct-subarrays-with-length-k/readme.md) | [Maximum Sum of Distinct Subarrays With Length K](https://leetcode.com/problems/maximum-sum-of-distinct-subarrays-with-length-k/) |
| 2511 | Easy | [Maximum Enemy Forts That Can Be Captured](../2511-maximum-enemy-forts-that-can-be-captured/readme.md) | [Maximum Enemy Forts That Can Be Captured](https://leetcode.com/problems/maximum-enemy-forts-that-can-be-captured/) |

## Examples

### Example 1

```text
Input: nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
Output: 6
Explanation: [1,1,1,0,0,1,1,1,1,1,1]
Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.
```

### Example 2

```text
Input: nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], k = 3
Output: 10
Explanation: [0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]
Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.
```

## References

- LeetCode problem and editorial links
