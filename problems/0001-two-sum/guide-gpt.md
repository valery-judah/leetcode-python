# LC-0001 · Two Sum — A Narrative Guide to Mastery

_Suggested filename: `LC-0001-guide.md`_

---

## 1) The Discovery Path: From Brute-Force to Optimal

### Reading the brief like an engineer

We’re given an array `nums` and an integer `target`. We must **return the indices** of **two distinct
elements** whose values sum to `target`. Order of indices doesn’t matter; any valid pair is acceptable. The
input is **unsorted**, and there may be **duplicates**.

Typical LeetCode constraints make `n` large enough that quadratic solutions time out on worst cases. That’s
the signal: if your first thought is “nested loops,” your second thought should be “how can we _index_ the
search?”

---

### Naive baseline (brute force)

**Idea.** Check every pair `(i, j)` with `i < j`. If `nums[i] + nums[j] == target`, return `[i, j]`.

**Pseudo:**

```
for i in [0..n-1]:
  for j in [i+1..n-1]:
    if nums[i] + nums[j] == target: return [i, j]
```

**Complexity.**

- Time: `O(n^2)` comparisons.
- Space: `O(1)` extra.

**Why it’s suboptimal.** With `n = 10^5`, `~5e9` checks in worst case is infeasible. The problem is
**search**: for each `nums[i]` we’re **searching linearly** for its complement.

---

### Bottleneck analysis → what exactly hurts?

For every element `a = nums[i]`, we need to answer the question:

> “Have we seen an element equal to `target - a`?”

The brute force method answers this by **scanning** the rest of the array each time. That’s redundant work. If
we could answer this membership query in ~`O(1)` time, we would immediately remove a factor of `n`.

---

### The “aha!” moment: turn search into lookup

Two equivalent algebraic views:

- Equation view: find `a, b` with `a + b = target` → equivalently `b = target - a` (the **complement**).
- Data view: maintain a **fast index** from values we’ve already seen to their indices. Then, for each new
  `a`, we just look up `target - a`.

This is the classic **hashing for complement queries** pattern (a one-pass hash map). It’s a **time–space
tradeoff**: you spend `O(n)` space to reduce time to `O(n)`.

---

### Building the optimal algorithm (thoughtfully)

**Invariant to maintain while scanning left→right at index `i`:**

> The hash map `seen` contains every value in `nums[0..i-1]` mapped to _an_ index where it occurred.

Now at position `i` with value `a = nums[i]`:

1. Compute `need = target - a`.
1. **Check before insert:** If `need in seen`, we’ve found indices `[seen[need], i]`. Return.
1. Otherwise, insert `seen[a] = i` and move on.

Why “check before insert”?

- Consider `target = 2x` and `a = x`. If you insert first, then look up, you might accidentally match the same
  index you just inserted. Checking first ensures the pair uses **two distinct indices**.
- It also naturally handles duplicates like `[3,3]` with `target=6`: at the second `3`, the first `3` is
  already in `seen`.

**Correctness sketch.**

- If there exists a solution `(p, q)` with `p < q`, when we reach `i = q`, we’ve already inserted `nums[p]`
  into `seen`. So we will find it and return.
- If no pair exists, we never return early—after one pass, the algorithm legitimately concludes there’s no
  solution (LeetCode always ensures existence; in general code you might return `None`/raise).

**Complexity.**

- Time: `O(n)` expected (amortized `O(1)` hash lookups).
- Space: `O(n)` for the map.

**Pythonic reference solution**

```python
def two_sum(nums: list[int], target: int) -> list[int]:
    seen: dict[int, int] = {}
    for i, a in enumerate(nums):
        need = target - a
        if need in seen:                 # check-before-insert to avoid self-pair bug
            return [seen[need], i]
        seen[a] = i
    raise ValueError("No two numbers sum to target")  # or return []
```

---

## 2) Systematic Test Case Construction: An Adversarial Approach

### Mindset: try to break it

Avoid **example-construction bias** (only crafting cases that confirm your idea). Instead, partition the input
space into **equivalence classes** and attack assumptions: duplicates, negatives, zero, extremes, multiple
answers, and degenerate sizes.

Below are **classes** with a representative case and what each reveals.

#### A. “Happy path” (typical unsorted, straightforward)

- **Case:** `nums=[2,7,11,15], target=9` → expect indices `[0,1]`.
- **Why:** Confirms basic complement logic.

#### B. “Zero-element” (no data)

- **Case:** `nums=[], target=5`
- **Expect:** Exception or sentinel (e.g., `None`/`[]`).
- **Why:** Ensures your code doesn’t index empty structures or assume a solution exists.

#### C. “Singleton” (insufficient elements)

- **Case:** `nums=[5], target=10`
- **Expect:** Exception/sentinel.
- **Why:** Forces you to consider minimum length logic.

#### D. “Boundary length” (minimum valid size)

- **Case:** `nums=[1,2], target=3` → `[0,1]`.
- **Why:** Off-by-one guardrail; ensures loop logic works at edges.

#### E. “Duplicate values” (same number can be used twice)

- **Case:** `nums=[3,3], target=6` → must return two distinct indices `[0,1]`.
- **Why:** Detects the **self-pair bug** (inserting before checking).

#### F. “Multiple valid pairs” (non-determinism acceptable)

- **Case:** `nums=[1,3,3,2], target=4` → `[0,1]` or `[0,2]` or `[3,?]` depending on order.
- **Why:** Confirms you return **any** valid pair and don’t over-constrain output.

#### G. “Negative numbers and zero”

