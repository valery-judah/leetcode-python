# 0718. Maximum Length of Repeated Subarray

## Quick Facts

- URL:
  [Maximum Length of Repeated Subarray](https://leetcode.com/problems/maximum-length-of-repeated-subarray/)
- Function: `findLength`
- Signature: `(nums1: list[int], nums2: list[int])  -> int`
- Primary pattern: **Sliding Window**

## Constraints

- `1 <= nums1.length, nums2.length <= 1000`
- `0 <= nums1[i], nums2[i] <= 100`

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
- Run: `pytest -q -k "0718"`

## Common Pitfalls

- [pitfall 1]
- [pitfall 2]
- [pitfall 3]

## Similar Problems

| Number | Difficulty | Name                                                                                                                   | LeetCode                                                                                                                            |
| ------ | ---------- | ---------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------- |
| 0209   | Medium     | [Minimum Size Subarray Sum](../0209-minimum-size-subarray-sum/readme.md)                                               | [Minimum Size Subarray Sum](https://leetcode.com/problems/minimum-size-subarray-sum/)                                               |
| 1923   | Hard       | [Longest Common Subpath](../1923-longest-common-subpath/readme.md)                                                     | [Longest Common Subpath](https://leetcode.com/problems/longest-common-subpath/)                                                     |
| 3177   | Hard       | [Find the Maximum Length of a Good Subsequence II](../3177-find-the-maximum-length-of-a-good-subsequence-ii/readme.md) | [Find the Maximum Length of a Good Subsequence II](https://leetcode.com/problems/find-the-maximum-length-of-a-good-subsequence-ii/) |
| 3176   | Medium     | [Find the Maximum Length of a Good Subsequence I](../3176-find-the-maximum-length-of-a-good-subsequence-i/readme.md)   | [Find the Maximum Length of a Good Subsequence I](https://leetcode.com/problems/find-the-maximum-length-of-a-good-subsequence-i/)   |

## Examples

### Example 1

```text
Input: nums1 = [1,2,3,2,1], nums2 = [3,2,1,4,7]
Output: 3
Explanation: The repeated subarray with maximum length is [3,2,1].
```

### Example 2

```text
Input: nums1 = [0,0,0,0,0], nums2 = [0,0,0,0,0]
Output: 5
Explanation: The repeated subarray with maximum length is [0,0,0,0,0].
```

## References

- LeetCode problem and editorial links
