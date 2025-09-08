# 0283. Move Zeroes

## Quick Facts

- URL: [Move Zeroes](https://leetcode.com/problems/move-zeroes/)
- Function: `moveZeroes`
- Signature: `(nums: list[int])  -> None`
- Primary pattern: **Two Pointers**

## Constraints

- `1 <= nums.length <= 10^4`
- `-2^31 <= nums[i] <= 2^31 - 1`

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
- Run: `pytest -q -k "0283"`

## Common Pitfalls

- [pitfall 1]
- [pitfall 2]
- [pitfall 3]

## Similar Problems

| Number | Difficulty | Name | LeetCode |
|---|---|---|---|
| 0027 | Easy | [Remove Element](../0027-remove-element/readme.md) | [Remove Element](https://leetcode.com/problems/remove-element/) |
| 2460 | Easy | [Apply Operations to an Array](../2460-apply-operations-to-an-array/readme.md) | [Apply Operations to an Array](https://leetcode.com/problems/apply-operations-to-an-array/) |

## Examples

### Example 1

```text
Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]
```

### Example 2

```text
Input: nums = [0]
Output: [0]
```

## References

- LeetCode problem and editorial links
