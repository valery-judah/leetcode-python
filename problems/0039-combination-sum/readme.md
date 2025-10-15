# 0039. Combination Sum

## Quick Facts

- URL: [Combination Sum](https://leetcode.com/problems/combination-sum/)
- Function: `combinationSum`
- Signature: `(candidates: list[int], target: int)  -> list[list[int]]`
- Primary pattern: **Backtracking**

## Constraints

- `1 <= candidates.length <= 30`
- `2 <= candidates[i] <= 40`
- `All elements of candidates are distinct.`
- `1 <= target <= 40`

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
- Run: `pytest -q -k "0039"`

## Common Pitfalls

- [pitfall 1]
- [pitfall 2]
- [pitfall 3]

## Similar Problems

| Number | Difficulty | Name                                                                                             | LeetCode                                                                                                      |
| ------ | ---------- | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------- |
| 0017   | Medium     | [Letter Combinations of a Phone Number](../0017-letter-combinations-of-a-phone-number/readme.md) | [Letter Combinations of a Phone Number](https://leetcode.com/problems/letter-combinations-of-a-phone-number/) |
| 0040   | Medium     | [Combination Sum II](../0040-combination-sum-ii/readme.md)                                       | [Combination Sum II](https://leetcode.com/problems/combination-sum-ii/)                                       |
| 0077   | Medium     | [Combinations](../0077-combinations/readme.md)                                                   | [Combinations](https://leetcode.com/problems/combinations/)                                                   |
| 0216   | Medium     | [Combination Sum III](../0216-combination-sum-iii/readme.md)                                     | [Combination Sum III](https://leetcode.com/problems/combination-sum-iii/)                                     |
| 0254   | Medium     | [Factor Combinations](../0254-factor-combinations/readme.md)                                     | [Factor Combinations](https://leetcode.com/problems/factor-combinations/)                                     |
| 0377   | Medium     | [Combination Sum IV](../0377-combination-sum-iv/readme.md)                                       | [Combination Sum IV](https://leetcode.com/problems/combination-sum-iv/)                                       |
| 3183   | Medium     | [The Number of Ways to Make the Sum](../3183-the-number-of-ways-to-make-the-sum/readme.md)       | [The Number of Ways to Make the Sum](https://leetcode.com/problems/the-number-of-ways-to-make-the-sum/)       |

## Examples

### Example 1

```text
Input: candidates = [2,3,6,7], target = 7
Output: [[2,2,3],[7]]
Explanation:
2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
7 is a candidate, and 7 = 7.
These are the only two combinations.
```

### Example 2

```text
Input: candidates = [2,3,5], target = 8
Output: [[2,2,2,2],[2,3,3],[3,5]]
```

### Example 3

```text
Input: candidates = [2], target = 1
Output: []
```

## References

- LeetCode problem and editorial links
