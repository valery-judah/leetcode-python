# Solving LeetCode 242 “Valid Anagram” — Rigorous Interview Guide

> Purpose: a compact, reusable guide to derive, verify, implement, and defend solutions for LeetCode 242 in interviews and code reviews.

______________________________________________________________________

## 1) Problem Restatement

Given two strings `s` and `t`, return `True` if `t` is an anagram of `s`, else `False`. An anagram has identical character multiplicities. Order is irrelevant.

______________________________________________________________________

## 2) Assumptions and Constraints

Clarify before coding:

- **Alphabet**: ASCII only, or full Unicode? Case sensitivity? Whitespace and punctuation included?
- **Normalization**: If Unicode, should we normalize (e.g., NFC/NFKC)? Case-fold?
- **Input size**: bounds on `len(s)` and `len(t)`; memory constraints; streaming vs in‑memory.
- **Time/space targets**: interviewer may accept `O(n log n)` sort; `O(n)` counting is optimal.

Default if unstated: ASCII, case-sensitive, in‑memory, `n = len(s) = len(t)` up to a few 10^5.

______________________________________________________________________

## 3) Discovery Path (How to Arrive at a Solution)

1. **State the invariant you need**: equality of multisets of characters.
1. **Naive idea**: membership checks (`c in t`) fail because they ignore multiplicity.
1. **Key observation**: sorting equalizes order; counting equalizes multiplicity. Either proves multiset equality.
1. **Choose DS by constraints**:
   - Unknown or large alphabet → hash map counts.
   - Small fixed alphabet (ASCII) → fixed-size int array.
   - When unsure or rushed → sorting often passes and is shortest to code.

______________________________________________________________________

## 4) Algorithms and Trade‑offs

| Method | Time | Space | When to Use | Notes |
|---|---:|---:|---|---|
| Sort both strings | `O(n log n)` | `O(n)` | Fast to write; any alphabet | Correct by permutation equality after sort |
| Hash‑map counting | `O(n)` avg | `O(k)` | Large/unknown alphabets | Robust; needs careful decrements |
| Fixed array (ASCII) | `O(n)` | `O(1)` | Known small alphabet | Best constants; simplest invariant check |

`k` = number of distinct characters observed.

______________________________________________________________________

## 5) Correctness Sketches

**Sorting**: If sorted strings are equal, they contain exactly the same characters with the same multiplicities, hence are anagrams. Conversely, anagrams sort to the same sequence. ⇔ relation holds.

**Counting (hash map or array)**:

- Invariant: after processing the i‑th position of both strings, for every character `x`, `count[x]` equals `(# of x in s[0..i]) − (# of x in t[0..i])`.
- Initialization: all zero.
- Maintenance: increment on `s[i]`, decrement on `t[i]`.
- Termination: all counts zero ⇔ equal multiplicities.

Early failure: any decrement below zero implies `t` overuses some char, so not an anagram.

______________________________________________________________________

## 6) Complexity

- Sorting: time `O(n log n)`, extra space `O(n)` due to Python sorting copies for strings; or `O(1)` if sorting lists in place after conversion.
- Counting: time `O(n)` average; space `O(k)` hash map or `O(1)` fixed-size array.

______________________________________________________________________

## 7) Implementations (Python)

> Always start with an early length check.

### 7.1 Sorting

```python
from typing import Final

def is_anagram_sort(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    return sorted(s) == sorted(t)
```

### 7.2 Counting with dict

```python
from typing import Dict

def is_anagram_count(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    counts: Dict[str, int] = {}
    for cs, ct in zip(s, t):
        counts[cs] = counts.get(cs, 0) + 1
        counts[ct] = counts.get(ct, 0) - 1
    # all zeros
    return all(v == 0 for v in counts.values())
```

### 7.3 Counting with fixed array (ASCII)

