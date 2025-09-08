# 1095. Find in Mountain Array

## Quick Facts

- URL: [Find in Mountain Array](https://leetcode.com/problems/find-in-mountain-array/)
- Function: `findInMountainArray`
- Signature: `(mountainArr: list[int], target: int)  -> int`
- Primary pattern: **Binary Search**

## Constraints

- `3 <= mountainArr.length() <= 10^4`
- `0 <= target <= 10^9`
- `0 <= mountainArr.get(index) <= 10^9`

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
- Run: `pytest -q -k "1095"`

## Common Pitfalls

- [pitfall 1]
- [pitfall 2]
- [pitfall 3]

## Similar Problems

| Number | Difficulty | Name | LeetCode |
|---|---|---|---|
| 0852 | Medium | [Peak Index in a Mountain Array](../0852-peak-index-in-a-mountain-array/readme.md) | [Peak Index in a Mountain Array](https://leetcode.com/problems/peak-index-in-a-mountain-array/) |
| 1671 | Hard | [Minimum Number of Removals to Make Mountain Array](../1671-minimum-number-of-removals-to-make-mountain-array/readme.md) | [Minimum Number of Removals to Make Mountain Array](https://leetcode.com/problems/minimum-number-of-removals-to-make-mountain-array/) |
| 2100 | Medium | [Find Good Days to Rob the Bank](../2100-find-good-days-to-rob-the-bank/readme.md) | [Find Good Days to Rob the Bank](https://leetcode.com/problems/find-good-days-to-rob-the-bank/) |
| 3285 | Easy | [Find Indices of Stable Mountains](../3285-find-indices-of-stable-mountains/readme.md) | [Find Indices of Stable Mountains](https://leetcode.com/problems/find-indices-of-stable-mountains/) |

## Examples

### Example 1

```text
Input: mountainArr = [1,2,3,4,5,3,1], target = 3
Output: 2
Explanation: 3 exists in the array, at index=2 and index=5. Return the minimum index, which is 2.
```

### Example 2

```text
Input: mountainArr = [0,1,2,4,2,1], target = 3
Output: -1
Explanation: 3 does not exist in the array, so we return -1.
```

## References

- LeetCode problem and editorial links
