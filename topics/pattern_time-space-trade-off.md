# Anticipatory Indexing: A Time–Space Tradeoff Pattern

## Abstract

Replace repeated scans with a maintained auxiliary structure that answers future queries fast. Spend memory and bounded update work now to cut later time. This pattern defines a formal model, design rules, variants, correctness obligations, and LeetCode-style examples.

______________________________________________________________________

## 1. Name

**Anticipatory Indexing** (aka **Preprocess-and-Index**). Trade time for space by materializing a summary or index while streaming or preprocessing the input.

______________________________________________________________________

## 2. Intent

Cut worst-case or amortized time by avoiding $O(n)$ rescans. Build a structure $S$ so that each query or decision is $O(1)$ or $O(\\log n)$ on average.

______________________________________________________________________

## 3. Model

- **Input sequence**: $x_1,\\dots,x_n$.
- At step $i$, you may:
  - **Query**: answer a predicate/aggregation about past items using only $S\_{i-1}$.
  - **Update**: set $S_i \\leftarrow U(S\_{i-1}, x_i)$.
- **Cost**:

$$
T\_{\\text{scan}} = \\Theta(n^2) \\quad \\text{vs} \\quad T\_{\\text{idx}} = \\sum\_{i=1}^{n} (c_Q(i) + c_U(i)).
$$

If $c_Q, c_U \\in O(1)$ on average, then $T\_{\\text{idx}} = O(n)$.

**Invariant:** $S_i$ reflects all information needed from ${x_1,\\dots,x_i}$ for future queries.

______________________________________________________________________

## 4. When to Use / When Not

**Use when:**

- Repeated membership, complement, predecessor, nearest-neighbor, or range queries.
- Streaming or online decisions.
- You can afford $O(n)$ extra space (or an approximate summary).

**Avoid when:**

- Single query with tiny $n$.
- Severe memory constraints and no acceptable approximation.
- Highly write-heavy workloads where maintenance dominates.

______________________________________________________________________

## 5. Structure

- **State $S$**: dictionary, set, tree, heap, prefix array, sketch, or Bloom filter.
- **Update $U$**: constant or logarithmic time per element.
- **Answer $A(q,S)$**: constant or logarithmic time per query.
- **Maintenance**: rehashing, rotations, rebuilds, or periodic compaction.

______________________________________________________________________

## 6. Correctness Obligations

- **Soundness**: answers from $S$ equal answers from rescanning raw data (or are within stated error bounds for probabilistic summaries).
- **Completeness**: $S$ keeps all info needed by future queries; no missing states.
- **Stability**: invariant holds after each update.
- **Randomized structures**: bound failure rates (e.g., Bloom filter FPR).

______________________________________________________________________

## 7. Complexity Tradeoffs

| Structure | Build/Update | Query | Space | Notes |
|---|---:|---:|---:|---|
| Hash set / dict | $O(1)$ avg | $O(1)$ avg | $O(n)$ | Adversarial inputs degrade to $O(n)$ per op |
| Balanced BST | $O(\\log n)$ | $O(\\log n)$ | $O(n)$ | Order queries supported |
| Prefix sums | $O(n)$ build; $O(1)$ query | $O(1)$ | $O(n)$ | Immutable array; use Fenwick/segment tree for updates |
| Fenwick / Segment tree | $O(\\log n)$ | $O(\\log n)$ | $O(n)$ | Range queries with updates |
| Bloom filter | $O(1)$ | $O(1)$ (prob.) | $O(m)$ bits | False positives only |
| LRU cache | $O(1)$ | $O(1)$ | $O(C)$ | Competitive under locality |

______________________________________________________________________

## 8. Design Recipe

1. **Bottleneck**: isolate the inner scan $P(x_i,\\cdot)$.
1. **Workload hypothesis**: expected queries, error tolerance, update rate, memory budget.
1. **Sufficient summary $S$**: minimal state to answer future queries.
1. **Update/Query contracts**: define $U$ and $A$; preserve invariant.
1. **Amortized bound**: rehashes/rebuilds must not dominate.
1. **Failure modes**: adversarial keys, skew, staleness, approximation error.

______________________________________________________________________

## 9. Patterns and LeetCode Examples

### 9.1 Contains Duplicate

- **Query**: seen before?
- **State**: `set`

```python
from typing import List

def contains_duplicate(nums: List[int]) -> bool:
    seen = set()
    for x in nums:
        if x in seen:
            return True
        seen.add(x)
    return False
```

Time $O(n)$ avg, space $O(n)$.

### 9.2 Two Sum

- **Query**: is `target - x` already present?
- **State**: `dict` value → index

```python
from typing import List

def two_sum(nums: List[int], target: int) -> List[int]:
    pos = {}
    for i, x in enumerate(nums):
        y = target - x
        if y in pos:
            return [pos[y], i]
        pos[x] = i
    return [-1, -1]
```

### 9.3 Range Sum Query (immutable)

