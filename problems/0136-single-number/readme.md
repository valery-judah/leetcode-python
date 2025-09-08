# 0136. Single Number

## Quick Facts

- URL: [Single Number](https://leetcode.com/problems/single-number/)
- Function: `singleNumber`
- Signature: `(nums: list[int])  -> int`
- Primary pattern: **Bit Manipulation**

## Constraints

- `1 <= nums.length <= 3 * 10^4`
- `-3 * 10^4 <= nums[i] <= 3 * 10^4`
- `Each element in the array appears twice except for one element which appears only once.`

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
- Run: `pytest -q -k "0136"`

## Common Pitfalls

- [pitfall 1]
- [pitfall 2]
- [pitfall 3]

## Similar Problems

| Number | Difficulty | Name | LeetCode |
|---|---|---|---|
| 0137 | Medium | [Single Number II](../0137-single-number-ii/readme.md) | [Single Number II](https://leetcode.com/problems/single-number-ii/) |
| 0260 | Medium | [Single Number III](../0260-single-number-iii/readme.md) | [Single Number III](https://leetcode.com/problems/single-number-iii/) |
| 0268 | Easy | [Missing Number](../0268-missing-number/readme.md) | [Missing Number](https://leetcode.com/problems/missing-number/) |
| 0287 | Medium | [Find the Duplicate Number](../0287-find-the-duplicate-number/readme.md) | [Find the Duplicate Number](https://leetcode.com/problems/find-the-duplicate-number/) |
| 0389 | Easy | [Find the Difference](../0389-find-the-difference/readme.md) | [Find the Difference](https://leetcode.com/problems/find-the-difference/) |
| 3158 | Easy | [Find the XOR of Numbers Which Appear Twice](../3158-find-the-xor-of-numbers-which-appear-twice/readme.md) | [Find the XOR of Numbers Which Appear Twice](https://leetcode.com/problems/find-the-xor-of-numbers-which-appear-twice/) |

## Examples

None

## References

- LeetCode problem and editorial links
