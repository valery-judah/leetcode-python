# 0067. Add Binary

## Quick Facts

- URL: [Add Binary](https://leetcode.com/problems/add-binary/)
- Function: `addBinary`
- Signature: `(a: str, b: str)  -> str`
- Primary pattern: **Math**

## Constraints

- `1 <= a.length, b.length <= 10^4`
- `a and b consist only of '0' or '1' characters.`
- `Each string does not contain leading zeros except for the zero itself.`

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
- Run: `pytest -q -k "0067"`

## Common Pitfalls

- [pitfall 1]
- [pitfall 2]
- [pitfall 3]

## Similar Problems

| Number | Difficulty | Name                                                                           | LeetCode                                                                                    |
| ------ | ---------- | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------- |
| 0002   | Medium     | [Add Two Numbers](../0002-add-two-numbers/readme.md)                           | [Add Two Numbers](https://leetcode.com/problems/add-two-numbers/)                           |
| 0043   | Medium     | [Multiply Strings](../0043-multiply-strings/readme.md)                         | [Multiply Strings](https://leetcode.com/problems/multiply-strings/)                         |
| 0066   | Easy       | [Plus One](../0066-plus-one/readme.md)                                         | [Plus One](https://leetcode.com/problems/plus-one/)                                         |
| 0989   | Easy       | [Add to Array-Form of Integer](../0989-add-to-array-form-of-integer/readme.md) | [Add to Array-Form of Integer](https://leetcode.com/problems/add-to-array-form-of-integer/) |

## Examples

### Example 1

```text
Input: a = "11", b = "1"
Output: "100"
```

### Example 2

```text
Input: a = "1010", b = "1011"
Output: "10101"
```

## References

- LeetCode problem and editorial links
