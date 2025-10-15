# 0905. Sort Array By Parity

## Quick Facts

- URL: [Sort Array By Parity](https://leetcode.com/problems/sort-array-by-parity/)
- Function: `sortArrayByParity`
- Signature: `(nums: list[int])  -> list[int]`
- Primary pattern: **Two Pointers**

## Constraints

- `1 <= nums.length <= 5000`
- `0 <= nums[i] <= 5000`

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
- Run: `pytest -q -k "0905"`

## Common Pitfalls

- [pitfall 1]
- [pitfall 2]
- [pitfall 3]

## Similar Problems

| Number | Difficulty | Name                                                                                                       | LeetCode                                                                                                                |
| ------ | ---------- | ---------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------- |
| 0922   | Easy       | [Sort Array By Parity II](../0922-sort-array-by-parity-ii/readme.md)                                       | [Sort Array By Parity II](https://leetcode.com/problems/sort-array-by-parity-ii/)                                       |
| 2164   | Easy       | [Sort Even and Odd Indices Independently](../2164-sort-even-and-odd-indices-independently/readme.md)       | [Sort Even and Odd Indices Independently](https://leetcode.com/problems/sort-even-and-odd-indices-independently/)       |
| 2231   | Easy       | [Largest Number After Digit Swaps by Parity](../2231-largest-number-after-digit-swaps-by-parity/readme.md) | [Largest Number After Digit Swaps by Parity](https://leetcode.com/problems/largest-number-after-digit-swaps-by-parity/) |

## Examples

### Example 1

```text
Input: nums = [3,1,2,4]
Output: [2,4,3,1]
Explanation: The outputs [4,2,3,1], [2,4,1,3], and [4,2,1,3] would also be accepted.
```

### Example 2

```text
Input: nums = [0]
Output: [0]
```

## References

- LeetCode problem and editorial links
