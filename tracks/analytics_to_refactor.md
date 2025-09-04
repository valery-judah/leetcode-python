# Why this tracks?

Rationale: order by dependency, transfer, and interview yield. Each track adds one primitive, reuses prior ones, and reduces branching.

# **Principles**

- Prereqs first. Arrays → pointers → counts → recursion → graphs → DP.
- One dominant pattern per track. Minimize context switching.
- Coverage > repetition early. Repetition returns in the hard mix.
- Greedy heuristics appear only after their data-structure base exists.
- Streaming and “search-on-answer” appear after binary search and heaps.

# **Track logic**

- **track_0_foundations**: Arrays, hashing, simple stacks, prefix. Goals: O(n) scans, set/map invariants, monotonic stack intro. Output: correct one-pass solutions without re-scans.

- **track_1_sliding_window**: Windows before advanced two-pointers. Fixed vs dynamic windows, count maps, “expand then shrink,” deque for max. Output: you can derive window equations and code them from scratch.

- **track_2_two_pointers_advanced**: Sorting + in-place mutation. 3Sum/4Sum, Dutch flag, rotate, Floyd cycle. Output: pointer movement proofs and boundary control under mutation.

- **track_3_binary_search_heaps**: Monotone predicate, search on answer, and top-K/streaming. Output: write ok(mid) predicates cleanly and choose heap vs quickselect on constraints.

- **track_4_intervals**: Sort-by-start and greedy packing. Meeting rooms, arrows, covered intervals, intersections. Output: sweep mental model and resource counting.

- **track_5_linked_lists**: Structural invariants and sentinel patterns. LRU, random pointer copy. Output: pointer rewiring with O(1) extra space and clean proofs.

- **track_6_trees_basics**: DFS/BFS templates, subtree properties, BST ops, LCA. Output: postorder “return tuple” pattern and iterative BFS discipline.

- **track_7_graphs_basics**: Grids as graphs, topo sort, BFS/DFS levels, Dijkstra. Output: template selection by graph type and weight model.

- **track_8_dynamic_programming_i**: 1D DP and state compression. Kadane, LIS, coin change, word break. Output: write transitions and dimensions without hints.

- **track_9_dynamic_programming_ii**: 2D table DP and sequences. Edit distance family, LCS, path DPs, hard boundary cases. Output: stable table design and backtracking reconstruction.

- **track_10_hard_mix**: Integration under pressure. Monotonic stack geometry (84/85), trie + DFS (208/212), union-find (684/721), Fenwick/segment tree (307), plus spaced-repetition of earlier cores (42, 239). Output: pick the right tool in ≤1 minute.

# **Why these IDs**

- Standard LeetCode IDs with high signal in interviews.
- Premium items included only where the pattern is uniquely valuable.
- A few intentional repeats in the hard mix for spaced repetition and transfer under harder contexts.

# **Exit checks per track**

- Foundations: solve 10 easy/mediums at ≤20 min each with ≤1 WA.
- Sliding window: derive window invariant before coding on all four types: set, counts, fixed-K, deque.
- Two-pointers adv: handle off-by-one and duplicates in 3Sum/4Sum without debug prints.
- Binary search/heaps: write binary_search_on_answer skeleton from memory and justify heap vs quickselect.
- Intervals: produce O(n log n) greedy proof sketches.
- Linked lists: no extra arrays or recursion for core ops.
- Trees/Graphs: choose correct traversal and memoization pattern without hints.
- DP I/II: specify state, transition, base, and order in one minute on paper.

This sequencing cuts cognitive load, maximizes reuse of templates, and matches common interviewer flow.
