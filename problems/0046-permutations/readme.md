# 0046. Permutations

## Quick Facts

- URL: [Permutations](https://leetcode.com/problems/permutations/)
- Function: `permute`
- Signature: `(nums: list[int])  -> list[list[int]]`
- Primary pattern: **Backtracking**

## Constraints

- `1 <= nums.length <= 6`
- `-10 <= nums[i] <= 10`
- `All the integers of nums are unique.`

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
- Run: `pytest -q -k "0046"`

## Common Pitfalls

- [pitfall 1]
- [pitfall 2]
- [pitfall 3]

## Similar Problems

| Number | Difficulty | Name | LeetCode |
|---|---|---|---|
| 0031 | Medium | [Next Permutation](../0031-next-permutation/readme.md) | [Next Permutation](https://leetcode.com/problems/next-permutation/) |
| 0047 | Medium | [Permutations II](../0047-permutations-ii/readme.md) | [Permutations II](https://leetcode.com/problems/permutations-ii/) |
| 0060 | Hard | [Permutation Sequence](../0060-permutation-sequence/readme.md) | [Permutation Sequence](https://leetcode.com/problems/permutation-sequence/) |
| 0077 | Medium | [Combinations](../0077-combinations/readme.md) | [Combinations](https://leetcode.com/problems/combinations/) |

## Examples

### Example 1

```text
Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
```

### Example 2

```text
Input: nums = [0,1]
Output: [[0,1],[1,0]]
```

### Example 3

```text
Input: nums = [1]
Output: [[1]]
```

## References

- LeetCode problem and editorial links
