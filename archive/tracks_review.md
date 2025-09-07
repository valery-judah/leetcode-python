# How to Use These Tracks Effectively (Interview‑Focused)

This review explains **how** to run the tracks, **what to practice**, and **how to judge readiness**. It is systemized for short, repeatable sessions and interview realism.

______________________________________________________________________

## 0) What’s in this repo

- `tracks/track_*.yaml`: ordered learning tracks with **why** for each problem, extensions, and omissions.
- `tracks/tracks.json`: compact list of `{name, ids}` for generators.
- `problems/<slug>/`: per‑problem folder with README, solution(s), tests, `meta.yaml` (see schema in the project root plan).

> Principle: **one primary pattern** per problem. Solve using that pattern first. Alternate solutions are fine later, not up front.

______________________________________________________________________

## 1) Daily loop (45–60 min per medium)

### A. Pick

1. Choose an active track (start at `track_0_foundations`, move in order).
1. Pull the next 1–3 unsolved items from the `problems` list in that track.

### B. Frame (≤5 min)

- Read the prompt, restate **inputs, outputs, constraints**.
- Decide the **pattern** first. If unclear, use the **cue→pattern table** below.
- State **complexity target** out loud (time, space) before coding.

### C. Plan (≤5 min)

- Write the invariant or predicate (e.g., *“window has no dups”*, *“ok(mid) is feasible”*, *“stack keeps increasing heights”*).
- Name key variables and data structures.

### D. Code (15–25 min)

- Code the **template** for the pattern, then adapt to the problem.
- Keep functions small. Separate helpers where it clarifies invariants.

### E. Test (10–15 min)

- Construct 5–8 cases that each kill a class of bugs (see **Edge‑case bank**).
- Run. If a test fails, **instrument** minimal prints or assert the invariant.

### F. Record (≤5 min)

- Update `problems/<slug>/meta.yaml`: status, attempts, last_solved, next `revisit_on`.
- Write 2–4 bullets in README: invariant, pitfalls, final complexities.

______________________________________________________________________

## 2) Track progression and readiness gates

Advance only when you meet the gate for the current track.

- **Track 0 Foundations**: 12+ problems at ≤20 min easy / ≤30 min medium. One‑pass hashmap, set logic, simple stack, prefix‑sum complement are automatic.
- **Track 1 Sliding Window**: You can derive the shrink condition for **set**, **counts**, **fixed‑size**, **deque** windows without hints. Solve 121, 3, 424, 76, 239 from memory.
- **Track 2 Two‑Pointers Advanced**: Clean duplicate handling in 3Sum/4Sum. Dutch Flag in ≤10 min. Can prove Trapping Rain Water two‑pointer correctness.
- **Track 3 Binary Search & Heaps**: You can write `binary_search_on_answer(ok)` skeleton blind. Justify heap vs quickselect vs bucket.
- **Track 4 Intervals**: Give a 2‑minute greedy proof for “pick by earliest end.” Implement merge/insert/intersect correctly first try.
- **Track 5 Linked Lists**: No extra arrays for core rewiring. Use dummy heads. Reverse sublist and k‑group without pointer leaks.
- **Track 6 Trees**: Postorder return‑tuple habit. LCA (BST and general). BFS levels with size snapshots.
- **Track 7 Graphs**: Grid BFS/DFS templates. Kahn’s topo with indegrees. Dijkstra with visited and decrease‑key by push‑again.
- **Track 8 DP I**: State, subproblem, transition, base (**SSTB**) in one minute on paper for LIS, Coin Change, Word Break.
- **Track 9 DP II**: Build 2D tables left‑to‑right/top‑down correctly. LCS, Edit Distance, Palindromes are smooth.
- **Track 10 Hard Mix**: Monotonic stack 84/85, Trie+DFS 212, DSU 947, BIT/SegTree 307 under time pressure.

______________________________________________________________________

## 3) Cue → Pattern decision table

Use these to pick a starting template fast.

- **“Longest/shortest subarray/substring with condition”** → Sliding Window.
  - Unique elements → window + set.
  - At most K distinct / budget K → counts + shrink on violation.
  - Fixed length K → roll counts in O(1) per step.
  - Max per window → monotonic deque.
- **Sorted array + sum/area** → Two Pointers. If k‑sum, sort + move l/r with dedup.
- **“Minimize max” or “can we do with X?”** → Binary Search on Answer with `ok(mid)`.
- **“Top K” / “K closest” / stream** → Heap (size‑K or two‑heap for median).
- **Intervals**:
  - Merge/insert → sort by start, merge into accumulator.
  - Non‑overlap/rooms/arrows → greedy by earliest end; rooms = min‑heap or sweep.
- **Linked list rewiring** → Dummy head + pointer choreography; avoid arrays.
- **Trees**:
  - Combine children → postorder return tuple.
  - BST ops → inorder or bound checks.
  - LCA → order property (BST) or postorder combine.
- **Graphs**:
  - Grid regions → DFS/BFS with visited.
  - Prereqs → Kahn topo.
  - Positive weights → Dijkstra.
  - Components/cycles in undirected → DSU.
- **DP**:
  - Subarray max → Kadane.
  - Sequence (LIS/LCS) → 1D tails or 2D table by match/skip.
  - Coin/Subset → 1D knapsack with careful iteration order.

______________________________________________________________________

## 4) Pattern templates to say out loud (no code)

