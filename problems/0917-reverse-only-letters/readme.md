# 0917. Reverse Only Letters

## Quick Facts

- URL: [Reverse Only Letters](https://leetcode.com/problems/reverse-only-letters/)
- Function: `reverseOnlyLetters`
- Signature: `(s: str)  -> str`
- Primary pattern: **Two Pointers**

## Constraints

- `1 <= s.length <= 100`
- `s consists of characters with ASCII values in the range [33, 122].`
- `s does not contain '\"' or '\\'.`

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
- Run: `pytest -q -k "0917"`

## Common Pitfalls

- [pitfall 1]
- [pitfall 2]
- [pitfall 3]

## Similar Problems

| Number | Difficulty | Name                                                 | LeetCode                                                          |
| ------ | ---------- | ---------------------------------------------------- | ----------------------------------------------------------------- |
| 2810   | Easy       | [Faulty Keyboard](../2810-faulty-keyboard/readme.md) | [Faulty Keyboard](https://leetcode.com/problems/faulty-keyboard/) |

## Examples

### Example 1

```text
Input: s = "ab-cd"
Output: "dc-ba"
```

### Example 2

```text
Input: s = "a-bC-dEf-ghIj"
Output: "j-Ih-gfE-dCba"
```

### Example 3

```text
Input: s = "Test1ng-Leet=code-Q!"
Output: "Qedo1ct-eeLg=ntse-T!"
```

## References

- LeetCode problem and editorial links
