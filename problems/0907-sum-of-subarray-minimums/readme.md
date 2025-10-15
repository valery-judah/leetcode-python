# 0907. Sum of Subarray Minimums

## Quick Facts

- URL: [Sum of Subarray Minimums](https://leetcode.com/problems/sum-of-subarray-minimums/)
- Function: `sumSubarrayMins`
- Signature: `(arr: list[int])  -> int`
- Primary pattern: **Stack**

## Constraints

- `1 <= arr.length <= 3 * 10^4`
- `1 <= arr[i] <= 3 * 10^4`

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
- Run: `pytest -q -k "0907"`

## Common Pitfalls

- [pitfall 1]
- [pitfall 2]
- [pitfall 3]

## Similar Problems

| Number | Difficulty | Name                                                                                   | LeetCode                                                                                            |
| ------ | ---------- | -------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------- |
| 2104   | Medium     | [Sum of Subarray Ranges](../2104-sum-of-subarray-ranges/readme.md)                     | [Sum of Subarray Ranges](https://leetcode.com/problems/sum-of-subarray-ranges/)                     |
| 2281   | Hard       | [Sum of Total Strength of Wizards](../2281-sum-of-total-strength-of-wizards/readme.md) | [Sum of Total Strength of Wizards](https://leetcode.com/problems/sum-of-total-strength-of-wizards/) |

## Examples

### Example 1

```text
Input: arr = [3,1,2,4]
Output: 17
Explanation:
Subarrays are [3], [1], [2], [4], [3,1], [1,2], [2,4], [3,1,2], [1,2,4], [3,1,2,4].
Minimums are 3, 1, 2, 4, 1, 1, 2, 1, 1, 1.
Sum is 17.
```

### Example 2

```text
Input: arr = [11,81,94,43,3]
Output: 444
```

## References

- LeetCode problem and editorial links