- **Window (counts)**: expand `r`, update counts; while invalid, shrink `l`; update best; continue.
- **Two Pointers (k‑sum)**: sort; for each `i`, skip dups; set `l=i+1,r=n-1`; move by sign; collect; dedup.
- **Binary Search on Answer**: set bounds; while `lo<hi`: `mid`; if `ok(mid)` then `hi=mid` else `lo=mid+1`.
- **Monotonic Deque**: pop back while worse; push new index; pop front if out of window; read front as answer.
- **Postorder Return Tuple**: get left/right tuples; compute local; update global; return tuple to parent.
- **DSU**: `find` with path compression, `union` by rank/size; count components.
- **Knapsack (min coins)**: init `dp[0]=0`, rest INF; for each coin, for amount from coin..N: `dp[a]=min(dp[a],dp[a-coin]+1)`.

______________________________________________________________________

## 5) Testing checklist (per problem)

- Zero/empty inputs; singletons.
- Duplicates, ties, equal elements.
- Max constraints (stress); min constraints.
- Negatives vs positives when relevant.
- Boundaries: first/last window, off‑by‑one around edges.
- Randomized spot checks for commutativity/associativity assumptions.

______________________________________________________________________

## 6) Spaced repetition and promotion rules

- After **first AC**: schedule `revisit_on = +7d`.
- After **second AC**: `+21d`.
- After **any miss** or >20 min struggle: `+3d` and mark `pitfalls` in README.
- Promotion: move to next track only when **gates** are met and last week’s accuracy ≥80% on current track items.

______________________________________________________________________

## 7) Time management for interviews (60 min block)

1. 3–5 min: clarify prompt, examples. Choose pattern. Complexity target.
1. 15–20 min: code clean first pass.
1. 10 min: test edge cases; fix.
1. 5 min: analyze complexity, prove invariant quickly.
1. 5 min: discuss alternatives and tradeoffs.
1. Buffer 10–15 min for curveballs.

> If stuck at 10 min: state backup approach (e.g., O(n log n) sort + heap), then iterate toward optimal.

______________________________________________________________________

## 8) Communication rubric (what to say)

- Problem restatement in your words.
- Pattern selection and **why**.
- Invariant/predicate statement.
- Complexity goal.
- Walkthrough on a small example.
- Edge cases you will test.
- Alternatives if time allows.

______________________________________________________________________

## 9) Common pitfalls per pattern

- **Window**: wrong shrink condition; forgetting to update best after shrink; not removing zero‑count keys.
- **Two Pointers**: missing dedup; moving the wrong side; integer overflows in k‑sum.
- **Binary Search**: infinite loop from mid/lo/hi mistakes; wrong predicate monotonicity; bad initial bounds.
- **Intervals**: mixing overlap vs containment; sorting by wrong key (start vs end).
- **Stacks**: not popping all pending at the end; wrong comparison direction in monotonic stacks.
- **Linked Lists**: forgetting dummy head; losing next pointer before rewiring.
- **Trees**: mixing global best with returned value; forgetting base cases.
- **Graphs**: revisiting nodes; building O(n²) adjacency when a map is enough.
- **DP**: wrong iteration order (0/1 vs unbounded); bad base initialization; double counting.

______________________________________________________________________

## 10) Using the track files

- Start from `tracks/track_0_foundations.yaml` and proceed sequentially.
- In each `track_*.yaml`, use the ordered `problems:` and optional `extensions:` as a queue.
- If you keep a generator, consume from `tracks.json` for `{name, ids}`.
- For each problem, scaffold `problems/<slug>/` and write `meta.yaml` with fields:
  - `status` (`todo|in_progress|solved|revisit`), `attempts`, `last_solved`, `revisit_on`.
  - `primary_pattern`, `time_complexity`, `space_complexity`.
  - `pitfalls` bullets.

______________________________________________________________________

## 11) Edge‑case bank (fast recall)

- Empty input; length 1; all equal; strictly increasing/decreasing; all zeros; alternating patterns.
- For strings: all same char; all distinct; mix of cases; Unicode/specials if relevant to codec problems.
- For sums/products: negatives, zeros, large magnitudes; overflow guards.
- For graphs: single node, disconnected components; cycles vs trees.

______________________________________________________________________

## 12) When unknown pattern appears

- Reduce to known core: can it be **window**, **two‑pointers**, **prefix/heap**, **interval**, **DSU**, **postorder tuple**, or **DP**?
- If not, propose a safe O(n log n) baseline (sort + structure). State it and implement.
- Re‑evaluate for optimizations only after baseline passes tests.

______________________________________________________________________

## 13) Final week before interview

- Day 7–5: Track 0–3 speed runs. Aim ≤10 min per easy, ≤20 per medium.
- Day 4–3: Track 4–6 mixed set.
- Day 2: Track 7–9 mixed set; 1–2 hards from Track 10.
- Day 1: Two full mocks. One design (LRU/LFU/Trie), one algorithms mixed.

______________________________________________________________________

## 14) Quality bar for submission

- Single pass where intended, no unnecessary structures.
- Names reflect roles (`left`, `right`, `need`, `have`, `ok`), not noise.
- Clear invariant comments at top and near tricky loops.
- Tests include at least 5 “bank” cases.
- Final note on **time/space** and **why this pattern**.

______________________________________________________________________

## 15) Short template crib (one‑liners)

- **SSTB for DP**: *State, Subproblem, Transition, Base*.
- **BS on answer**: `lo, hi = min, max; while lo < hi: mid; if ok(mid): hi=mid else lo=mid+1`.
- **Deque max**: drop back while worse; drop front if out; front is max.
- **DSU**: path compression in `find`, union by size.
- **Postorder**: compute from children; update global; return to parent.

Stay mechanical. Pick a pattern, state its invariant, implement its template, test edges, record learnings, repeat.
