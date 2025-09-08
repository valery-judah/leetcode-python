# 0189. Rotate Array

## Quick Facts

- URL: [Rotate Array](https://leetcode.com/problems/rotate-array/)
- Function: `rotate`
- Signature: `(nums: list[int], k: int)  -> None`
- Primary pattern: **Two Pointers**

## Constraints

- `1 <= nums.length <= 10^5`
- `-2^31 <= nums[i] <= 2^31 - 1`
- `0 <= k <= 10^5`

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
- Run: `pytest -q -k "0189"`

## Common Pitfalls

- [pitfall 1]
- [pitfall 2]
- [pitfall 3]

## Similar Problems

| Number | Difficulty | Name | LeetCode |
|---|---|---|---|
| 0061 | Medium | [Rotate List](../0061-rotate-list/readme.md) | [Rotate List](https://leetcode.com/problems/rotate-list/) |
| 0186 | Medium | [Reverse Words in a String II](../0186-reverse-words-in-a-string-ii/readme.md) | [Reverse Words in a String II](https://leetcode.com/problems/reverse-words-in-a-string-ii/) |
| 2607 | Medium | [Make K-Subarray Sums Equal](../2607-make-k-subarray-sums-equal/readme.md) | [Make K-Subarray Sums Equal](https://leetcode.com/problems/make-k-subarray-sums-equal/) |
| 3400 | Medium | [Maximum Number of Matching Indices After Right Shifts](../3400-maximum-number-of-matching-indices-after-right-shifts/readme.md) | [Maximum Number of Matching Indices After Right Shifts](https://leetcode.com/problems/maximum-number-of-matching-indices-after-right-shifts/) |

## Examples

### Example 1

```text
Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]
```

### Example 2

```text
Input: nums = [-1,-100,3,99], k = 2
Output: [3,99,-1,-100]
Explanation:
rotate 1 steps to the right: [99,-1,-100,3]
rotate 2 steps to the right: [3,99,-1,-100]
```

## References

- LeetCode problem and editorial links
