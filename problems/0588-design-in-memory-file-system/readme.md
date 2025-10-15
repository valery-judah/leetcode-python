# 0588. Design In-Memory File System

## Quick Facts

- URL: [Design In-Memory File System](https://leetcode.com/problems/design-in-memory-file-system/)
- Function: \`\`
- Signature: `(inputs: list[int], inputs: list[int])  -> list[str]`
- Primary pattern: **Hash Table**

## Constraints

- `1 <= path.length, filePath.length <= 100`
- `path and filePath are absolute paths which begin with '/' and do not end with '/' except that the path is just "/".`
- `You can assume that all directory names and file names only contain lowercase letters, and the same names will not exist in the same directory.`
- `You can assume that all operations will be passed valid parameters, and users will not attempt to retrieve file content or list a directory or file that does not exist.`
- `You can assume that the parent directory for the file in addContentToFile will exist.`
- `1 <= content.length <= 50`
- `At most 300 calls will be made to ls, mkdir, addContentToFile, and readContentFromFile.`

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
- Run: `pytest -q -k "0588"`

## Common Pitfalls

- [pitfall 1]
- [pitfall 2]
- [pitfall 3]

## Similar Problems

| Number | Difficulty | Name                                                                     | LeetCode                                                                              |
| ------ | ---------- | ------------------------------------------------------------------------ | ------------------------------------------------------------------------------------- |
| 0146   | Medium     | [LRU Cache](../0146-lru-cache/readme.md)                                 | [LRU Cache](https://leetcode.com/problems/lru-cache/)                                 |
| 0460   | Hard       | [LFU Cache](../0460-lfu-cache/readme.md)                                 | [LFU Cache](https://leetcode.com/problems/lfu-cache/)                                 |
| 0635   | Medium     | [Design Log Storage System](../0635-design-log-storage-system/readme.md) | [Design Log Storage System](https://leetcode.com/problems/design-log-storage-system/) |

## Examples

### Example 1

```text
Input
["FileSystem", "ls", "mkdir", "addContentToFile", "ls", "readContentFromFile"]
[[], ["/"], ["/a/b/c"], ["/a/b/c/d", "hello"], ["/"], ["/a/b/c/d"]]
Output
[null, [], null, null, ["a"], "hello"]

Explanation
FileSystem fileSystem = new FileSystem();
fileSystem.ls("/");                         // return []
fileSystem.mkdir("/a/b/c");
fileSystem.addContentToFile("/a/b/c/d", "hello");
fileSystem.ls("/");                         // return ["a"]
fileSystem.readContentFromFile("/a/b/c/d"); // return "hello"
```

## References

- LeetCode problem and editorial links