- **Query**: sum on `[l, r]`.
- **State**: prefix sums.

```python
class NumArray:
    def __init__(self, nums):
        ps = [0]
        for v in nums:
            ps.append(ps[-1] + v)
        self.ps = ps
    def sumRange(self, l: int, r: int) -> int:
        return self.ps[r + 1] - self.ps[l]
```

### 9.4 Top-K Frequent Elements

- **Query**: top-k by count.
- **State**: frequency `dict` + heap/bucket index.
- **Trade**: space for $O(n)$ bucket buildup and $O(n)$ time.

### 9.5 Duplicate Detection at Scale (approximate)

- **Query**: membership with small RAM.
- **State**: Bloom filter.
- **Benefit**: dramatically less memory. **Cost**: false positives.

______________________________________________________________________

## 10. Proof Sketches

### 10.1 Soundness for Contains Duplicate

Induction on stream index $i$. Base $i=1$: `seen` contains exactly ${x_1}$. Step: at $i$, `x in seen` iff there exists $j < i$ with $x_j = x$. After check, add $x_i$. Invariant holds.

### 10.2 Amortized $O(1)$ Hashing

With geometric resizing (bounded load factor), total moves across $n$ inserts is $O(n)$. Hence average per insert is $O(1)$. Membership has the same bound.

______________________________________________________________________

## 11. Failure Modes and Mitigations

- **Adversarial hashing** → robust hash, random seeding, or tree fallback (e.g., hashmap-to-tree under heavy collision).
- **Skewed distributions** → balanced trees or two-level hashing.
- **Staleness** in dynamic datasets → versioning or rebuild triggers.
- **Approximation errors** → size the sketch for target error; validate hits if needed.
- **Memory blow-up** → compress keys, store indices not values, purge via LRU/TTL.

______________________________________________________________________

## 12. Variants

- **Data-structure augmentation**: keep extra fields to answer queries (e.g., subtree sizes for order statistics).
- **Predecessor/nearest-neighbor**: balanced BST, skip list, k-d tree.
- **Sketching/streaming**: Count–Min, HyperLogLog, reservoir sampling.
- **External-memory**: B-trees for I/O-efficient indexing.
- **Succinct**: near-entropy space with $O(1)$ rank/select.

______________________________________________________________________

## 13. Implementation Checklist

- Define target query $Q$ precisely.
- Choose $S$ that answers $Q$ without touching raw array.
- Specify $U$ and invariant.
- Bound $c_U, c_Q$; justify amortized costs.
- Handle collisions, edge cases, and duplicates.
- Add tests covering: empty, single element, all equal, strictly increasing, random, adversarial.

______________________________________________________________________

## 14. Reference Template (drop-in)

```python
from typing import Iterable, Any

class AnticipatoryIndex:
    def __init__(self, init_state: Any):
        self.S = init_state

    def query(self, x):
        # implement A(S, x)
        raise NotImplementedError

    def update(self, x) -> None:
        # implement U(S, x); maintain invariant
        raise NotImplementedError

def process(stream: Iterable, idx: AnticipatoryIndex):
    for x in stream:
        yield idx.query(x)
        idx.update(x)
```

______________________________________________________________________

## 15. Worked Example: Contains Nearby Duplicate (k-window)

- **Query**: has same value within last $k$ indices?
- **State**: sliding window `set`.

```python
from typing import List

def contains_nearby_duplicate(nums: List[int], k: int) -> bool:
    seen = set()
    for i, x in enumerate(nums):
        if x in seen:
            return True
        seen.add(x)
        if i >= k:
            seen.remove(nums[i - k])
    return False
```

Invariant: `seen` equals the contents of the last $\\le k$ items.

______________________________________________________________________

## 16. Connections to Theory

- **Static data-structure model**: preprocess time $T_p$ vs query time $T_q$.
- **Cell-probe model**: space–time lower bounds for dictionaries and predecessor.
- **Amortized analysis**: potential method for dynamic arrays and hashing.
- **Probabilistic data structures**: explicit error–time–space tradeoff.

______________________________________________________________________

## 17. Summary

Anticipatory Indexing replaces right-side scans with a maintained summary $S$. Define the future workload, pick a sufficient summary, enforce the invariant, and prove amortized bounds. This is the standard lever to turn $O(n^2)$ patterns into $O(n)$ solutions in interview problems and beyond.

______________________________________________________________________

## 18. Further Practice (LeetCode set)

- 217 **Contains Duplicate** → set.
- 1 **Two Sum** → dict.
- 219 **Contains Nearby Duplicate** → sliding window + set.
- 238 **Product of Array Except Self** → prefix/suffix passes.
- 560 **Subarray Sum Equals K** → prefix sums + dict.
- 703 **Kth Largest Element in a Stream** → heap index.
- 355 **Design Twitter** → hash + heap + time index.

**For each solution include:** chosen $S, U, A$, invariant, complexity, and edge cases.