- **Case:** `nums=[0,-3,1,2,-1], target=-1` → `[-3, 2]` → indices `[1,3]`.
- **Why:** Ensures arithmetic/complements handle negatives and zero.

#### H. “Large magnitude values”

- **Case:** `nums=[10**9, -10**9, 4, 6], target=10` → `[2,3]`.
- **Why:** In non-Python languages, catches potential overflow concerns; in Python, confirms generality.

#### I. “No solution”

- **Case:** `nums=[1,2,5], target=100`
- **Expect:** Exception/sentinel.
- **Why:** Ensures graceful failure and no infinite loops.

#### J. “Late match” (forces full traversal)

- **Case:** `nums=[5,4,3,2,1], target=6` → `[1,3]` or `[0,4]`.
- **Why:** Confirms the structure handles late discoveries and preserves earlier indices correctly.

> **Tip:** Automate these as table-driven tests. For LeetCode’s guarantees you won’t hit “no solution,” but
> robust library code should still handle it.

---

## 3) Common Pitfalls and Error Analysis

### The core pitfall: **Self-pair due to insert-before-check**

**Symptom.** For `nums=[3]` and `target=6` (or in the presence of one `3` when expecting a pair), code that
inserts first then checks may “find” the same index twice or pass degenerate cases.

**Root cause.** You insert `a=3` into `seen` and then immediately look for `need=3`; the map returns the same
index you just inserted.

**Prevention.**

- **Check-before-insert**: look up `need` first; only insert `a` if no match found.
- Add the duplicate test `([3,3], 6)` to your suite.

---

### Other frequent mistakes

1. **Returning values instead of indices.**\
   The problem explicitly asks for indices. Prevention: name your map `value_to_index`, and return
   `[value_to_index[need], i]`.

1. **Overwriting earlier index for duplicates (when you care about stability).**\
   In LeetCode Two Sum, any valid pair works; but in some specs you might need **earliest** indices.
   Prevention: only set `seen[a] = i` if `a` not already in `seen`.

1. **Applying two-pointers on unsorted input.**\
   Two-pointers requires **sorted** arrays (that’s Two Sum II). Sorting first would change indices unless you
   keep original positions. Prevention: prefer the hash-map approach here; reserve two-pointers for the sorted
   variant.

1. **Assuming a solution exists in generic code.**\
   LeetCode’s prompt guarantees one, but library code should handle none-found cleanly (return sentinel or
   raise).

---

## 4) Reflection and Deeper Connections

### Distilling the core pattern

- **Name:** One-Pass Hash for Complement (a.k.a. Hashing for Sum-Complement Queries)
- **Essence:** Replace an inner linear search with an `O(1)` **associative lookup** by storing just enough
  prior state (here: value → index).
- **Lens:** A classic **time–space tradeoff** and a special case of “preprocessing & indexing.”

### Where this pattern appears again

- **Two Sum II (Sorted)**: Uses **Two Pointers** instead of a hash map (because sorting enables monotonic
  movement).
- **3Sum / 4Sum**: Fix one (or two) numbers, reduce to repeated Two Sum on the remainder (hash or two-pointers
  depending on sorting).
- **Subarray Sum Equals K**: Use **prefix sums** and a hash map of prefix frequencies to find complements
  (`prefix[j] - prefix[i] = K`).
- **Two Sum Less Than K / Closest**: Variants mixing hash and ordering, often switching to two-pointers after
  sorting depending on the objective.

### Trade-off analysis (engineering perspective)

- **Hash-map (this solution):**
    - **Pros:** Linear time, simple, single pass, no sorting, preserves original indices.
    - **Cons:** `O(n)` extra memory; hash-table overhead; non-deterministic pair selection with duplicates
      (acceptable here).
- **Sort + Two Pointers:**
    - **Pros:** `O(n log n)` time, `O(1)` extra space (in-place sort), useful for related objectives (closest
      sum, count pairs).
    - **Cons:** Destroys original order; you must track original indices or copy pairs, adding complexity.
- **Brute-force:**
    - **Pros:** Minimal code, `O(1)` space; sometimes fine for tiny `n`.
    - **Cons:** Catastrophic for large `n`.

**Guiding heuristic:**

- If the array is **unsorted** and you need **indices**, default to **one-pass hash map**.
- If the array is **sorted** or you’re free to sort and don’t need original indices, consider **two-pointers**
  for space savings or for range-style objectives.

---

## Appendix: Minimal but rigorous Python (with stability option)

```python
def two_sum(nums: list[int], target: int) -> list[int]:
    """Return indices of two numbers adding to target (any valid pair)."""
    seen: dict[int, int] = {}
    for i, a in enumerate(nums):
        need = target - a
        if need in seen:
            return [seen[need], i]
        # keep earliest index for stability-sensitive variants:
        if a not in seen:
            seen[a] = i
    raise ValueError("No two numbers sum to target")
```

**Loop invariant.** Before processing `i`, `seen` contains some (or all) values from `nums[0..i-1]` each
mapped to an index `< i`.\
**Progress.** Each iteration either returns a valid pair or adds one mapping, moving `i` forward.\
**Termination.** If no pair exists, the loop ends with no return, and we raise.

---

### Closing thought

Two Sum is more than a warm-up; it’s a **proto-pattern**. The real upgrade is not learning “the answer,” but
training your reflex: _whenever you catch yourself scanning for matches inside a loop, ask: can I precompute
or index the needed information to turn search into lookup?_ That question alone collapses many `O(n^2)`
problems into `O(n)`.
