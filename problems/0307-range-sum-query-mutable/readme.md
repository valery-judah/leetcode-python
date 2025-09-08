# 0307. Range Sum Query - Mutable

## Quick Facts

- URL: [Range Sum Query - Mutable](https://leetcode.com/problems/range-sum-query-mutable/)
- Function: ``
- Signature: `(inputs: list[int], inputs: list[int])  -> list[str]`
- Primary pattern: **Array**

## Constraints

- `1 <= nums.length <= 3 * 10^4`
- `-100 <= nums[i] <= 100`
- `0 <= index < nums.length`
- `-100 <= val <= 100`
- `0 <= left <= right < nums.length`
- `At most 3 * 10^4 calls will be made to update and sumRange.`

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
- Run: `pytest -q -k "0307"`

## Common Pitfalls

- [pitfall 1]
- [pitfall 2]
- [pitfall 3]

## Similar Problems

| Number | Difficulty | Name | LeetCode |
|---|---|---|---|
| 0303 | Easy | [Range Sum Query - Immutable](../0303-range-sum-query-immutable/readme.md) | [Range Sum Query - Immutable](https://leetcode.com/problems/range-sum-query-immutable/) |
| 0308 | Medium | [Range Sum Query 2D - Mutable](../0308-range-sum-query-2d-mutable/readme.md) | [Range Sum Query 2D - Mutable](https://leetcode.com/problems/range-sum-query-2d-mutable/) |
| 2381 | Medium | [Shifting Letters II](../2381-shifting-letters-ii/readme.md) | [Shifting Letters II](https://leetcode.com/problems/shifting-letters-ii/) |

## Examples

### Example 1

```text
Input
["NumArray", "sumRange", "update", "sumRange"]
[[[1, 3, 5]], [0, 2], [1, 2], [0, 2]]
Output
[null, 9, null, 8]

Explanation
NumArray numArray = new NumArray([1, 3, 5]);
numArray.sumRange(0, 2); // return 1 + 3 + 5 = 9
numArray.update(1, 2);   // nums = [1, 2, 5]
numArray.sumRange(0, 2); // return 1 + 2 + 5 = 8
```

## References

- LeetCode problem and editorial links
