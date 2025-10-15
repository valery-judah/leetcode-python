# 0978. Longest Turbulent Subarray

## Quick Facts

- URL: [Longest Turbulent Subarray](https://leetcode.com/problems/longest-turbulent-subarray/)
- Function: `maxTurbulenceSize`
- Signature: `(arr: list[int])  -> int`
- Primary pattern: **Sliding Window**

## Constraints

- `1 <= arr.length <= 4 * 10^4`
- `0 <= arr[i] <= 10^9`

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
- Run: `pytest -q -k "0978"`

## Common Pitfalls

- [pitfall 1]
- [pitfall 2]
- [pitfall 3]

## Similar Problems

| Number | Difficulty | Name                                                                           | LeetCode                                                                                    |
| ------ | ---------- | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------- |
| 0053   | Medium     | [Maximum Subarray](../0053-maximum-subarray/readme.md)                         | [Maximum Subarray](https://leetcode.com/problems/maximum-subarray/)                         |
| 2765   | Easy       | [Longest Alternating Subarray](../2765-longest-alternating-subarray/readme.md) | [Longest Alternating Subarray](https://leetcode.com/problems/longest-alternating-subarray/) |

## Examples

### Example 1

```text
Input: arr = [9,4,2,10,7,8,8,1,9]
Output: 5
Explanation: arr[1] > arr[2] < arr[3] > arr[4] < arr[5]
```

### Example 2

```text
Input: arr = [4,8,12,16]
Output: 2
```

### Example 3

```text
Input: arr = [100]
Output: 1
```

## References

- LeetCode problem and editorial links
