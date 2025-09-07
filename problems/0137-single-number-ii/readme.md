# 0137. Single Number II

## Quick Facts

- URL: [Single Number II](https://leetcode.com/problems/single-number-ii/)
- Function: `singleNumber`
- Signature: `(nums: list[int])  -> int`
- Primary pattern: **Bit Manipulation**

## Constraints

- `1 <= nums.length <= 3 * 10^4`
- `-2^31 <= nums[i] <= 2^31 - 1`
- `Each element in nums appears exactly three times except for one element which appears once.`

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
- Run: `pytest -q -k "0137"`

## Common Pitfalls

- [pitfall 1]
- [pitfall 2]
- [pitfall 3]

## Similar Problems

| Number | Difficulty | Name | LeetCode |
|---|---|---|---|
| 0136 | Easy | [Single Number](../0136-single-number/readme.md) | [Single Number](https://leetcode.com/problems/single-number/) |
| 0260 | Medium | [Single Number III](../0260-single-number-iii/readme.md) | [Single Number III](https://leetcode.com/problems/single-number-iii/) |
| 3428 | Easy | [Find the XOR of Numbers Which Appear Twice](../3428-find-the-xor-of-numbers-which-appear-twice/readme.md) | [Find the XOR of Numbers Which Appear Twice](https://leetcode.com/problems/find-the-xor-of-numbers-which-appear-twice/) |

## Examples

### Example 1

```text
Input: nums = [2,2,3,2]
Output: 3
```

### Example 2

```text
Input: nums = [0,1,0,1,0,1,99]
Output: 99
```

## References

- LeetCode problem and editorial links