```python
def is_anagram_ascii(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    # Assumes ASCII; if input may be non-ASCII, do not use this variant
    counts = [0] * 128
    for cs, ct in zip(s, t):
        o1 = ord(cs); o2 = ord(ct)
        if o1 >= 128 or o2 >= 128:
            return False  # or raise ValueError if contract is ASCII-only
        counts[o1] += 1
        counts[o2] -= 1
    return all(c == 0 for c in counts)
```

### 7.4 Unicode‑safe variant with normalization

```python
import unicodedata

def is_anagram_unicode(s: str, t: str, normalization: str = "NFC", casefold: bool = False) -> bool:
    if casefold:
        s, t = s.casefold(), t.casefold()
    s = unicodedata.normalize(normalization, s)
    t = unicodedata.normalize(normalization, t)
    if len(s) != len(t):
        return False
    counts = {}
    for cs, ct in zip(s, t):
        counts[cs] = counts.get(cs, 0) + 1
        counts[ct] = counts.get(ct, 0) - 1
    return all(v == 0 for v in counts.values())
```

______________________________________________________________________

## 8) Tests

### 8.1 Unit tests

```python
import unittest

class TestAnagram(unittest.TestCase):
    def test_empty(self):
        self.assertTrue(is_anagram_count("", ""))

    def test_len_mismatch(self):
        self.assertFalse(is_anagram_count("a", ""))

    def test_positive_simple(self):
        self.assertTrue(is_anagram_count("anagram", "nagaram"))

    def test_negative_simple(self):
        self.assertFalse(is_anagram_count("rat", "car"))

    def test_repeats(self):
        self.assertTrue(is_anagram_count("aabbcc", "baccab"))

    def test_ascii_variant(self):
        self.assertTrue(is_anagram_ascii("abc", "cba"))
        self.assertFalse(is_anagram_ascii("Ä", "A"))  # non-ASCII guarded

    def test_unicode_combining(self):
        # "é" can be U+00E9 or "e"+U+0301; normalize to compare
        self.assertTrue(is_anagram_unicode("éa", "a\u0065\u0301"))

if __name__ == "__main__":
    unittest.main()
```

### 8.2 Lightweight property tests (no external deps)

```python
import random
import string

def shuffle(s: str) -> str:
    arr = list(s)
    random.shuffle(arr)
    return "".join(arr)

alphabet = string.ascii_letters
for _ in range(200):
    n = random.randint(0, 200)
    s = "".join(random.choice(alphabet) for _ in range(n))
    assert is_anagram_count(s, shuffle(s))

for _ in range(200):
    a = "".join(random.choice("abc") for _ in range(50))
    b = "".join(random.choice("xyz") for _ in range(50))
    assert not is_anagram_count(a, b)
```

______________________________________________________________________

## 9) Pitfalls Checklist

- [ ] Forgot early **length check**.
- [ ] Used membership or set equality (ignores multiplicity).
- [ ] Claimed Unicode support without **normalization**.
- [ ] Used a fixed ASCII array on non‑ASCII input.
- [ ] Off‑by‑one in paired iteration.
- [ ] Mutated counts asymmetrically (only increments or only decrements).

______________________________________________________________________

## 10) Interview Talk‑track

### 10.1 Default script (≈25s)

“First, I check lengths and return False if they differ. If equal, I choose between sort and count. Sorting is `O(n log n)` and shortest to write. Counting is `O(n)` by maintaining a per‑char net count that ends at zero. For ASCII I use a fixed array for constant space and best constants; for Unicode I normalize (NFC) and use a dict. Correctness follows from multiset equality; the loop invariant is that after i steps, counts reflect the difference in multiplicities over prefixes. I can discuss trade‑offs or handle streaming if inputs are huge.”

### 10.2 If constraints are unknown

- Start with sorting to get a correct baseline fast.
- Say: “If we need linear time or large inputs, I will switch to counting.”

### 10.3 If pushed on performance

