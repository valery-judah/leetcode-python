# 0271. Encode and Decode Strings

## Quick Facts

- URL: [Encode and Decode Strings](https://leetcode.com/problems/encode-and-decode-strings/)
- Function: `encode`
- Signature: `(dummy_input: list[str])  -> list[str]`
- Primary pattern: **Array**

## Constraints

- `1 <= strs.length <= 200`
- `0 <= strs[i].length <= 200`
- `strs[i] contains any possible characters out of 256 valid ASCII characters.`

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
- Run: `pytest -q -k "0271"`

## Common Pitfalls

- [pitfall 1]
- [pitfall 2]
- [pitfall 3]

## Similar Problems

| Number | Difficulty | Name | LeetCode |
|---|---|---|---|
| 0038 | Medium | [Count and Say](../0038-count-and-say/readme.md) | [Count and Say](https://leetcode.com/problems/count-and-say/) |
| 0297 | Hard | [Serialize and Deserialize Binary Tree](../0297-serialize-and-deserialize-binary-tree/readme.md) | [Serialize and Deserialize Binary Tree](https://leetcode.com/problems/serialize-and-deserialize-binary-tree/) |
| 0443 | Medium | [String Compression](../0443-string-compression/readme.md) | [String Compression](https://leetcode.com/problems/string-compression/) |
| 0696 | Easy | [Count Binary Substrings](../0696-count-binary-substrings/readme.md) | [Count Binary Substrings](https://leetcode.com/problems/count-binary-substrings/) |

## Examples

### Example 1

```text
string encode(vector<string> strs) {{
  // ... your code
  return encoded_string;
}}
```

### Example 2

```text
vector<string> decode(string s) {{
  //... your code
  return strs;
}}
```

### Example 3

```text
string encoded_string = encode(strs);
```

### Example 4

```text
vector<string> strs2 = decode(encoded_string);
```

### Example 5

```text
Input: dummy_input = ["Hello","World"]
Output: ["Hello","World"]
Explanation:
Machine 1:
Codec encoder = new Codec();
String msg = encoder.encode(strs);
Machine 1 ---msg---> Machine 2

Machine 2:
Codec decoder = new Codec();
String[] strs = decoder.decode(msg);
```

### Example 6

```text
Input: dummy_input = [""]
Output: [""]
```

## References

- LeetCode problem and editorial links
