# 0043. Multiply Strings

## Quick Facts

- URL: [Multiply Strings](https://leetcode.com/problems/multiply-strings/)
- Function: `multiply`
- Signature: `(num1: str, num2: str)  -> str`
- Primary pattern: **Math**

## Constraints

- `1 <= num1.length, num2.length <= 200`
- `num1 and num2 consist of digits only.`
- `Both num1 and num2 do not contain any leading zero, except the number 0 itself.`

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
- Run: `pytest -q -k "0043"`

## Common Pitfalls

- [pitfall 1]
- [pitfall 2]
- [pitfall 3]

## Similar Problems

| Number | Difficulty | Name | LeetCode |
|---|---|---|---|
| 0002 | Medium | [Add Two Numbers](../0002-add-two-numbers/readme.md) | [Add Two Numbers](https://leetcode.com/problems/add-two-numbers/) |
| 0066 | Easy | [Plus One](../0066-plus-one/readme.md) | [Plus One](https://leetcode.com/problems/plus-one/) |
| 0067 | Easy | [Add Binary](../0067-add-binary/readme.md) | [Add Binary](https://leetcode.com/problems/add-binary/) |
| 0415 | Easy | [Add Strings](../0415-add-strings/readme.md) | [Add Strings](https://leetcode.com/problems/add-strings/) |
| 2373 | Medium | [Apply Discount to Prices](../2373-apply-discount-to-prices/readme.md) | [Apply Discount to Prices](https://leetcode.com/problems/apply-discount-to-prices/) |

## Examples

### Example 1

```text
Input: num1 = "2", num2 = "3"
Output: "6"
```

### Example 2

```text
Input: num1 = "123", num2 = "456"
Output: "56088"
```

## References

- LeetCode problem and editorial links
