# 1618. Maximum Font to Fit a Sentence in a Screen

## Quick Facts

- URL: [Maximum Font to Fit a Sentence in a Screen](https://leetcode.com/problems/maximum-font-to-fit-a-sentence-in-a-screen/)
- Function: `maxFont`
- Signature: `(text: str, w: int, h: int, fonts: list[int])  -> int`
- Primary pattern: **Binary Search**

## Constraints

- `1 <= text.length <= 50000`
- `text contains only lowercase English letters.`
- `1 <= w <= 10^7`
- `1 <= h <= 10^4`
- `1 <= fonts.length <= 10^5`
- `1 <= fonts[i] <= 10^5`
- `fonts is sorted in ascending order and does not contain duplicates.`

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
- Run: `pytest -q -k "1618"`

## Common Pitfalls

- [pitfall 1]
- [pitfall 2]
- [pitfall 3]

## Similar Problems

None

## Examples

### Example 1

```text
interface FontInfo {{
  // Returns the width of character ch on the screen using font size fontSize.
  // O(1) per call
  public int getWidth(int fontSize, char ch);

  // Returns the height of any character on the screen using font size fontSize.
  // O(1) per call
  public int getHeight(int fontSize);
}}
```

### Example 2

```text
Input: text = "helloworld", w = 80, h = 20, fonts = [6,8,10,12,14,16,18,24,36]
Output: 6
```

### Example 3

```text
Input: text = "leetcode", w = 1000, h = 50, fonts = [1,2,4]
Output: 4
```

### Example 4

```text
Input: text = "easyquestion", w = 100, h = 100, fonts = [10,15,20,25]
Output: -1
```

## References

- LeetCode problem and editorial links
