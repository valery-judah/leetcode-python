# 0041. First Missing Positive

## Quick Facts

- URL: [First Missing Positive](https://leetcode.com/problems/first-missing-positive/)
- Function: `firstMissingPositive`
- Signature: `(nums: list[int])  -> int`
- Primary pattern: **Hash Table**

## Constraints

- `1 <= nums.length <= 10^5`
- `-2^31 <= nums[i] <= 2^31 - 1`

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
- Run: `pytest -q -k "0041"`

## Common Pitfalls

- [pitfall 1]
- [pitfall 2]
- [pitfall 3]

## Similar Problems

| Number | Difficulty | Name | LeetCode |
|---|---|---|---|
| 0268 | Easy | [Missing Number](../0268-missing-number/readme.md) | [Missing Number](https://leetcode.com/problems/missing-number/) |
| 0287 | Medium | [Find the Duplicate Number](../0287-find-the-duplicate-number/readme.md) | [Find the Duplicate Number](https://leetcode.com/problems/find-the-duplicate-number/) |
| 0448 | Easy | [Find All Numbers Disappeared in an Array](../0448-find-all-numbers-disappeared-in-an-array/readme.md) | [Find All Numbers Disappeared in an Array](https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/) |
| 0770 | Hard | [Couples Holding Hands](../0770-couples-holding-hands/readme.md) | [Couples Holding Hands](https://leetcode.com/problems/couples-holding-hands/) |
| 2413 | Medium | [Smallest Number in Infinite Set](../2413-smallest-number-in-infinite-set/readme.md) | [Smallest Number in Infinite Set](https://leetcode.com/problems/smallest-number-in-infinite-set/) |
| 2640 | Medium | [Maximum Number of Integers to Choose From a Range I](../2640-maximum-number-of-integers-to-choose-from-a-range-i/readme.md) | [Maximum Number of Integers to Choose From a Range I](https://leetcode.com/problems/maximum-number-of-integers-to-choose-from-a-range-i/) |
| 2661 | Medium | [Smallest Missing Non-negative Integer After Operations](../2661-smallest-missing-non-negative-integer-after-operations/readme.md) | [Smallest Missing Non-negative Integer After Operations](https://leetcode.com/problems/smallest-missing-non-negative-integer-after-operations/) |
| 2702 | Medium | [Maximum Number of Integers to Choose From a Range II](../2702-maximum-number-of-integers-to-choose-from-a-range-ii/readme.md) | [Maximum Number of Integers to Choose From a Range II](https://leetcode.com/problems/maximum-number-of-integers-to-choose-from-a-range-ii/) |
| 3236 | Easy | [Smallest Missing Integer Greater Than Sequential Prefix Sum](../3236-smallest-missing-integer-greater-than-sequential-prefix-sum/readme.md) | [Smallest Missing Integer Greater Than Sequential Prefix Sum](https://leetcode.com/problems/smallest-missing-integer-greater-than-sequential-prefix-sum/) |

## Examples

### Example 1

```text
Input: nums = [1,2,0]
Output: 3
Explanation: The numbers in the range [1,2] are all in the array.
```

### Example 2

```text
Input: nums = [3,4,-1,1]
Output: 2
Explanation: 1 is in the array but 2 is missing.
```

### Example 3

```text
Input: nums = [7,8,9,11,12]
Output: 1
Explanation: The smallest positive integer 1 is missing.
```

## References

- LeetCode problem and editorial links
