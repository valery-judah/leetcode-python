# 0090. Subsets II

## Quick Facts

- URL: [Subsets II](https://leetcode.com/problems/subsets-ii/)
- Function: `subsetsWithDup`
- Signature: `(nums: list[int])  -> list[list[int]]`
- Primary pattern: **Backtracking**

## Constraints

- `1 <= nums.length <= 10`
- `-10 <= nums[i] <= 10`

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
- Run: `pytest -q -k "0090"`

## Common Pitfalls

- [pitfall 1]
- [pitfall 2]
- [pitfall 3]

## Similar Problems

| Number | Difficulty | Name | LeetCode |
|---|---|---|---|
| 0078 | Medium | [Subsets](../0078-subsets/readme.md) | [Subsets](https://leetcode.com/problems/subsets/) |
| 2109 | Hard | [Find Array Given Subset Sums](../2109-find-array-given-subset-sums/readme.md) | [Find Array Given Subset Sums](https://leetcode.com/problems/find-array-given-subset-sums/) |

## Examples

### Example 1

```text
Input: nums = [1,2,2]
Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]
```

### Example 2

```text
Input: nums = [0]
Output: [[],[0]]
```

## References

- LeetCode problem and editorial links
