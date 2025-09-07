# 0066. Plus One

## Quick Facts

- URL: [Plus One](https://leetcode.com/problems/plus-one/)
- Function: `plusOne`
- Signature: `(digits: list[int])  -> list[int]`
- Primary pattern: **Math**

## Constraints

- `1 <= digits.length <= 100`
- `0 <= digits[i] <= 9`
- `digits does not contain any leading 0's.`

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
- Run: `pytest -q -k "0066"`

## Common Pitfalls

- [pitfall 1]
- [pitfall 2]
- [pitfall 3]

## Similar Problems

| Number | Difficulty | Name | LeetCode |
|---|---|---|---|
| 0043 | Medium | [Multiply Strings](../0043-multiply-strings/readme.md) | [Multiply Strings](https://leetcode.com/problems/multiply-strings/) |
| 0067 | Easy | [Add Binary](../0067-add-binary/readme.md) | [Add Binary](https://leetcode.com/problems/add-binary/) |
| 0369 | Medium | [Plus One Linked List](../0369-plus-one-linked-list/readme.md) | [Plus One Linked List](https://leetcode.com/problems/plus-one-linked-list/) |
| 1031 | Easy | [Add to Array-Form of Integer](../1031-add-to-array-form-of-integer/readme.md) | [Add to Array-Form of Integer](https://leetcode.com/problems/add-to-array-form-of-integer/) |
| 2710 | Medium | [Minimum Operations to Reduce an Integer to 0](../2710-minimum-operations-to-reduce-an-integer-to-0/readme.md) | [Minimum Operations to Reduce an Integer to 0](https://leetcode.com/problems/minimum-operations-to-reduce-an-integer-to-0/) |

## Examples

### Example 1

```text
Input: digits = [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.
Incrementing by one gives 123 + 1 = 124.
Thus, the result should be [1,2,4].
```

### Example 2

```text
Input: digits = [4,3,2,1]
Output: [4,3,2,2]
Explanation: The array represents the integer 4321.
Incrementing by one gives 4321 + 1 = 4322.
Thus, the result should be [4,3,2,2].
```

### Example 3

```text
Input: digits = [9]
Output: [1,0]
Explanation: The array represents the integer 9.
Incrementing by one gives 9 + 1 = 10.
Thus, the result should be [1,0].
```

## References

- LeetCode problem and editorial links
