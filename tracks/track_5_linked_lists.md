# Linked Lists — Invariants, Rewiring, and Structural Tricks

Track: `track_5_linked_lists`

Master pointer invariants, fast–slow techniques, in‑place rewiring, segment reversals, and list‑specific sorting.

See generation instructions in ../README.md.

## Problems

| Problem | Diff | Baseline | Complex Justified | Optimal | Repeats | Min Time | Conf | Clarified |             Communicated | Stated | Edge Tests | Clean Impl | Mistakes |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| [Reverse Linked List](../problems/0206-reverse-linked-list/readme.md) | Easy | ✖️ | ✖️ | ✖️ |  | 0 |                 1 | ✖️ | ✖️ | ✖️ | ✖️ | ✖️ |                      |
| [Middle of the Linked List](../problems/0876-middle-of-the-linked-list/readme.md) | Easy | ✖️ | ✖️ | ✖️ |  | 0 |                 1 | ✖️ | ✖️ | ✖️ | ✖️ | ✖️ |                      |
| [Linked List Cycle](../problems/0141-linked-list-cycle/readme.md) | Easy | ✖️ | ✖️ | ✖️ |  | 0 |                 1 | ✖️ | ✖️ | ✖️ | ✖️ | ✖️ |                      |
| [Intersection of Two Linked Lists](../problems/0160-intersection-of-two-linked-lists/readme.md) | Easy | ✖️ | ✖️ | ✖️ |  | 0 |                 1 | ✖️ | ✖️ | ✖️ | ✖️ | ✖️ |                      |
| [Merge Two Sorted Lists](../problems/0021-merge-two-sorted-lists/readme.md) | Easy | ✖️ | ✖️ | ✖️ |  | 0 |                 1 | ✖️ | ✖️ | ✖️ | ✖️ | ✖️ |                      |
| [Palindrome Linked List](../problems/0234-palindrome-linked-list/readme.md) | Easy | ✖️ | ✖️ | ✖️ |  | 0 |                 1 | ✖️ | ✖️ | ✖️ | ✖️ | ✖️ |                      |
| [Reverse Linked List II](../problems/0092-reverse-linked-list-ii/readme.md) | Medium | ✖️ | ✖️ | ✖️ |  | 0 |                 1 | ✖️ | ✖️ | ✖️ | ✖️ | ✖️ |                      |
| [Reorder List](../problems/0143-reorder-list/readme.md) | Medium | ✖️ | ✖️ | ✖️ |  | 0 |                 1 | ✖️ | ✖️ | ✖️ | ✖️ | ✖️ |                      |
| [Add Two Numbers](../problems/0002-add-two-numbers/readme.md) | Medium | ✖️ | ✖️ | ✖️ |  | 0 |                 1 | ✖️ | ✖️ | ✖️ | ✖️ | ✖️ |                      |
| [Sort List](../problems/0148-sort-list/readme.md) | Medium | ✖️ | ✖️ | ✖️ |  | 0 |                 1 | ✖️ | ✖️ | ✖️ | ✖️ | ✖️ |                      |
| [Reverse Nodes in k-Group](../problems/0025-reverse-nodes-in-k-group/readme.md) | Hard | ✖️ | ✖️ | ✖️ |  | 0 |                 1 | ✖️ | ✖️ | ✖️ | ✖️ | ✖️ |                      |
| [Copy List with Random Pointer](../problems/0138-copy-list-with-random-pointer/readme.md) | Medium | ✖️ | ✖️ | ✖️ |  | 0 |                 1 | ✖️ | ✖️ | ✖️ | ✖️ | ✖️ |                      |


## Extensions (Optional)

| Problem | Diff | Baseline | Complex Justified | Optimal | Repeats | Min Time | Conf | Clarified |             Communicated | Stated | Edge Tests | Clean Impl | Mistakes |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| [Swap Nodes in Pairs](../problems/0024-swap-nodes-in-pairs/readme.md) | Medium | ✖️ | ✖️ | ✖️ |  | 0 |                 1 | ✖️ | ✖️ | ✖️ | ✖️ | ✖️ |                      |
| [Remove Nth Node From End of List](../problems/0019-remove-nth-node-from-end-of-list/readme.md) | Medium | ✖️ | ✖️ | ✖️ |  | 0 |                 1 | ✖️ | ✖️ | ✖️ | ✖️ | ✖️ |                      |
| [Remove Linked List Elements](../problems/0203-remove-linked-list-elements/readme.md) | Easy | ✖️ | ✖️ | ✖️ |  | 0 |                 1 | ✖️ | ✖️ | ✖️ | ✖️ | ✖️ |                      |
| Odd Even Linked List | Medium |  |  |  |  |  |                  |  |  |  |  |  |                      |
| [Rotate List](../problems/0061-rotate-list/readme.md) | Medium | ✖️ | ✖️ | ✖️ |  | 0 |                 1 | ✖️ | ✖️ | ✖️ | ✖️ | ✖️ |                      |
| [Partition List](../problems/0086-partition-list/readme.md) | Medium | ✖️ | ✖️ | ✖️ |  | 0 |                 1 | ✖️ | ✖️ | ✖️ | ✖️ | ✖️ |                      |
| [Flatten a Multilevel Doubly Linked List](../problems/0430-flatten-a-multilevel-doubly-linked-list/readme.md) | Medium | ✖️ | ✖️ | ✖️ |  | 0 |                 1 | ✖️ | ✖️ | ✖️ | ✖️ | ✖️ |                      |
| Design Linked List | Medium |  |  |  |  |  |                  |  |  |  |  |  |                      |
| [LRU Cache](../problems/0146-lru-cache/readme.md) | Medium | ✖️ | ✖️ | ✖️ |  | 0 |                 1 | ✖️ | ✖️ | ✖️ | ✖️ | ✖️ |                      |
