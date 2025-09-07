# 0349. Intersection of Two Arrays

## Quick Facts

- URL: [Intersection of Two Arrays](https://leetcode.com/problems/intersection-of-two-arrays/)
- Function: `intersection`
- Signature: `(nums1: list[int], nums2: list[int])  -> list[int]`
- Primary pattern: **Two Pointers**

## Constraints

- `1 <= nums1.length, nums2.length <= 1000`
- `0 <= nums1[i], nums2[i] <= 1000`

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
- Run: `pytest -q -k "0349"`

## Common Pitfalls

- [pitfall 1]
- [pitfall 2]
- [pitfall 3]

## Similar Problems

| Number | Difficulty | Name | LeetCode |
|---|---|---|---|
| 0350 | Easy | [Intersection of Two Arrays II](../0350-intersection-of-two-arrays-ii/readme.md) | [Intersection of Two Arrays II](https://leetcode.com/problems/intersection-of-two-arrays-ii/) |
| 1213 | Easy | [Intersection of Three Sorted Arrays](../1213-intersection-of-three-sorted-arrays/readme.md) | [Intersection of Three Sorted Arrays](https://leetcode.com/problems/intersection-of-three-sorted-arrays/) |
| 1392 | Easy | [Find the Difference of Two Arrays](../1392-find-the-difference-of-two-arrays/readme.md) | [Find the Difference of Two Arrays](https://leetcode.com/problems/find-the-difference-of-two-arrays/) |
| 2085 | Easy | [Count Common Words With One Occurrence](../2085-count-common-words-with-one-occurrence/readme.md) | [Count Common Words With One Occurrence](https://leetcode.com/problems/count-common-words-with-one-occurrence/) |
| 2143 | Hard | [Choose Numbers From Two Arrays in Range](../2143-choose-numbers-from-two-arrays-in-range/readme.md) | [Choose Numbers From Two Arrays in Range](https://leetcode.com/problems/choose-numbers-from-two-arrays-in-range/) |
| 2248 | Easy | [Intersection of Multiple Arrays](../2248-intersection-of-multiple-arrays/readme.md) | [Intersection of Multiple Arrays](https://leetcode.com/problems/intersection-of-multiple-arrays/) |
| 2540 | Easy | [Minimum Common Value](../2540-minimum-common-value/readme.md) | [Minimum Common Value](https://leetcode.com/problems/minimum-common-value/) |
| 3002 | Medium | [Maximum Size of a Set After Removals](../3002-maximum-size-of-a-set-after-removals/readme.md) | [Maximum Size of a Set After Removals](https://leetcode.com/problems/maximum-size-of-a-set-after-removals/) |

## Examples

### Example 1

```text
Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2]
```

### Example 2

```text
Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [9,4]
Explanation: [4,9] is also accepted.
```

## References

- LeetCode problem and editorial links
