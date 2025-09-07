# 0146. LRU Cache

## Quick Facts

- URL: [LRU Cache](https://leetcode.com/problems/lru-cache/)
- Function: \`\`
- Signature: `(inputs: list[int], inputs: list[int])  -> list[str]`
- Primary pattern: **Hash Table**

## Constraints

- `1 <= capacity <= 3000`
- `0 <= key <= 10^4`
- `0 <= value <= 10^5`
- `At most 2 * 10^5 calls will be made to get and put.`

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
- Run: `pytest -q -k "0146"`

## Common Pitfalls

- [pitfall 1]
- [pitfall 2]
- [pitfall 3]

## Similar Problems

| Number | Difficulty | Name | LeetCode |
|---|---|---|---|
| 0460 | Hard | [LFU Cache](../0460-lfu-cache/readme.md) | [LFU Cache](https://leetcode.com/problems/lfu-cache/) |
| 0588 | Hard | [Design In-Memory File System](../0588-design-in-memory-file-system/readme.md) | [Design In-Memory File System](https://leetcode.com/problems/design-in-memory-file-system/) |
| 0604 | Easy | [Design Compressed String Iterator](../0604-design-compressed-string-iterator/readme.md) | [Design Compressed String Iterator](https://leetcode.com/problems/design-compressed-string-iterator/) |
| 1903 | Medium | [Design Most Recently Used Queue](../1903-design-most-recently-used-queue/readme.md) | [Design Most Recently Used Queue](https://leetcode.com/problems/design-most-recently-used-queue/) |

## Examples

### Example 1

```text
Input
["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
[[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
Output
[null, null, null, 1, null, -1, null, -1, 3, 4]

Explanation
LRUCache lRUCache = new LRUCache(2);
lRUCache.put(1, 1); // cache is {{1=1}}
lRUCache.put(2, 2); // cache is {{1=1, 2=2}}
lRUCache.get(1);    // return 1
lRUCache.put(3, 3); // LRU key was 2, evicts key 2, cache is {{1=1, 3=3}}
lRUCache.get(2);    // returns -1 (not found)
lRUCache.put(4, 4); // LRU key was 1, evicts key 1, cache is {{4=4, 3=3}}
lRUCache.get(1);    // return -1 (not found)
lRUCache.get(3);    // return 3
lRUCache.get(4);    // return 4
```

## References

- LeetCode problem and editorial links
