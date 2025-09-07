# 0128. Longest Consecutive Sequence

## Quick Facts

- URL: [Longest Consecutive Sequence](https://leetcode.com/problems/longest-consecutive-sequence/)
- Function: `longestConsecutive`
- Signature: `(nums: list[int])  -> int`
- Primary pattern: **Hash Table**

## Constraints

- `0 <= nums.length <= 10^5`
- `-10^9 <= nums[i] <= 10^9`

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
- Run: `pytest -q -k "0128"`

## Common Pitfalls

- [pitfall 1]
- [pitfall 2]
- [pitfall 3]

## Similar Problems

| Number | Difficulty | Name | LeetCode |
|---|---|---|---|
| 0298 | Medium | [Binary Tree Longest Consecutive Sequence](../0298-binary-tree-longest-consecutive-sequence/readme.md) | [Binary Tree Longest Consecutive Sequence](https://leetcode.com/problems/binary-tree-longest-consecutive-sequence/) |
| 2278 | Medium | [Find Three Consecutive Integers That Sum to a Given Number](../2278-find-three-consecutive-integers-that-sum-to-a-given-number/readme.md) | [Find Three Consecutive Integers That Sum to a Given Number](https://leetcode.com/problems/find-three-consecutive-integers-that-sum-to-a-given-number/) |
| 2355 | Medium | [Maximum Consecutive Floors Without Special Floors](../2355-maximum-consecutive-floors-without-special-floors/readme.md) | [Maximum Consecutive Floors Without Special Floors](https://leetcode.com/problems/maximum-consecutive-floors-without-special-floors/) |
| 2492 | Medium | [Length of the Longest Alphabetical Continuous Substring](../2492-length-of-the-longest-alphabetical-continuous-substring/readme.md) | [Length of the Longest Alphabetical Continuous Substring](https://leetcode.com/problems/length-of-the-longest-alphabetical-continuous-substring/) |
| 3299 | Medium | [Find the Maximum Number of Elements in Subset](../3299-find-the-maximum-number-of-elements-in-subset/readme.md) | [Find the Maximum Number of Elements in Subset](https://leetcode.com/problems/find-the-maximum-number-of-elements-in-subset/) |

## Examples

### Example 1

```text
Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
```

### Example 2

```text
Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9
```

### Example 3

```text
Input: nums = [1,0,1,2]
Output: 3
```

## References

- LeetCode problem and editorial links
