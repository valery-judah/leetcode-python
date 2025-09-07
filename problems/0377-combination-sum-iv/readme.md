# 0377. Combination Sum IV

## Quick Facts

- URL: [Combination Sum IV](https://leetcode.com/problems/combination-sum-iv/)
- Function: `combinationSum4`
- Signature: `(nums: list[int], target: int)  -> int`
- Primary pattern: **Dynamic Programming**

## Constraints

- `1 <= nums.length <= 200`
- `1 <= nums[i] <= 1000`
- `All the elements of nums are unique.`
- `1 <= target <= 1000`

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
- Run: `pytest -q -k "0377"`

## Common Pitfalls

- [pitfall 1]
- [pitfall 2]
- [pitfall 3]

## Similar Problems

| Number | Difficulty | Name | LeetCode |
|---|---|---|---|
| 0039 | Medium | [Combination Sum](../0039-combination-sum/readme.md) | [Combination Sum](https://leetcode.com/problems/combination-sum/) |
| 2787 | Medium | [Ways to Express an Integer as Sum of Powers](../2787-ways-to-express-an-integer-as-sum-of-powers/readme.md) | [Ways to Express an Integer as Sum of Powers](https://leetcode.com/problems/ways-to-express-an-integer-as-sum-of-powers/) |

## Examples

### Example 1

```text
Input: nums = [1,2,3], target = 4
Output: 7
Explanation:
The possible combination ways are:
(1, 1, 1, 1)
(1, 1, 2)
(1, 2, 1)
(1, 3)
(2, 1, 1)
(2, 2)
(3, 1)
Note that different sequences are counted as different combinations.
```

### Example 2

```text
Input: nums = [9], target = 3
Output: 0
```

## References

- LeetCode problem and editorial links
