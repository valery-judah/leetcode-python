# 0078. Subsets

## Quick Facts

- URL: [Subsets](https://leetcode.com/problems/subsets/)
- Function: `subsets`
- Signature: `(nums: list[int])  -> list[list[int]]`
- Primary pattern: **Backtracking**

## Constraints

- `1 <= nums.length <= 10`
- `-10 <= nums[i] <= 10`
- `All the numbers of nums are unique.`

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
- Run: `pytest -q -k "0078"`

## Common Pitfalls

- [pitfall 1]
- [pitfall 2]
- [pitfall 3]

## Similar Problems

| Number | Difficulty | Name | LeetCode |
|---|---|---|---|
| 0090 | Medium | [Subsets II](../0090-subsets-ii/readme.md) | [Subsets II](https://leetcode.com/problems/subsets-ii/) |
| 0320 | Medium | [Generalized Abbreviation](../0320-generalized-abbreviation/readme.md) | [Generalized Abbreviation](https://leetcode.com/problems/generalized-abbreviation/) |
| 0800 | Medium | [Letter Case Permutation](../0800-letter-case-permutation/readme.md) | [Letter Case Permutation](https://leetcode.com/problems/letter-case-permutation/) |
| 2109 | Hard | [Find Array Given Subset Sums](../2109-find-array-given-subset-sums/readme.md) | [Find Array Given Subset Sums](https://leetcode.com/problems/find-array-given-subset-sums/) |
| 2170 | Medium | [Count Number of Maximum Bitwise-OR Subsets](../2170-count-number-of-maximum-bitwise-or-subsets/readme.md) | [Count Number of Maximum Bitwise-OR Subsets](https://leetcode.com/problems/count-number-of-maximum-bitwise-or-subsets/) |

## Examples

### Example 1

```text
Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
```

### Example 2

```text
Input: nums = [0]
Output: [[],[0]]
```

## References

- LeetCode problem and editorial links
