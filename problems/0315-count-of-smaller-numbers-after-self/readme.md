# 0315. Count of Smaller Numbers After Self

## Quick Facts

- URL: [Count of Smaller Numbers After Self](https://leetcode.com/problems/count-of-smaller-numbers-after-self/)
- Function: `countSmaller`
- Signature: `(nums: list[int])  -> list[int]`
- Primary pattern: **Binary Search**

## Constraints

- `1 <= nums.length <= 10^5`
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
- Run: `pytest -q -k "0315"`

## Common Pitfalls

- [pitfall 1]
- [pitfall 2]
- [pitfall 3]

## Similar Problems

| Number | Difficulty | Name | LeetCode |
|---|---|---|---|
| 0327 | Hard | [Count of Range Sum](../0327-count-of-range-sum/readme.md) | [Count of Range Sum](https://leetcode.com/problems/count-of-range-sum/) |
| 0406 | Medium | [Queue Reconstruction by Height](../0406-queue-reconstruction-by-height/readme.md) | [Queue Reconstruction by Height](https://leetcode.com/problems/queue-reconstruction-by-height/) |
| 0493 | Hard | [Reverse Pairs](../0493-reverse-pairs/readme.md) | [Reverse Pairs](https://leetcode.com/problems/reverse-pairs/) |
| 1365 | Easy | [How Many Numbers Are Smaller Than the Current Number](../1365-how-many-numbers-are-smaller-than-the-current-number/readme.md) | [How Many Numbers Are Smaller Than the Current Number](https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/) |
| 2179 | Hard | [Count Good Triplets in an Array](../2179-count-good-triplets-in-an-array/readme.md) | [Count Good Triplets in an Array](https://leetcode.com/problems/count-good-triplets-in-an-array/) |
| 2519 | Hard | [Count the Number of K-Big Indices](../2519-count-the-number-of-k-big-indices/readme.md) | [Count the Number of K-Big Indices](https://leetcode.com/problems/count-the-number-of-k-big-indices/) |

## Examples

### Example 1

```text
Input: nums = [5,2,6,1]
Output: [2,1,1,0]
Explanation:
To the right of 5 there are 2 smaller elements (2 and 1).
To the right of 2 there is only 1 smaller element (1).
To the right of 6 there is 1 smaller element (1).
To the right of 1 there is 0 smaller element.
```

### Example 2

```text
Input: nums = [-1]
Output: [0]
```

### Example 3

```text
Input: nums = [-1,-1]
Output: [0,0]
```

## References

- LeetCode problem and editorial links
