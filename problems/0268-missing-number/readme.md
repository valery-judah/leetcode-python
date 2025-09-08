# 0268. Missing Number

## Quick Facts

- URL: [Missing Number](https://leetcode.com/problems/missing-number/)
- Function: `missingNumber`
- Signature: `(nums: list[int])  -> int`
- Primary pattern: **Binary Search**

## Constraints

- `n == nums.length`
- `1 <= n <= 10^4`
- `0 <= nums[i] <= n`
- `All the numbers of nums are unique.`

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
- Run: `pytest -q -k "0268"`

## Common Pitfalls

- [pitfall 1]
- [pitfall 2]
- [pitfall 3]

## Similar Problems

| Number | Difficulty | Name | LeetCode |
|---|---|---|---|
| 0041 | Hard | [First Missing Positive](../0041-first-missing-positive/readme.md) | [First Missing Positive](https://leetcode.com/problems/first-missing-positive/) |
| 0136 | Easy | [Single Number](../0136-single-number/readme.md) | [Single Number](https://leetcode.com/problems/single-number/) |
| 0287 | Medium | [Find the Duplicate Number](../0287-find-the-duplicate-number/readme.md) | [Find the Duplicate Number](https://leetcode.com/problems/find-the-duplicate-number/) |
| 0765 | Hard | [Couples Holding Hands](../0765-couples-holding-hands/readme.md) | [Couples Holding Hands](https://leetcode.com/problems/couples-holding-hands/) |
| 1980 | Medium | [Find Unique Binary String](../1980-find-unique-binary-string/readme.md) | [Find Unique Binary String](https://leetcode.com/problems/find-unique-binary-string/) |
| 3471 | Easy | [Find the Largest Almost Missing Integer](../3471-find-the-largest-almost-missing-integer/readme.md) | [Find the Largest Almost Missing Integer](https://leetcode.com/problems/find-the-largest-almost-missing-integer/) |

## Examples

None

## References

- LeetCode problem and editorial links
