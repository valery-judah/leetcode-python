# 0215. Kth Largest Element in an Array

## Quick Facts

- URL: [Kth Largest Element in an Array](https://leetcode.com/problems/kth-largest-element-in-an-array/)
- Function: `findKthLargest`
- Signature: `(nums: list[int], k: int)  -> int`
- Primary pattern: **Heap (Priority Queue)**

## Constraints

- `1 <= k <= nums.length <= 10^5`
- `-10^4 <= nums[i] <= 10^4`

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
- Run: `pytest -q -k "0215"`

## Common Pitfalls

- [pitfall 1]
- [pitfall 2]
- [pitfall 3]

## Similar Problems

| Number | Difficulty | Name | LeetCode |
|---|---|---|---|
| 0324 | Medium | [Wiggle Sort II](../0324-wiggle-sort-ii/readme.md) | [Wiggle Sort II](https://leetcode.com/problems/wiggle-sort-ii/) |
| 0347 | Medium | [Top K Frequent Elements](../0347-top-k-frequent-elements/readme.md) | [Top K Frequent Elements](https://leetcode.com/problems/top-k-frequent-elements/) |
| 0414 | Easy | [Third Maximum Number](../0414-third-maximum-number/readme.md) | [Third Maximum Number](https://leetcode.com/problems/third-maximum-number/) |
| 0703 | Easy | [Kth Largest Element in a Stream](../0703-kth-largest-element-in-a-stream/readme.md) | [Kth Largest Element in a Stream](https://leetcode.com/problems/kth-largest-element-in-a-stream/) |
| 0973 | Medium | [K Closest Points to Origin](../0973-k-closest-points-to-origin/readme.md) | [K Closest Points to Origin](https://leetcode.com/problems/k-closest-points-to-origin/) |
| 1985 | Medium | [Find the Kth Largest Integer in the Array](../1985-find-the-kth-largest-integer-in-the-array/readme.md) | [Find the Kth Largest Integer in the Array](https://leetcode.com/problems/find-the-kth-largest-integer-in-the-array/) |
| 2099 | Easy | [Find Subsequence of Length K With the Largest Sum](../2099-find-subsequence-of-length-k-with-the-largest-sum/readme.md) | [Find Subsequence of Length K With the Largest Sum](https://leetcode.com/problems/find-subsequence-of-length-k-with-the-largest-sum/) |
| 2146 | Medium | [K Highest Ranked Items Within a Price Range](../2146-k-highest-ranked-items-within-a-price-range/readme.md) | [K Highest Ranked Items Within a Price Range](https://leetcode.com/problems/k-highest-ranked-items-within-a-price-range/) |

## Examples

### Example 1

```text
Input: nums = [3,2,1,5,6,4], k = 2
Output: 5
```

### Example 2

```text
Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
Output: 4
```

## References

- LeetCode problem and editorial links
