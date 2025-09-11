# 0011 — Container With Most Water

A rigorous, practical guide in the same workflow you used for “Valid Anagram”: clarify → discover → prove → implement → test → audit.

______________________________________________________________________

## 1) Problem model

- Input: heights `h[0..n-1]`, `n ≥ 2`, `h[i] ≥ 0`.
- Container at indices `i < j` holds area `A(i, j) = (j - i) * min(h[i], h[j])`.
- Goal: return `max_{0≤i<j<n} A(i, j)`.

**Targets:** `O(n)` time, `O(1)` extra space.

______________________________________________________________________

## 2) Clarifications and assumptions

- Heights are integers in Python. In fixed-width languages, use 64-bit to avoid overflow of `(j - i) * min(...)`.
- Duplicates and zeros are allowed.
- Return the area only. Indices are not required.

______________________________________________________________________

## 3) Baseline oracle (keeps us honest)

A direct `O(n^2)` scan. Useful as an oracle for small `n` in property tests.

```py
from typing import List

def maxArea_bruteforce(height: List[int]) -> int:
    best = 0
    n = len(height)
    for i in range(n):
        hi = height[i]
        for j in range(i + 1, n):
            hj = height[j]
            area = (j - i) * (hi if hi < hj else hj)
            if area > best:
                best = area
    return best
```

______________________________________________________________________

## 4) Discovery Path — understandable greedy reasoning

**Plain-language goal:** keep the width large and the limiting height large.

1. **Start from the widest pair.** Put pointers at the ends `(l, r) = (0, n-1)`. This maximizes width.

1. **What can make area bigger next?** Any move reduces width by 1. So the *only* way to offset the width loss is to increase the *limiting* height `min(h[l], h[r])`.

> [!note]
> this one is interesting: we need to ask ourselves what to do on each step? 'What to do?' \<- What our goal and what our dV on this specific step? Maximising area.

3. **Which pointer should move?**

   - If `h[l] < h[r]`, the left line is the limiter. Moving `r` left shrinks width and keeps the limiter ≤ `h[l]` (or worse). That cannot help. The only move with upside is to drop the short left wall and search for a taller one → move `l += 1`.
   - If `h[r] < h[l]`, symmetric: move `r -= 1`.
   - If equal, either side can move. Move one.

1. **Micro thought experiment (why moving the taller side fails).**

   - Suppose `h[l] = 2`, `h[r] = 7`. If you move the right pointer inward, width shrinks, and the new min is still ≤ 2. Best-case area after that move is `(new_width) * 2`, which is strictly smaller than the current `(old_width) * 2`. No gain is possible.

1. **Tiny walkthrough on the canonical example** `[1,8,6,2,5,4,8,3,7]`:

   - Start `(l,r)=(0,8)`: area `8*1=8`. Left is shorter → move `l`.
   - `(1,8)`: area `7*7=49`. Right is shorter (7\<8)? No, left is 8 and right 7 → move `r`.
   - `(1,7)`: area `6*3=18`. Right is shorter → move `r`.
   - Continue this rule; the best seen is `49`, which is the answer. The rule prevents pointless moves.

**Greedy rule (one sentence):** always advance the pointer at the shorter line.

**Why it’s safe:** if you keep the shorter side and move the taller one, the minimum height can’t rise, and the width shrinks, so the area cannot improve.

______________________________________________________________________

## 5) Correctness

### A. Dominance / exchange argument (informal)

With `h[l] ≤ h[r]`, every pair that keeps `l` and moves `r` inward has area ≤ `(r-l) * h[l]` with a smaller width, so it cannot beat the current pair. Any improvement that still uses `l` would need a `r' > r` with `h[r'] > h[l]`, which does not exist. Therefore dropping `l` is safe. Symmetric for the other side.

### B. Loop invariant (precise)

**Invariant:** at loop entry, there exists an optimal pair entirely within `[l, r]`.

- **Init:** holds for `[0, n-1]`.
- **Maintain:** if `h[l] ≤ h[r]`, some optimum does not use `l` (by dominance), so advancing `l` preserves the invariant. Symmetric otherwise.
- **Terminate:** when `l ≥ r`, the recorded `best` equals the global optimum.

______________________________________________________________________

## 6) Complexity

- Time `O(n)` (each pointer moves at most `n-1` times).
- Space `O(1)`.

______________________________________________________________________

## 7) Reference implementation (Python)

```py
from typing import List

def maxArea(height: List[int]) -> int:
    l, r = 0, len(height) - 1
    best = 0
    while l < r:
        left, right = height[l], height[r]
        # compute before moving
        if left <= right:
            area = (r - l) * left
            if area > best:
                best = area
            l += 1
        else:
            area = (r - l) * right
            if area > best:
                best = area
            r -= 1
    return best
```

______________________________________________________________________

## 8) Tests (pytest style)

Curated cases + randomized vs oracle + scale sanity.

Create `tests/test_container.py` and import the functions from your module.

### A. Deterministic unit tests

```py
from container import maxArea

def test_min_size_and_zeros():
    assert maxArea([0, 0]) == 0
    assert maxArea([0, 5]) == 0
    assert maxArea([5, 0]) == 0
    assert maxArea([1, 1]) == 1

def test_canonical():
    assert maxArea([1,8,6,2,5,4,8,3,7]) == 49
    assert maxArea([1,2,1]) == 2
    assert maxArea([4,3,2,1,4]) == 16
    assert maxArea([1,3,2,5,25,24,5]) == 24

def test_plateaus_and_duplicates():
    assert maxArea([3,3,3,3]) == 9      # width 3 * height 3 between ends
    assert maxArea([0,3,0,3,0]) == 9

def test_monotone_sequences():
    assert maxArea([1,2,3,4,5]) == 6    # e.g., (1,4): width 3 * min 2
    assert maxArea([5,4,3,2,1]) == 6    # e.g., (0,2): width 2 * min 3
```

### B. Randomized property tests vs oracle

```py
import random
from container import maxArea
from oracle_bruteforce import maxArea_bruteforce

def test_random_against_oracle():
    random.seed(7)
    for n in [2,3,4,5,8,16,25,50]:
        for _ in range(200):
            arr = [random.randint(0, 20) for _ in range(n)]
            assert maxArea(arr) == maxArea_bruteforce(arr)
```

### C. Scale sanity (no oracle)

```py
def test_scale_constant_array():
    n = 100_000
    arr = [10] * n
    assert maxArea(arr) == (n - 1) * 10
```

______________________________________________________________________

## 9) Pitfalls checklist (carried over from the anagram guide style)

- Move only the **shorter** side at each step.
- Compute and record area **before** advancing pointers.
- Width is `(r - l)`, not `(r - l + 1)`.
- Do not assume the optimum uses an endpoint; the sweep covers all candidates.
- Avoid premature micro-optimizations; `O(n)` is already optimal.
- In non-Python languages, beware integer overflow.

______________________________________________________________________

## 10) Interview-ready summary (drop-in for README)

```md
**Model**: maximize `A(i,j) = (j - i) * min(h[i], h[j])`.
**Rule**: always move the pointer at the shorter line.
**Why**: moving the taller side keeps the minimum ≤ current shorter height while shrinking width, so area cannot increase.
**Proof**: dominance argument + window invariant.
**Complexity**: `O(n)` time, `O(1)` space.
```

______________________________________________________________________

## 11) Suggested file layout (for your repo)

```
problems/
  0011-container-with-most-water/
    README.md
    container.py            # maxArea
    oracle_bruteforce.py    # maxArea_bruteforce
    tests/
      test_container.py
    chatgpt-guide.md        # this file
```
