# 0163. Missing Ranges

## Quick Facts

- URL: [Missing Ranges](https://leetcode.com/problems/missing-ranges/)
- Function: `findMissingRanges`
- Signature: `(nums: list[int], lower: int, upper: int)  -> list[list[int]]`
- Primary pattern: **Array**

## Constraints

- `-10^9 <= lower <= upper <= 10^9`
- `0 <= nums.length <= 100`
- `lower <= nums[i] <= upper`
- `All the values of nums are unique.`

## Problem Crux (1–2 sentences)

[state what must be detected/computed and key bound]

## Clarifying Questions (for interview)

- [input domain? ranges?]
- [edge-case semantics?]
- [any pair vs first pair? ties?]

## Reasoning Flow (notes-only)

[outline the logical steps that lead to the chosen approach]

## Approach Options

| #   | Idea           | When to use | Correctness invariant | Time       | Space |
| --- | -------------- | ----------- | --------------------- | ---------- | ----- |
| A   | [primary idea] | [scenario]  | [invariant]           | O(n)       | O(n)  |
| B   | [alternative]  | [scenario]  | [invariant]           | O(n log n) | O(1)  |
| C   | [reject]       | [why not]   | [violated invariant]  | -          | -     |

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
- Run: `pytest -q -k "0163"`

## Common Pitfalls

- [pitfall 1]
- [pitfall 2]
- [pitfall 3]

## Similar Problems

| Number | Difficulty | Name                                                                             | LeetCode                                                                                      |
| ------ | ---------- | -------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- |
| 0228   | Easy       | [Summary Ranges](../0228-summary-ranges/readme.md)                               | [Summary Ranges](https://leetcode.com/problems/summary-ranges/)                               |
| 2655   | Medium     | [Find Maximal Uncovered Ranges](../2655-find-maximal-uncovered-ranges/readme.md) | [Find Maximal Uncovered Ranges](https://leetcode.com/problems/find-maximal-uncovered-ranges/) |

## Examples

### Example 1

```text
Input: nums = [0,1,3,50,75], lower = 0, upper = 99
Output: [[2,2],[4,49],[51,74],[76,99]]
Explanation: The ranges are:
[2,2]
[4,49]
[51,74]
[76,99]
```

### Example 2

```text
Input: nums = [-1], lower = -1, upper = -1
Output: []
Explanation: There are no missing ranges since there are no missing numbers.
```

## References

- LeetCode problem and editorial links
