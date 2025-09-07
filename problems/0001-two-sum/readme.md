# 0001. Two Sum

## Quick Facts

- URL: [Two Sum](https://leetcode.com/problems/two-sum/)
- Function: `twoSum`
- Signature: `(nums: list[int], target: int)  -> list[int]`
- Primary pattern: **Hash Table**

## Constraints

- `2 <= nums.length <= 10^4`
- `-10^9 <= nums[i] <= 10^9`
- `-10^9 <= target <= 10^9`
- `Only one valid answer exists.`

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
- Run: `pytest -q -k "0001"`

## Common Pitfalls

- [pitfall 1]
- [pitfall 2]
- [pitfall 3]

## Similar Problems

| Number | Difficulty | Name | LeetCode |
|---|---|---|---|
| 0015 | Medium | [3Sum](../0015-3sum/readme.md) | [3Sum](https://leetcode.com/problems/3sum/) |
| 0018 | Medium | [4Sum](../0018-4sum/readme.md) | [4Sum](https://leetcode.com/problems/4sum/) |
| 0167 | Medium | [Two Sum II - Input Array Is Sorted](../0167-two-sum-ii-input-array-is-sorted/readme.md) | [Two Sum II - Input Array Is Sorted](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/) |
| 0170 | Easy | [Two Sum III - Data structure design](../0170-two-sum-iii-data-structure-design/readme.md) | [Two Sum III - Data structure design](https://leetcode.com/problems/two-sum-iii-data-structure-design/) |
| 0560 | Medium | [Subarray Sum Equals K](../0560-subarray-sum-equals-k/readme.md) | [Subarray Sum Equals K](https://leetcode.com/problems/subarray-sum-equals-k/) |
| 0653 | Easy | [Two Sum IV - Input is a BST](../0653-two-sum-iv-input-is-a-bst/readme.md) | [Two Sum IV - Input is a BST](https://leetcode.com/problems/two-sum-iv-input-is-a-bst/) |
| 1083 | Easy | [Two Sum Less Than K](../1083-two-sum-less-than-k/readme.md) | [Two Sum Less Than K](https://leetcode.com/problems/two-sum-less-than-k/) |
| 1798 | Medium | [Max Number of K-Sum Pairs](../1798-max-number-of-k-sum-pairs/readme.md) | [Max Number of K-Sum Pairs](https://leetcode.com/problems/max-number-of-k-sum-pairs/) |
| 1830 | Medium | [Count Good Meals](../1830-count-good-meals/readme.md) | [Count Good Meals](https://leetcode.com/problems/count-good-meals/) |
| 2116 | Easy | [Count Number of Pairs With Absolute Difference K](../2116-count-number-of-pairs-with-absolute-difference-k/readme.md) | [Count Number of Pairs With Absolute Difference K](https://leetcode.com/problems/count-number-of-pairs-with-absolute-difference-k/) |
| 2133 | Medium | [Number of Pairs of Strings With Concatenation Equal to Target](../2133-number-of-pairs-of-strings-with-concatenation-equal-to-target/readme.md) | [Number of Pairs of Strings With Concatenation Equal to Target](https://leetcode.com/problems/number-of-pairs-of-strings-with-concatenation-equal-to-target/) |
| 2320 | Easy | [Find All K-Distant Indices in an Array](../2320-find-all-k-distant-indices-in-an-array/readme.md) | [Find All K-Distant Indices in an Array](https://leetcode.com/problems/find-all-k-distant-indices-in-an-array/) |
| 2427 | Easy | [First Letter to Appear Twice](../2427-first-letter-to-appear-twice/readme.md) | [First Letter to Appear Twice](https://leetcode.com/problems/first-letter-to-appear-twice/) |
| 2430 | Hard | [Number of Excellent Pairs](../2430-number-of-excellent-pairs/readme.md) | [Number of Excellent Pairs](https://leetcode.com/problems/number-of-excellent-pairs/) |
| 2442 | Easy | [Number of Arithmetic Triplets](../2442-number-of-arithmetic-triplets/readme.md) | [Number of Arithmetic Triplets](https://leetcode.com/problems/number-of-arithmetic-triplets/) |
| 2455 | Medium | [Node With Highest Edge Score](../2455-node-with-highest-edge-score/readme.md) | [Node With Highest Edge Score](https://leetcode.com/problems/node-with-highest-edge-score/) |
| 2476 | Easy | [Check Distances Between Same Letters](../2476-check-distances-between-same-letters/readme.md) | [Check Distances Between Same Letters](https://leetcode.com/problems/check-distances-between-same-letters/) |
| 2480 | Easy | [Find Subarrays With Equal Sum](../2480-find-subarrays-with-equal-sum/readme.md) | [Find Subarrays With Equal Sum](https://leetcode.com/problems/find-subarrays-with-equal-sum/) |
| 2524 | Easy | [Largest Positive Integer That Exists With Its Negative](../2524-largest-positive-integer-that-exists-with-its-negative/readme.md) | [Largest Positive Integer That Exists With Its Negative](https://leetcode.com/problems/largest-positive-integer-that-exists-with-its-negative/) |
| 2561 | Easy | [Number of Distinct Averages](../2561-number-of-distinct-averages/readme.md) | [Number of Distinct Averages](https://leetcode.com/problems/number-of-distinct-averages/) |
| 2917 | Easy | [Count Pairs Whose Sum is Less than Target](../2917-count-pairs-whose-sum-is-less-than-target/readme.md) | [Count Pairs Whose Sum is Less than Target](https://leetcode.com/problems/count-pairs-whose-sum-is-less-than-target/) |

## Examples

### Example 1

```text
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
```

### Example 2

```text
Input: nums = [3,2,4], target = 6
Output: [1,2]
```

### Example 3

```text
Input: nums = [3,3], target = 6
Output: [0,1]
```

## References

- LeetCode problem and editorial links