- Counting: `O(n)` time; space `O(k)` where `k` = distinct chars.
- ASCII array: `O(1)` space (128/256), fewer hash lookups, branch‑free inner loop.
- Note Python constant factors: `sorted` in C is fast for small `n`; for `n > ~1e5`, counting usually wins.

### 10.4 If Unicode/locale is raised

- Normalize both strings to NFC (or NFKC if compatibility desired).
- Optional `casefold()` for case‑insensitive.
- State limitation: code‑point counting ignores grapheme clusters; clarify acceptance.

### 10.5 If memory is tight or data is streaming

- Streaming files: single pass that increments for `s` and decrements for `t` per chunk; maintain dict/array counts; verify zeros at end.
- Very large but disk‑resident: external sort both files then merge‑scan; `O(n log n)` with low RAM.

### 10.6 Trade‑off one‑liners

- **Sort**: shortest code, any alphabet, `O(n log n)`.
- **Dict count**: linear time, handles Unicode, `O(k)` space.
- **ASCII array**: linear time, constant space, best constants.

### 10.7 Common traps to preempt

- Set or membership checks ignore multiplicity.
- Forgetting early length check.
- Claiming Unicode support without normalization.
- Using ASCII array on non‑ASCII input.

### 10.8 Decision tree (whiteboard)

```
Unknown constraints?
  └─ Yes → Sort now → pass tests → discuss upgrades.
Known need O(n) or large n?
  └─ Yes → Counting.
      ├─ Alphabet small fixed? → ASCII array.
      └─ Otherwise → Dict.
Unicode/case rules?
  └─ Normalize + optional casefold before count.
```

### 10.9 Micro‑derivation to narrate (invariant)

“Let `count[x]` be net multiplicity of `x`. Start zeros. For each i: `++count[s[i]]`, `--count[t[i]]`. If strings are anagrams, every char’s net is zero at end. If any `count[x]` dips negative during the scan, `t` overuses `x`, so we can early‑reject.”

### 10.10 Sample Q&A

- **Q:** Why not sort only one and binary‑search?\
  **A:** Loses multiplicity equality and worsens complexity.
- **Q:** Prove correctness of counting.\
  **A:** Loop invariant as above; termination with all zeros ⇔ equal multisets.
- **Q:** Space bound?\
  **A:** Dict `O(k)`, array `O(1)` for fixed alphabet.
- **Q:** Worst case for dict?\
  **A:** Many distinct code points increase `k`; still linear in `n` updates.
- **Q:** How to handle emojis?\
  **A:** Clarify requirement. If grapheme‑aware, need segmentation library; otherwise code‑point comparison per problem norms.

______________________________________________________________________

## 11) Extensions

- **Group Anagrams**: replace boolean check with canonical key (sorted string or count tuple).
- **Find All Anagrams in a String**: sliding window + differential counts.
- **Ransom Note**: one‑sided counting with nonnegative decrements.
- **Near‑anagram distance**: L1 distance of count vectors.
- **Streaming**: process files chunk‑by‑chunk, maintain counts per byte/char.

______________________________________________________________________

## Appendix A — Unicode Notes

- Combine **normalization** (NFC/NFKC) with **casefold** if case‑insensitive equality is desired.
- Be aware of grapheme clusters (emoji sequences, skin tones). Python iterates code points, not grapheme clusters. For interviews, code‑point counting is usually acceptable; clarify if needed.

______________________________________________________________________

## Appendix B — Reflection Prompts

Use these after coding to stress‑test your reasoning:

- What is the exact **invariant** my loop maintains? Can I state it in one sentence?
- Did I explicitly rule out incorrect strategies that ignore **multiplicity**?
- If I claim Unicode support, where do I **normalize** and why that form?
- What are my **failure modes** and the counterexamples that expose them?
- Which approach do I pick under **time pressure** vs under **performance** constraints, and why?
- Did I add the **length‑mismatch** test, and is it the very first line?
- Can I defend my **big‑O** plus constant factors and memory in 2 sentences?
