# 0992. Subarrays with K Different Integers

## Quick Facts

- URL:
  [Subarrays with K Different Integers](https://leetcode.com/problems/subarrays-with-k-different-integers/)
- Function: `subarraysWithKDistinct`
- Signature: `(nums: list[int], k: int)  -> int`
- Primary pattern: **Sliding Window**

## Constraints

- `1 <= nums.length <= 2 * 10^4`
- `1 <= nums[i], k <= nums.length`

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
- Run: `pytest -q -k "0992"`

## Common Pitfalls

- [pitfall 1]
- [pitfall 2]
- [pitfall 3]

## Similar Problems

| Number | Difficulty | Name                                                                                                                               | LeetCode                                                                                                                                        |
| ------ | ---------- | ---------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------- |
| 0003   | Medium     | [Longest Substring Without Repeating Characters](../0003-longest-substring-without-repeating-characters/readme.md)                 | [Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters/)                 |
| 0159   | Medium     | [Longest Substring with At Most Two Distinct Characters](../0159-longest-substring-with-at-most-two-distinct-characters/readme.md) | [Longest Substring with At Most Two Distinct Characters](https://leetcode.com/problems/longest-substring-with-at-most-two-distinct-characters/) |
| 0340   | Medium     | [Longest Substring with At Most K Distinct Characters](../0340-longest-substring-with-at-most-k-distinct-characters/readme.md)     | [Longest Substring with At Most K Distinct Characters](https://leetcode.com/problems/longest-substring-with-at-most-k-distinct-characters/)     |
| 2062   | Easy       | [Count Vowel Substrings of a String](../2062-count-vowel-substrings-of-a-string/readme.md)                                         | [Count Vowel Substrings of a String](https://leetcode.com/problems/count-vowel-substrings-of-a-string/)                                         |
| 2107   | Medium     | [Number of Unique Flavors After Sharing K Candies](../2107-number-of-unique-flavors-after-sharing-k-candies/readme.md)             | [Number of Unique Flavors After Sharing K Candies](https://leetcode.com/problems/number-of-unique-flavors-after-sharing-k-candies/)             |
| 2261   | Medium     | [K Divisible Elements Subarrays](../2261-k-divisible-elements-subarrays/readme.md)                                                 | [K Divisible Elements Subarrays](https://leetcode.com/problems/k-divisible-elements-subarrays/)                                                 |
| 2799   | Medium     | [Count Complete Subarrays in an Array](../2799-count-complete-subarrays-in-an-array/readme.md)                                     | [Count Complete Subarrays in an Array](https://leetcode.com/problems/count-complete-subarrays-in-an-array/)                                     |

## Examples

### Example 1

```text
Input: nums = [1,2,1,2,3], k = 2
Output: 7
Explanation: Subarrays formed with exactly 2 different integers: [1,2], [2,1], [1,2], [2,3], [1,2,1], [2,1,2], [1,2,1,2]
```

### Example 2

```text
Input: nums = [1,2,1,3,4], k = 3
Output: 3
Explanation: Subarrays formed with exactly 3 different integers: [1,2,1,3], [2,1,3], [1,3,4].
```

## References

- LeetCode problem and editorial links
