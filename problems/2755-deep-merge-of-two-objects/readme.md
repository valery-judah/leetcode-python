# 2755. Deep Merge of Two Objects

## Quick Facts

- URL: [Deep Merge of Two Objects](https://leetcode.com/problems/deep-merge-of-two-objects/)
- Function: `deepMerge`
- Signature: `(obj1: str, obj2: str)  -> str`
- Primary pattern: ****

## Constraints

- `obj1 and obj2 are valid JSON values`
- `1 <= JSON.stringify(obj1).length <= 5 * 10^5`
- `1 <= JSON.stringify(obj2).length <= 5 * 10^5`

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
- Run: `pytest -q -k "2755"`

## Common Pitfalls

- [pitfall 1]
- [pitfall 2]
- [pitfall 3]

## Similar Problems

None

## Examples

### Example 1

```text
Input: obj1 = {{"a": 1, "c": 3}}, obj2 = {{"a": 2, "b": 2}}
Output: {{"a": 2, "c": 3, "b": 2}}
Explanation: The value of obj1["a"] changed to 2 because if both objects have the same key and their value is not an array or object then we change the obj1 value to the obj2 value. Key "b" with value was added to obj1 as it doesn't exist in obj1.
```

### Example 2

```text
Input: obj1 = [{{}}, 2, 3], obj2 = [[], 5]
Output: [[], 5, 3]
Explanation: result[0] = obj2[0] because obj1[0] and obj2[0] have different types. result[2] = obj1[2] because obj2[2] does not exist.
```

### Example 3

```text
Input: 
obj1 = {{"a": 1, "b": {{"c": [1 , [2, 7], 5], "d": 2}}}}, 
obj2 = {{"a": 1, "b": {{"c": [6, [6], [9]], "e": 3}}}}
Output: {{"a": 1, "b": {{"c": [6, [6, 7], [9]], "d": 2, "e": 3}}}}
Explanation: 
Arrays obj1["b"]["c"] and obj2["b"]["c"] have been merged in way that obj2 values overwrite obj1 values deeply only if they are not arrays or objects.
obj2["b"]["c"] has key "e" that obj1 doesn't have so it's added to obj1.
```

### Example 4

```text
Input: obj1 = true, obj2 = null
Output: null
```

## References

- LeetCode problem and editorial links
