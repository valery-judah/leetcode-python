# 0075. Sort Colors

## Quick Facts

- URL: [Sort Colors](https://leetcode.com/problems/sort-colors/)
- Function: `sortColors`
- Signature: `(nums: list[int])  -> None`
- Primary pattern: **Two Pointers**

## Constraints

- `n == nums.length`
- `1 <= n <= 300`
- `nums[i] is either 0, 1, or 2.`

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
- Run: `pytest -q -k "0075"`

## Common Pitfalls

- [pitfall 1]
- [pitfall 2]
- [pitfall 3]

## Similar Problems

| Number | Difficulty | Name | LeetCode |
|---|---|---|---|
| 0148 | Medium | [Sort List](../0148-sort-list/readme.md) | [Sort List](https://leetcode.com/problems/sort-list/) |
| 0280 | Medium | [Wiggle Sort](../0280-wiggle-sort/readme.md) | [Wiggle Sort](https://leetcode.com/problems/wiggle-sort/) |
| 0324 | Medium | [Wiggle Sort II](../0324-wiggle-sort-ii/readme.md) | [Wiggle Sort II](https://leetcode.com/problems/wiggle-sort-ii/) |

## Examples

### Example 1

```text
Input: nums = [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]
```

### Example 2

```text
Input: nums = [2,0,1]
Output: [0,1,2]
```

## References

- LeetCode problem and editorial links
