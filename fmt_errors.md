ruff check . --fix
E741 Ambiguous variable name: `l`
  --> old_leetcode/005. Longest Palindromic Substring.py:11:21
   |
 9 |     lenMax = 0
10 |
11 |     def anagramStat(l, r, res, lenMax):
   |                     ^
12 |         while l >= 0 and r < len(s) and s[l] == s[r]:
13 |             if r - l + 1 > lenMax:
   |

E741 Ambiguous variable name: `l`
  --> old_leetcode/005. Longest Palindromic Substring.py:16:13
   |
14 |                 lenMax = r - l + 1
15 |                 res = s[l: r + 1]
16 |             l -= 1
   |             ^
17 |             r += 1
18 |         return res, lenMax
   |

E741 Ambiguous variable name: `l`
  --> old_leetcode/005. Longest Palindromic Substring.py:21:9
   |
20 |     for i in range(len(s)):
21 |         l, r = i, i + 1
   |         ^
22 |         res, lenMax = anagramStat(l, r, res, lenMax)
   |

E741 Ambiguous variable name: `l`
  --> old_leetcode/005. Longest Palindromic Substring.py:24:9
   |
22 |         res, lenMax = anagramStat(l, r, res, lenMax)
23 |
24 |         l, r = i, i
   |         ^
25 |         res, lenMax = anagramStat(l, r, res, lenMax)
   |

E741 Ambiguous variable name: `l`
  --> old_leetcode/022. Generate Parentheses.py:11:16
   |
 9 |     out = []
10 |
11 |     def helper(l: int, r: int, brackets: str):
   |                ^
12 |         if not l and not r:
13 |             out.append(brackets)
   |

SIM110 Use `return all(v <= 1 for v in counter.values())` instead of `for` loop
  --> old_leetcode/036. Valid Sudoku.py:27:9
   |
25 |           counter = Counter(slice)
26 |           counter.pop(".")
27 | /         for v in counter.values():
28 | |             if v > 1:
29 | |                 return False
30 | |         return True
   | |___________________^
31 |
32 |       def getAreas(board: list[list[str]]):
   |
help: Replace with `return all(v <= 1 for v in counter.values())`

F811 Redefinition of unused `permute` from line 62
  --> old_leetcode/046. Permutations.py:79:5
   |
79 | def permute(nums: list[int]) -> list[list[int]]:
   |     ^^^^^^^ `permute` redefined here
80 |     candidates = set(nums)
81 |     res = []
   |
  ::: old_leetcode/046. Permutations.py:62:5
   |
61 | # leetCode solution without intensive copying
62 | def permute(nums: list[int]) -> list[list[int]]:
   |     ------- previous definition of `permute` here
63 |     def backtrack(curr):
64 |         if len(curr) == len(nums):
   |
help: Remove definition: `permute`

F811 Redefinition of unused `groupAnagrams_dict` from line 19
  --> old_leetcode/049. Group Anagrams.py:37:5
   |
36 | @test
37 | def groupAnagrams_dict(strs: list[str]) -> list[list[str]]:
   |     ^^^^^^^^^^^^^^^^^^ `groupAnagrams_dict` redefined here
38 |     anagrams = defaultdict(list)
39 |     for word in strs:
   |
  ::: old_leetcode/049. Group Anagrams.py:19:5
   |
18 | @test
19 | def groupAnagrams_dict(strs: list[str]) -> list[list[str]]:
   |     ------------------ previous definition of `groupAnagrams_dict` here
20 |     anagrams = defaultdict(list)
21 |     for word in strs:
   |
help: Remove definition: `groupAnagrams_dict`

B007 Loop control variable `i` not used within loop body
  --> old_leetcode/070. Climbing Stairs.py:23:9
   |
21 | def climb2(n: int) -> int:
22 |     one, two = 1, 1
23 |     for i in range(n - 1):
   |         ^
24 |         one, two = one + two, one
25 |     return one
   |
help: Rename unused `i` to `_i`

B006 Do not use mutable data structures for argument defaults
  --> old_leetcode/078. Subsets.py:68:33
   |
67 | def subsets_back2(nums: list[int]) -> list[list[int]]:
68 |     def backtrack(first=0, curr=[]):
   |                                 ^^
69 |         # if the combination is done
70 |         if len(curr) == k:
   |
help: Replace with `None`; initialize within function

B007 Loop control variable `k` not used within loop body
  --> old_leetcode/078. Subsets.py:83:9
   |
81 |     output = []
82 |     n = len(nums)
83 |     for k in range(n + 1):
   |         ^
84 |         backtrack()
85 |     return output
   |
help: Rename unused `k` to `_k`

E501 Line too long (117 > 100)
 --> old_leetcode/150. Evaluate Reverse Polish Notation.py:5:101
  |
3 | def evalRPN(tokens: list[str]) -> int:
4 |     stack = []
5 |     operations = {"+": lambda x, y: x + y, "-": lambda x, y: x - y, "*": lambda x, y: x * y, "/": lambda x, y: x / y}
  |                                                                                                     ^^^^^^^^^^^^^^^^^
6 |
7 |     for token in tokens:
  |

SIM110 Use `return any(nums_copy[i] == nums_copy[i - 1] for i in range(1, len(nums_copy)))` instead of `for` loop
  --> old_leetcode/217. Contains Duplicate.py:28:5
   |
26 |       nums_copy = nums[:] # Create a copy to avoid modifying the original list passed to the test
27 |       nums_copy.sort()
28 | /     for i in range(1, len(nums_copy)):
29 | |         if nums_copy[i] == nums_copy[i - 1]:
30 | |             return True
31 | |     return False
   | |________________^
   |
help: Replace with `return any(nums_copy[i] == nums_copy[i - 1] for i in range(1, len(nums_copy)))`

PT009 Use a regular `assert` instead of unittest-style `assertTrue`
  --> old_leetcode/217. Contains Duplicate.py:38:9
   |
36 |     def test_bruteforce(self):
37 |         print("\nTesting: contains_duplicate_brutforce")
38 |         self.assertTrue(contains_duplicate_brutforce([1, 2, 3, 1]), "Test Case 1 Failed (Bruteforce)")
   |         ^^^^^^^^^^^^^^^
39 |         self.assertFalse(contains_duplicate_brutforce([1, 2, 3, 4]), "Test Case 2 Failed (Bruteforce)")
40 |         self.assertTrue(contains_duplicate_brutforce([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]), "Test Case 3 Failed (Bruteforce)")
   |
help: Replace `assertTrue(...)` with `assert ...`

E501 Line too long (102 > 100)
  --> old_leetcode/217. Contains Duplicate.py:38:101
   |
36 |     def test_bruteforce(self):
37 |         print("\nTesting: contains_duplicate_brutforce")
38 |         self.assertTrue(contains_duplicate_brutforce([1, 2, 3, 1]), "Test Case 1 Failed (Bruteforce)")
   |                                                                                                     ^^
39 |         self.assertFalse(contains_duplicate_brutforce([1, 2, 3, 4]), "Test Case 2 Failed (Bruteforce)")
40 |         self.assertTrue(contains_duplicate_brutforce([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]), "Test Case 3 Failed (Bruteforce)")
   |

PT009 Use a regular `assert` instead of unittest-style `assertFalse`
  --> old_leetcode/217. Contains Duplicate.py:39:9
   |
37 |         print("\nTesting: contains_duplicate_brutforce")
38 |         self.assertTrue(contains_duplicate_brutforce([1, 2, 3, 1]), "Test Case 1 Failed (Bruteforce)")
39 |         self.assertFalse(contains_duplicate_brutforce([1, 2, 3, 4]), "Test Case 2 Failed (Bruteforce)")
   |         ^^^^^^^^^^^^^^^^
40 |         self.assertTrue(contains_duplicate_brutforce([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]), "Test Case 3 Failed (Bruteforce)")
41 |         self.assertFalse(contains_duplicate_brutforce([]), "Test Case 4 Failed (Bruteforce - Empty)")
   |
help: Replace `assertFalse(...)` with `assert ...`

E501 Line too long (103 > 100)
  --> old_leetcode/217. Contains Duplicate.py:39:101
   |
37 |         print("\nTesting: contains_duplicate_brutforce")
38 |         self.assertTrue(contains_duplicate_brutforce([1, 2, 3, 1]), "Test Case 1 Failed (Bruteforce)")
39 |         self.assertFalse(contains_duplicate_brutforce([1, 2, 3, 4]), "Test Case 2 Failed (Bruteforce)")
   |                                                                                                     ^^^
40 |         self.assertTrue(contains_duplicate_brutforce([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]), "Test Case 3 Failed (Bruteforce)")
41 |         self.assertFalse(contains_duplicate_brutforce([]), "Test Case 4 Failed (Bruteforce - Empty)")
   |

PT009 Use a regular `assert` instead of unittest-style `assertTrue`
  --> old_leetcode/217. Contains Duplicate.py:40:9
   |
38 |         self.assertTrue(contains_duplicate_brutforce([1, 2, 3, 1]), "Test Case 1 Failed (Bruteforce)")
39 |         self.assertFalse(contains_duplicate_brutforce([1, 2, 3, 4]), "Test Case 2 Failed (Bruteforce)")
40 |         self.assertTrue(contains_duplicate_brutforce([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]), "Test Case 3 Failed (Bruteforce)")
   |         ^^^^^^^^^^^^^^^
41 |         self.assertFalse(contains_duplicate_brutforce([]), "Test Case 4 Failed (Bruteforce - Empty)")
42 |         self.assertFalse(contains_duplicate_brutforce([5]), "Test Case 5 Failed (Bruteforce - Single Element)")
   |
help: Replace `assertTrue(...)` with `assert ...`

E501 Line too long (120 > 100)
  --> old_leetcode/217. Contains Duplicate.py:40:101
   |
38 |         self.assertTrue(contains_duplicate_brutforce([1, 2, 3, 1]), "Test Case 1 Failed (Bruteforce)")
39 |         self.assertFalse(contains_duplicate_brutforce([1, 2, 3, 4]), "Test Case 2 Failed (Bruteforce)")
40 |         self.assertTrue(contains_duplicate_brutforce([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]), "Test Case 3 Failed (Bruteforce)")
   |                                                                                                     ^^^^^^^^^^^^^^^^^^^^
41 |         self.assertFalse(contains_duplicate_brutforce([]), "Test Case 4 Failed (Bruteforce - Empty)")
42 |         self.assertFalse(contains_duplicate_brutforce([5]), "Test Case 5 Failed (Bruteforce - Single Element)")
   |

PT009 Use a regular `assert` instead of unittest-style `assertFalse`
  --> old_leetcode/217. Contains Duplicate.py:41:9
   |
39 |         self.assertFalse(contains_duplicate_brutforce([1, 2, 3, 4]), "Test Case 2 Failed (Bruteforce)")
40 |         self.assertTrue(contains_duplicate_brutforce([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]), "Test Case 3 Failed (Bruteforce)")
41 |         self.assertFalse(contains_duplicate_brutforce([]), "Test Case 4 Failed (Bruteforce - Empty)")
   |         ^^^^^^^^^^^^^^^^
42 |         self.assertFalse(contains_duplicate_brutforce([5]), "Test Case 5 Failed (Bruteforce - Single Element)")
43 |         self.assertTrue(contains_duplicate_brutforce([0, 0]), "Test Case 6 Failed (Bruteforce - Zeros)")
   |
help: Replace `assertFalse(...)` with `assert ...`

E501 Line too long (101 > 100)
  --> old_leetcode/217. Contains Duplicate.py:41:101
   |
39 |         self.assertFalse(contains_duplicate_brutforce([1, 2, 3, 4]), "Test Case 2 Failed (Bruteforce)")
40 |         self.assertTrue(contains_duplicate_brutforce([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]), "Test Case 3 Failed (Bruteforce)")
41 |         self.assertFalse(contains_duplicate_brutforce([]), "Test Case 4 Failed (Bruteforce - Empty)")
   |                                                                                                     ^
42 |         self.assertFalse(contains_duplicate_brutforce([5]), "Test Case 5 Failed (Bruteforce - Single Element)")
43 |         self.assertTrue(contains_duplicate_brutforce([0, 0]), "Test Case 6 Failed (Bruteforce - Zeros)")
   |

PT009 Use a regular `assert` instead of unittest-style `assertFalse`
  --> old_leetcode/217. Contains Duplicate.py:42:9
   |
40 |         self.assertTrue(contains_duplicate_brutforce([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]), "Test Case 3 Failed (Bruteforce)")
41 |         self.assertFalse(contains_duplicate_brutforce([]), "Test Case 4 Failed (Bruteforce - Empty)")
42 |         self.assertFalse(contains_duplicate_brutforce([5]), "Test Case 5 Failed (Bruteforce - Single Element)")
   |         ^^^^^^^^^^^^^^^^
43 |         self.assertTrue(contains_duplicate_brutforce([0, 0]), "Test Case 6 Failed (Bruteforce - Zeros)")
44 |         self.assertTrue(contains_duplicate_brutforce([-1, -2, -1]), "Test Case 7 Failed (Bruteforce - Negatives)")
   |
help: Replace `assertFalse(...)` with `assert ...`

E501 Line too long (111 > 100)
  --> old_leetcode/217. Contains Duplicate.py:42:101
   |
40 |         self.assertTrue(contains_duplicate_brutforce([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]), "Test Case 3 Failed (Bruteforce)")
41 |         self.assertFalse(contains_duplicate_brutforce([]), "Test Case 4 Failed (Bruteforce - Empty)")
42 |         self.assertFalse(contains_duplicate_brutforce([5]), "Test Case 5 Failed (Bruteforce - Single Element)")
   |                                                                                                     ^^^^^^^^^^^
43 |         self.assertTrue(contains_duplicate_brutforce([0, 0]), "Test Case 6 Failed (Bruteforce - Zeros)")
44 |         self.assertTrue(contains_duplicate_brutforce([-1, -2, -1]), "Test Case 7 Failed (Bruteforce - Negatives)")
   |

PT009 Use a regular `assert` instead of unittest-style `assertTrue`
  --> old_leetcode/217. Contains Duplicate.py:43:9
   |
41 |         self.assertFalse(contains_duplicate_brutforce([]), "Test Case 4 Failed (Bruteforce - Empty)")
42 |         self.assertFalse(contains_duplicate_brutforce([5]), "Test Case 5 Failed (Bruteforce - Single Element)")
43 |         self.assertTrue(contains_duplicate_brutforce([0, 0]), "Test Case 6 Failed (Bruteforce - Zeros)")
   |         ^^^^^^^^^^^^^^^
44 |         self.assertTrue(contains_duplicate_brutforce([-1, -2, -1]), "Test Case 7 Failed (Bruteforce - Negatives)")
   |
help: Replace `assertTrue(...)` with `assert ...`

E501 Line too long (104 > 100)
  --> old_leetcode/217. Contains Duplicate.py:43:101
   |
41 |         self.assertFalse(contains_duplicate_brutforce([]), "Test Case 4 Failed (Bruteforce - Empty)")
42 |         self.assertFalse(contains_duplicate_brutforce([5]), "Test Case 5 Failed (Bruteforce - Single Element)")
43 |         self.assertTrue(contains_duplicate_brutforce([0, 0]), "Test Case 6 Failed (Bruteforce - Zeros)")
   |                                                                                                     ^^^^
44 |         self.assertTrue(contains_duplicate_brutforce([-1, -2, -1]), "Test Case 7 Failed (Bruteforce - Negatives)")
   |

PT009 Use a regular `assert` instead of unittest-style `assertTrue`
  --> old_leetcode/217. Contains Duplicate.py:44:9
   |
42 |         self.assertFalse(contains_duplicate_brutforce([5]), "Test Case 5 Failed (Bruteforce - Single Element)")
43 |         self.assertTrue(contains_duplicate_brutforce([0, 0]), "Test Case 6 Failed (Bruteforce - Zeros)")
44 |         self.assertTrue(contains_duplicate_brutforce([-1, -2, -1]), "Test Case 7 Failed (Bruteforce - Negatives)")
   |         ^^^^^^^^^^^^^^^
45 |
46 |     def test_set(self):
   |
help: Replace `assertTrue(...)` with `assert ...`

E501 Line too long (114 > 100)
  --> old_leetcode/217. Contains Duplicate.py:44:101
   |
42 |         self.assertFalse(contains_duplicate_brutforce([5]), "Test Case 5 Failed (Bruteforce - Single Element)")
43 |         self.assertTrue(contains_duplicate_brutforce([0, 0]), "Test Case 6 Failed (Bruteforce - Zeros)")
44 |         self.assertTrue(contains_duplicate_brutforce([-1, -2, -1]), "Test Case 7 Failed (Bruteforce - Negatives)")
   |                                                                                                     ^^^^^^^^^^^^^^
45 |
46 |     def test_set(self):
   |

PT009 Use a regular `assert` instead of unittest-style `assertTrue`
  --> old_leetcode/217. Contains Duplicate.py:48:9
   |
46 |     def test_set(self):
47 |         print("\nTesting: contains_duplicate_set")
48 |         self.assertTrue(contains_duplicate_set([1, 2, 3, 1]), "Test Case 1 Failed (Set)")
   |         ^^^^^^^^^^^^^^^
49 |         self.assertFalse(contains_duplicate_set([1, 2, 3, 4]), "Test Case 2 Failed (Set)")
50 |         self.assertTrue(contains_duplicate_set([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]), "Test Case 3 Failed (Set)")
   |
help: Replace `assertTrue(...)` with `assert ...`

PT009 Use a regular `assert` instead of unittest-style `assertFalse`
  --> old_leetcode/217. Contains Duplicate.py:49:9
   |
47 |         print("\nTesting: contains_duplicate_set")
48 |         self.assertTrue(contains_duplicate_set([1, 2, 3, 1]), "Test Case 1 Failed (Set)")
49 |         self.assertFalse(contains_duplicate_set([1, 2, 3, 4]), "Test Case 2 Failed (Set)")
   |         ^^^^^^^^^^^^^^^^
50 |         self.assertTrue(contains_duplicate_set([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]), "Test Case 3 Failed (Set)")
51 |         self.assertFalse(contains_duplicate_set([]), "Test Case 4 Failed (Set - Empty)")
   |
help: Replace `assertFalse(...)` with `assert ...`

PT009 Use a regular `assert` instead of unittest-style `assertTrue`
  --> old_leetcode/217. Contains Duplicate.py:50:9
   |
48 |         self.assertTrue(contains_duplicate_set([1, 2, 3, 1]), "Test Case 1 Failed (Set)")
49 |         self.assertFalse(contains_duplicate_set([1, 2, 3, 4]), "Test Case 2 Failed (Set)")
50 |         self.assertTrue(contains_duplicate_set([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]), "Test Case 3 Failed (Set)")
   |         ^^^^^^^^^^^^^^^
51 |         self.assertFalse(contains_duplicate_set([]), "Test Case 4 Failed (Set - Empty)")
52 |         self.assertFalse(contains_duplicate_set([5]), "Test Case 5 Failed (Set - Single Element)")
   |
help: Replace `assertTrue(...)` with `assert ...`

E501 Line too long (107 > 100)
  --> old_leetcode/217. Contains Duplicate.py:50:101
   |
48 |         self.assertTrue(contains_duplicate_set([1, 2, 3, 1]), "Test Case 1 Failed (Set)")
49 |         self.assertFalse(contains_duplicate_set([1, 2, 3, 4]), "Test Case 2 Failed (Set)")
50 |         self.assertTrue(contains_duplicate_set([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]), "Test Case 3 Failed (Set)")
   |                                                                                                     ^^^^^^^
51 |         self.assertFalse(contains_duplicate_set([]), "Test Case 4 Failed (Set - Empty)")
52 |         self.assertFalse(contains_duplicate_set([5]), "Test Case 5 Failed (Set - Single Element)")
   |

PT009 Use a regular `assert` instead of unittest-style `assertFalse`
  --> old_leetcode/217. Contains Duplicate.py:51:9
   |
49 |         self.assertFalse(contains_duplicate_set([1, 2, 3, 4]), "Test Case 2 Failed (Set)")
50 |         self.assertTrue(contains_duplicate_set([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]), "Test Case 3 Failed (Set)")
51 |         self.assertFalse(contains_duplicate_set([]), "Test Case 4 Failed (Set - Empty)")
   |         ^^^^^^^^^^^^^^^^
52 |         self.assertFalse(contains_duplicate_set([5]), "Test Case 5 Failed (Set - Single Element)")
53 |         self.assertTrue(contains_duplicate_set([0, 0]), "Test Case 6 Failed (Set - Zeros)")
   |
help: Replace `assertFalse(...)` with `assert ...`

PT009 Use a regular `assert` instead of unittest-style `assertFalse`
  --> old_leetcode/217. Contains Duplicate.py:52:9
   |
50 |         self.assertTrue(contains_duplicate_set([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]), "Test Case 3 Failed (Set)")
51 |         self.assertFalse(contains_duplicate_set([]), "Test Case 4 Failed (Set - Empty)")
52 |         self.assertFalse(contains_duplicate_set([5]), "Test Case 5 Failed (Set - Single Element)")
   |         ^^^^^^^^^^^^^^^^
53 |         self.assertTrue(contains_duplicate_set([0, 0]), "Test Case 6 Failed (Set - Zeros)")
54 |         self.assertTrue(contains_duplicate_set([-1, -2, -1]), "Test Case 7 Failed (Set - Negatives)")
   |
help: Replace `assertFalse(...)` with `assert ...`

PT009 Use a regular `assert` instead of unittest-style `assertTrue`
  --> old_leetcode/217. Contains Duplicate.py:53:9
   |
51 |         self.assertFalse(contains_duplicate_set([]), "Test Case 4 Failed (Set - Empty)")
52 |         self.assertFalse(contains_duplicate_set([5]), "Test Case 5 Failed (Set - Single Element)")
53 |         self.assertTrue(contains_duplicate_set([0, 0]), "Test Case 6 Failed (Set - Zeros)")
   |         ^^^^^^^^^^^^^^^
54 |         self.assertTrue(contains_duplicate_set([-1, -2, -1]), "Test Case 7 Failed (Set - Negatives)")
   |
help: Replace `assertTrue(...)` with `assert ...`

PT009 Use a regular `assert` instead of unittest-style `assertTrue`
  --> old_leetcode/217. Contains Duplicate.py:54:9
   |
52 |         self.assertFalse(contains_duplicate_set([5]), "Test Case 5 Failed (Set - Single Element)")
53 |         self.assertTrue(contains_duplicate_set([0, 0]), "Test Case 6 Failed (Set - Zeros)")
54 |         self.assertTrue(contains_duplicate_set([-1, -2, -1]), "Test Case 7 Failed (Set - Negatives)")
   |         ^^^^^^^^^^^^^^^
55 |
56 |     def test_sorting(self):
   |
help: Replace `assertTrue(...)` with `assert ...`

E501 Line too long (101 > 100)
  --> old_leetcode/217. Contains Duplicate.py:54:101
   |
52 |         self.assertFalse(contains_duplicate_set([5]), "Test Case 5 Failed (Set - Single Element)")
53 |         self.assertTrue(contains_duplicate_set([0, 0]), "Test Case 6 Failed (Set - Zeros)")
54 |         self.assertTrue(contains_duplicate_set([-1, -2, -1]), "Test Case 7 Failed (Set - Negatives)")
   |                                                                                                     ^
55 |
56 |     def test_sorting(self):
   |

PT009 Use a regular `assert` instead of unittest-style `assertTrue`
  --> old_leetcode/217. Contains Duplicate.py:59:9
   |
57 |         print("\nTesting: contains_duplicates_sorting_approach")
58 |         # Pass copies because the function sorts the list in place
59 |         self.assertTrue(contains_duplicates_sorting_approach([1, 2, 3, 1]), "Test Case 1 Failed (Sorting)")
   |         ^^^^^^^^^^^^^^^
60 |         self.assertFalse(contains_duplicates_sorting_approach([1, 2, 3, 4]), "Test Case 2 Failed (Sorting)")
61 |         self.assertTrue(contains_duplicates_sorting_approach([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]), "Test Case 3 Failed (Sorting)")
   |
help: Replace `assertTrue(...)` with `assert ...`

E501 Line too long (107 > 100)
  --> old_leetcode/217. Contains Duplicate.py:59:101
   |
57 |         print("\nTesting: contains_duplicates_sorting_approach")
58 |         # Pass copies because the function sorts the list in place
59 |         self.assertTrue(contains_duplicates_sorting_approach([1, 2, 3, 1]), "Test Case 1 Failed (Sorting)")
   |                                                                                                     ^^^^^^^
60 |         self.assertFalse(contains_duplicates_sorting_approach([1, 2, 3, 4]), "Test Case 2 Failed (Sorting)")
61 |         self.assertTrue(contains_duplicates_sorting_approach([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]), "Test Case 3 Failed (Sorting)")
   |

PT009 Use a regular `assert` instead of unittest-style `assertFalse`
  --> old_leetcode/217. Contains Duplicate.py:60:9
   |
58 |         # Pass copies because the function sorts the list in place
59 |         self.assertTrue(contains_duplicates_sorting_approach([1, 2, 3, 1]), "Test Case 1 Failed (Sorting)")
60 |         self.assertFalse(contains_duplicates_sorting_approach([1, 2, 3, 4]), "Test Case 2 Failed (Sorting)")
   |         ^^^^^^^^^^^^^^^^
61 |         self.assertTrue(contains_duplicates_sorting_approach([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]), "Test Case 3 Failed (Sorting)")
62 |         self.assertFalse(contains_duplicates_sorting_approach([]), "Test Case 4 Failed (Sorting - Empty)")
   |
help: Replace `assertFalse(...)` with `assert ...`

E501 Line too long (108 > 100)
  --> old_leetcode/217. Contains Duplicate.py:60:101
   |
58 |         # Pass copies because the function sorts the list in place
59 |         self.assertTrue(contains_duplicates_sorting_approach([1, 2, 3, 1]), "Test Case 1 Failed (Sorting)")
60 |         self.assertFalse(contains_duplicates_sorting_approach([1, 2, 3, 4]), "Test Case 2 Failed (Sorting)")
   |                                                                                                     ^^^^^^^^
61 |         self.assertTrue(contains_duplicates_sorting_approach([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]), "Test Case 3 Failed (Sorting)")
62 |         self.assertFalse(contains_duplicates_sorting_approach([]), "Test Case 4 Failed (Sorting - Empty)")
   |

PT009 Use a regular `assert` instead of unittest-style `assertTrue`
  --> old_leetcode/217. Contains Duplicate.py:61:9
   |
59 |         self.assertTrue(contains_duplicates_sorting_approach([1, 2, 3, 1]), "Test Case 1 Failed (Sorting)")
60 |         self.assertFalse(contains_duplicates_sorting_approach([1, 2, 3, 4]), "Test Case 2 Failed (Sorting)")
61 |         self.assertTrue(contains_duplicates_sorting_approach([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]), "Test Case 3 Failed (Sorting)")
   |         ^^^^^^^^^^^^^^^
62 |         self.assertFalse(contains_duplicates_sorting_approach([]), "Test Case 4 Failed (Sorting - Empty)")
63 |         self.assertFalse(contains_duplicates_sorting_approach([5]), "Test Case 5 Failed (Sorting - Single Element)")
   |
help: Replace `assertTrue(...)` with `assert ...`

E501 Line too long (125 > 100)
  --> old_leetcode/217. Contains Duplicate.py:61:101
   |
59 |         self.assertTrue(contains_duplicates_sorting_approach([1, 2, 3, 1]), "Test Case 1 Failed (Sorting)")
60 |         self.assertFalse(contains_duplicates_sorting_approach([1, 2, 3, 4]), "Test Case 2 Failed (Sorting)")
61 |         self.assertTrue(contains_duplicates_sorting_approach([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]), "Test Case 3 Failed (Sorting)")
   |                                                                                                     ^^^^^^^^^^^^^^^^^^^^^^^^^
62 |         self.assertFalse(contains_duplicates_sorting_approach([]), "Test Case 4 Failed (Sorting - Empty)")
63 |         self.assertFalse(contains_duplicates_sorting_approach([5]), "Test Case 5 Failed (Sorting - Single Element)")
   |

PT009 Use a regular `assert` instead of unittest-style `assertFalse`
  --> old_leetcode/217. Contains Duplicate.py:62:9
   |
60 |         self.assertFalse(contains_duplicates_sorting_approach([1, 2, 3, 4]), "Test Case 2 Failed (Sorting)")
61 |         self.assertTrue(contains_duplicates_sorting_approach([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]), "Test Case 3 Failed (Sorting)")
62 |         self.assertFalse(contains_duplicates_sorting_approach([]), "Test Case 4 Failed (Sorting - Empty)")
   |         ^^^^^^^^^^^^^^^^
63 |         self.assertFalse(contains_duplicates_sorting_approach([5]), "Test Case 5 Failed (Sorting - Single Element)")
64 |         self.assertTrue(contains_duplicates_sorting_approach([0, 0]), "Test Case 6 Failed (Sorting - Zeros)")
   |
help: Replace `assertFalse(...)` with `assert ...`

E501 Line too long (106 > 100)
  --> old_leetcode/217. Contains Duplicate.py:62:101
   |
60 |         self.assertFalse(contains_duplicates_sorting_approach([1, 2, 3, 4]), "Test Case 2 Failed (Sorting)")
61 |         self.assertTrue(contains_duplicates_sorting_approach([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]), "Test Case 3 Failed (Sorting)")
62 |         self.assertFalse(contains_duplicates_sorting_approach([]), "Test Case 4 Failed (Sorting - Empty)")
   |                                                                                                     ^^^^^^
63 |         self.assertFalse(contains_duplicates_sorting_approach([5]), "Test Case 5 Failed (Sorting - Single Element)")
64 |         self.assertTrue(contains_duplicates_sorting_approach([0, 0]), "Test Case 6 Failed (Sorting - Zeros)")
   |

PT009 Use a regular `assert` instead of unittest-style `assertFalse`
  --> old_leetcode/217. Contains Duplicate.py:63:9
   |
61 |         self.assertTrue(contains_duplicates_sorting_approach([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]), "Test Case 3 Failed (Sorting)")
62 |         self.assertFalse(contains_duplicates_sorting_approach([]), "Test Case 4 Failed (Sorting - Empty)")
63 |         self.assertFalse(contains_duplicates_sorting_approach([5]), "Test Case 5 Failed (Sorting - Single Element)")
   |         ^^^^^^^^^^^^^^^^
64 |         self.assertTrue(contains_duplicates_sorting_approach([0, 0]), "Test Case 6 Failed (Sorting - Zeros)")
65 |         self.assertTrue(contains_duplicates_sorting_approach([-1, -2, -1]), "Test Case 7 Failed (Sorting - Negatives)")
   |
help: Replace `assertFalse(...)` with `assert ...`

E501 Line too long (116 > 100)
  --> old_leetcode/217. Contains Duplicate.py:63:101
   |
61 |         self.assertTrue(contains_duplicates_sorting_approach([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]), "Test Case 3 Failed (Sorting)")
62 |         self.assertFalse(contains_duplicates_sorting_approach([]), "Test Case 4 Failed (Sorting - Empty)")
63 |         self.assertFalse(contains_duplicates_sorting_approach([5]), "Test Case 5 Failed (Sorting - Single Element)")
   |                                                                                                     ^^^^^^^^^^^^^^^^
64 |         self.assertTrue(contains_duplicates_sorting_approach([0, 0]), "Test Case 6 Failed (Sorting - Zeros)")
65 |         self.assertTrue(contains_duplicates_sorting_approach([-1, -2, -1]), "Test Case 7 Failed (Sorting - Negatives)")
   |

PT009 Use a regular `assert` instead of unittest-style `assertTrue`
  --> old_leetcode/217. Contains Duplicate.py:64:9
   |
62 |         self.assertFalse(contains_duplicates_sorting_approach([]), "Test Case 4 Failed (Sorting - Empty)")
63 |         self.assertFalse(contains_duplicates_sorting_approach([5]), "Test Case 5 Failed (Sorting - Single Element)")
64 |         self.assertTrue(contains_duplicates_sorting_approach([0, 0]), "Test Case 6 Failed (Sorting - Zeros)")
   |         ^^^^^^^^^^^^^^^
65 |         self.assertTrue(contains_duplicates_sorting_approach([-1, -2, -1]), "Test Case 7 Failed (Sorting - Negatives)")
   |
help: Replace `assertTrue(...)` with `assert ...`

E501 Line too long (109 > 100)
  --> old_leetcode/217. Contains Duplicate.py:64:101
   |
62 |         self.assertFalse(contains_duplicates_sorting_approach([]), "Test Case 4 Failed (Sorting - Empty)")
63 |         self.assertFalse(contains_duplicates_sorting_approach([5]), "Test Case 5 Failed (Sorting - Single Element)")
64 |         self.assertTrue(contains_duplicates_sorting_approach([0, 0]), "Test Case 6 Failed (Sorting - Zeros)")
   |                                                                                                     ^^^^^^^^^
65 |         self.assertTrue(contains_duplicates_sorting_approach([-1, -2, -1]), "Test Case 7 Failed (Sorting - Negatives)")
   |

PT009 Use a regular `assert` instead of unittest-style `assertTrue`
  --> old_leetcode/217. Contains Duplicate.py:65:9
   |
63 |         self.assertFalse(contains_duplicates_sorting_approach([5]), "Test Case 5 Failed (Sorting - Single Element)")
64 |         self.assertTrue(contains_duplicates_sorting_approach([0, 0]), "Test Case 6 Failed (Sorting - Zeros)")
65 |         self.assertTrue(contains_duplicates_sorting_approach([-1, -2, -1]), "Test Case 7 Failed (Sorting - Negatives)")
   |         ^^^^^^^^^^^^^^^
66 |
67 | # This allows running the tests from the command line
   |
help: Replace `assertTrue(...)` with `assert ...`

E501 Line too long (119 > 100)
  --> old_leetcode/217. Contains Duplicate.py:65:101
   |
63 |         self.assertFalse(contains_duplicates_sorting_approach([5]), "Test Case 5 Failed (Sorting - Single Element)")
64 |         self.assertTrue(contains_duplicates_sorting_approach([0, 0]), "Test Case 6 Failed (Sorting - Zeros)")
65 |         self.assertTrue(contains_duplicates_sorting_approach([-1, -2, -1]), "Test Case 7 Failed (Sorting - Negatives)")
   |                                                                                                     ^^^^^^^^^^^^^^^^^^^
66 |
67 | # This allows running the tests from the command line
   |

B007 Loop control variable `n` not used within loop body
  --> old_leetcode/238. Product of Array Except Self.py:11:12
   |
 9 | def productExceptSelf(nums: list[int]) -> list[int]:
10 |     out = [1] * len(nums)
11 |     for i, n in enumerate(nums):
   |            ^
12 |         for j in range(0, len(nums)):
13 |             if i != j:
   |
help: Rename unused `n` to `_n`

F841 Local variable `product` is assigned to but never used
  --> old_leetcode/238. Product of Array Except Self.py:29:5
   |
27 | @test
28 | def productExceptSelf_optimized(nums: list[int]) -> list[int]:
29 |     product = [1] * len(nums)
   |     ^^^^^^^
30 |
31 |     for i in range(1, len(nums)):
   |
help: Remove assignment to unused variable `product`

B007 Loop control variable `i` not used within loop body
  --> old_leetcode/238. Product of Array Except Self.py:31:9
   |
29 |     product = [1] * len(nums)
30 |
31 |     for i in range(1, len(nums)):
   |         ^
32 |         pass
   |
help: Rename unused `i` to `_i`

E501 Line too long (107 > 100)
  --> old_leetcode/295. Find Median from Data Stream.py:43:101
   |
42 |     def addNum(self, num: int) -> None:
43 |         print(f"before: n: {num},    left: {self.leftHeap}, median:{self.median}, right: {self.rightHeap}")
   |                                                                                                     ^^^^^^^
44 |         if not self.median:
45 |             self.median.append(num)
   |

E501 Line too long (105 > 100)
  --> old_leetcode/295. Find Median from Data Stream.py:67:101
   |
65 |                 self.median.pop(0)
66 |
67 |         print(f"after: n: {num},   left: {self.leftHeap}, median:{self.median}, right: {self.rightHeap}")
   |                                                                                                     ^^^^^
68 |
69 |     def findMedian(self) -> float:
   |

B007 Loop control variable `i` not used within loop body
  --> old_leetcode/355. Design Twitter.py:25:13
   |
23 |     def getNewsFeed(self, userId: int) -> list[int]:
24 |         res = []
25 |         for i in range(len(self.tweets[userId])):
   |             ^
26 |             res.append(heapq.heappop(self.tweets[userId]))
27 |         return res
   |
help: Rename unused `i` to `_i`

E741 Ambiguous variable name: `l`
 --> old_leetcode/424. Longest Repeating Character Replacement.py:2:5
  |
1 | def characterReplacement(s: str, k: int) -> int:
2 |     l = 0
  |     ^
3 |     count = {}
4 |     res = 0
  |

E741 Ambiguous variable name: `l`
  --> old_leetcode/424. Longest Repeating Character Replacement.py:11:13
   |
 9 |         while (r - l + 1) - max(count.values()) > k:
10 |             count[s[l]] -= 1
11 |             l += 1
   |             ^
12 |         res = max(res, r - l + 1)
13 |     return res
   |

B007 Loop control variable `j` not used within loop body
  --> old_leetcode/424. Longest Repeating Character Replacement.py:30:13
   |
28 | def characterReplacement_second(s: str, k: int) -> int:
29 |     for i in range(len(s)):
30 |         for j in range(i + 1, len(s)):
   |             ^
31 |             pass
   |
help: Rename unused `j` to `_j`

E741 Ambiguous variable name: `l`
 --> old_leetcode/567. Permutation in String.py:5:5
  |
4 | def checkInclusion(s1: str, s2: str) -> bool:
5 |     l = 0
  |     ^
6 |     firstCount = Counter(s1)
7 |     stringCount = {}
  |

F841 Local variable `l` is assigned to but never used
 --> old_leetcode/567. Permutation in String.py:5:5
  |
4 | def checkInclusion(s1: str, s2: str) -> bool:
5 |     l = 0
  |     ^
6 |     firstCount = Counter(s1)
7 |     stringCount = {}
  |
help: Remove assignment to unused variable `l`

F841 Local variable `firstCount` is assigned to but never used
 --> old_leetcode/567. Permutation in String.py:6:5
  |
4 | def checkInclusion(s1: str, s2: str) -> bool:
5 |     l = 0
6 |     firstCount = Counter(s1)
  |     ^^^^^^^^^^
7 |     stringCount = {}
8 |     for i in range(len(s1) - len(s1)):
  |
help: Remove assignment to unused variable `firstCount`

F841 Local variable `stringCount` is assigned to but never used
 --> old_leetcode/567. Permutation in String.py:7:5
  |
5 |     l = 0
6 |     firstCount = Counter(s1)
7 |     stringCount = {}
  |     ^^^^^^^^^^^
8 |     for i in range(len(s1) - len(s1)):
9 |         word2check = s2[i:i + len(s1)]
  |
help: Remove assignment to unused variable `stringCount`

F841 Local variable `word2check` is assigned to but never used
 --> old_leetcode/567. Permutation in String.py:9:9
  |
7 |     stringCount = {}
8 |     for i in range(len(s1) - len(s1)):
9 |         word2check = s2[i:i + len(s1)]
  |         ^^^^^^^^^^
  |
help: Remove assignment to unused variable `word2check`

E741 Ambiguous variable name: `l`
  --> old_leetcode/647. Palindromic Substrings.py:10:32
   |
 8 |     res = 0
 9 |
10 |     def getPalindromeNumber(s, l, r):
   |                                ^
11 |         res = 0
12 |         while l >= 0 and r < len(s) and s[l] == s[r]:
   |

E741 Ambiguous variable name: `l`
  --> old_leetcode/647. Palindromic Substrings.py:14:13
   |
12 |         while l >= 0 and r < len(s) and s[l] == s[r]:
13 |             res += 1
14 |             l -= 1
   |             ^
15 |             r += 1
16 |         return res
   |

E741 Ambiguous variable name: `l`
  --> old_leetcode/704. BinarySearch.py:10:5
   |
 8 |             return -1
 9 |
10 |     l = 0
   |     ^
11 |     r = len(nums) - 1
   |

E741 Ambiguous variable name: `l`
  --> old_leetcode/704. BinarySearch.py:22:17
   |
20 |             print(f"l: {l}, median: {median}, r: {r}")
21 |             if target > nums[median]:
22 |                 l = median
   |                 ^
23 |             elif target == nums[median]:
24 |                 return median
   |

F841 Local variable `p` is assigned to but never used
  --> old_leetcode/890. Find and Replace Pattern.py:10:5
   |
 8 |     # Testing setdefault
 9 |     m = {}
10 |     p = [m.setdefault(c, len(m)) for c in "aqq"]
   |     ^
11 |     print(m)
   |
help: Remove assignment to unused variable `p`

SIM201 Use `len(word) != len(cur_pattern)` instead of `not len(word) == len(cur_pattern)`
  --> old_leetcode/890. Find and Replace Pattern.py:19:12
   |
17 |         word2pattern = dict()
18 |         pattern2word = dict()
19 |         if not len(word) == len(cur_pattern):
   |            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
20 |             return False
21 |         for i in range(len(word)):
   |
help: Replace with `!=` operator

E501 Line too long (157 > 100)
  --> old_leetcode/downloaders/instagram.py:19:101
   |
17 | …
18 | …
19 | …sername}, {followee.full_name}, {followee.followers}, {followee.follows}, {followee.username}")
   |                                        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
20 | …
21 | …
   |

SIM115 Use a context manager for opening files
  --> old_leetcode/downloaders/instagram.py:20:16
   |
18 |     for followee in profile.get_followers():
19 |         follow_list.append(f"https://instagram.com/{followee.username}, {followee.full_name}, {followee.followers}, {followee.follows}…
20 |         file = open("argentinafamilty_followers.txt", "a+")
   |                ^^^^
21 |         file.write(follow_list[count])
22 |         file.write("\n")
   |

B904 Within an `except` clause, raise exceptions with `raise ... from err` or `raise ... from None` to distinguish them from errors in exception handling
  --> old_leetcode/fluent_python/BingoCage.py:17:13
   |
15 |             return self._items.pop()
16 |         except IndexError:
17 |             raise LookupError("pick from empty BingoCage")  # <4>
   |             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
18 |
19 |     def __call__(self):  # <5>
   |

E501 Line too long (103 > 100)
  --> old_leetcode/leetcode_015_3Sum.py:15:101
   |
13 |     def test_3_sum(self):
14 |         testcases = [
15 |             TestData(name="case 0", numbers=[-1, 0, 1, 2, -1, -4], expected=[[-1, -1, 2], [-1, 0, 1]]),
   |                                                                                                     ^^^
16 |             TestData(name="case 0", numbers=[0, 0, 0], expected=[[0, 0, 0]])
17 |         ]
   |

PT009 Use a regular `assert` instead of unittest-style `assertListEqual`
  --> old_leetcode/leetcode_015_3Sum.py:20:13
   |
18 |         for case in testcases:
19 |             actual = Solution.three_sum_sorted(nums=case.numbers)
20 |             self.assertListEqual(
   |             ^^^^^^^^^^^^^^^^^^^^
21 |                 case.expected,
22 |                 actual,
   |
help: Replace `assertListEqual(...)` with `assert ...`

E501 Line too long (123 > 100)
  --> old_leetcode/leetcode_094_InOrderTraversal.py:22:101
   |
20 |     def test_3_sum(self):
21 |         testcases = [
22 |             TestData(name="case 0", root=TreeNode(val=1, right=TreeNode(val=2, left=TreeNode(val=3))), expected=[1, 3, 2]),
   |                                                                                                     ^^^^^^^^^^^^^^^^^^^^^^^
23 |             TestData(name="case 1", root=None, expected=[])
24 |         ]
   |

PT009 Use a regular `assert` instead of unittest-style `assertListEqual`
  --> old_leetcode/leetcode_094_InOrderTraversal.py:27:13
   |
25 |         for case in testcases:
26 |             actual = Solution.inorder_traversal(root=case.root)
27 |             self.assertListEqual(
   |             ^^^^^^^^^^^^^^^^^^^^
28 |                 case.expected,
29 |                 actual,
   |
help: Replace `assertListEqual(...)` with `assert ...`

E501 Line too long (116 > 100)
  --> old_leetcode/leetcode_101_SymmetricTree.py:26:101
   |
24 |         testcases = [
25 |             TestData(name="case 0", root=TreeNode(val=3, left=TreeNode(9),
26 |                                                   right=TreeNode(val=20, left=TreeNode(val=15), right=TreeNode(7))),
   |                                                                                                     ^^^^^^^^^^^^^^^^
27 |                      expected=False),
28 |             TestData(name="case 1",
   |

PT009 Use a regular `assert` instead of unittest-style `assertEqual`
  --> old_leetcode/leetcode_101_SymmetricTree.py:35:13
   |
33 |         for case in testcases:
34 |             actual = Solution.is_symmetric(root=case.root)
35 |             self.assertEqual(
   |             ^^^^^^^^^^^^^^^^
36 |                 case.expected,
37 |                 actual,
   |
help: Replace `assertEqual(...)` with `assert ...`

E501 Line too long (116 > 100)
  --> old_leetcode/leetcode_102_LevelOrderTraversal.py:24:101
   |
22 |         testcases = [
23 |             TestData(name="case 0", root=TreeNode(val=3, left=TreeNode(9),
24 |                                                   right=TreeNode(val=20, left=TreeNode(val=15), right=TreeNode(7))),
   |                                                                                                     ^^^^^^^^^^^^^^^^
25 |                      expected=[[3], [9, 20], [15, 7]]),
26 |             TestData(name="case 1", root=None, expected=[])
   |

PT009 Use a regular `assert` instead of unittest-style `assertListEqual`
  --> old_leetcode/leetcode_102_LevelOrderTraversal.py:30:13
   |
28 |         for case in testcases:
29 |             actual = Solution.level_order_traversal(root=case.root)
30 |             self.assertListEqual(
   |             ^^^^^^^^^^^^^^^^^^^^
31 |                 case.expected,
32 |                 actual,
   |
help: Replace `assertListEqual(...)` with `assert ...`

B007 Loop control variable `i` not used within loop body
  --> old_leetcode/leetcode_102_LevelOrderTraversal.py:46:17
   |
44 |         current_level = []
45 |         while queue:
46 |             for i in range(len(queue)):
   |                 ^
47 |                 elem = queue.popleft()
48 |                 current_level.append(elem.val)
   |
help: Rename unused `i` to `_i`

E501 Line too long (116 > 100)
  --> old_leetcode/leetcode_104_MaximumDepth.py:26:101
   |
24 |         testcases = [
25 |             TestData(name="case 0", root=TreeNode(val=3, left=TreeNode(9),
26 |                                                   right=TreeNode(val=20, left=TreeNode(val=15), right=TreeNode(7))),
   |                                                                                                     ^^^^^^^^^^^^^^^^
27 |                      expected=3),
28 |             TestData(name="case 1", root=None, expected=0)
   |

PT009 Use a regular `assert` instead of unittest-style `assertEqual`
  --> old_leetcode/leetcode_104_MaximumDepth.py:34:13
   |
32 |             sol = Solution()
33 |             actual = sol.maxDepth(root=case.root)
34 |             self.assertEqual(
   |             ^^^^^^^^^^^^^^^^
35 |                 case.expected,
36 |                 actual,
   |
help: Replace `assertEqual(...)` with `assert ...`

PT009 Use a regular `assert` instead of unittest-style `assertEqual`
  --> old_leetcode/leetcode_104_MaximumDepth.py:42:13
   |
40 |         for case in testcases:
41 |             actual = sol.maxDepth_BFS(root=case.root)
42 |             self.assertEqual(
   |             ^^^^^^^^^^^^^^^^
43 |                 case.expected,
44 |                 actual,
   |
help: Replace `assertEqual(...)` with `assert ...`

PT009 Use a regular `assert` instead of unittest-style `assertEqual`
  --> old_leetcode/leetcode_112_PathSum.py:37:13
   |
35 |         for case in testcases:
36 |             actual = Solution.has_path_sum(root=case.root, targetSum=case.target)
37 |             self.assertEqual(
   |             ^^^^^^^^^^^^^^^^
38 |                 case.expected,
39 |                 actual,
   |
help: Replace `assertEqual(...)` with `assert ...`

PT009 Use a regular `assert` instead of unittest-style `assertEqual`
  --> old_leetcode/leetcode_112_PathSum.py:45:13
   |
43 |             solution = Solution()
44 |             actual = solution.has_path_sum_recursive(root=case.root, targetSum=case.target)
45 |             self.assertEqual(
   |             ^^^^^^^^^^^^^^^^
46 |                 case.expected,
47 |                 actual,
   |
help: Replace `assertEqual(...)` with `assert ...`

E501 Line too long (118 > 100)
  --> old_leetcode/leetcode_112_PathSum.py:78:101
   |
76 |         if targetSum == 0 and not (root.left or root.right):
77 |             return True
78 |         return self.has_path_sum_recursive(root.left, targetSum) or self.has_path_sum_recursive(root.right, targetSum)
   |                                                                                                     ^^^^^^^^^^^^^^^^^^
   |

E501 Line too long (116 > 100)
  --> old_leetcode/leetcode_113_PathSum_2.py:22:101
   |
20 |             TestData(name="case 1-2", root=TreeNode(val=1, left=TreeNode(2), right=TreeNode(3)),
21 |                      target=5, expected=[]),
22 |             TestData(name="full case", root=getTree([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, None, 5, 1]),
   |                                                                                                     ^^^^^^^^^^^^^^^^
23 |                      target=22, expected=[[5, 4, 11, 2], [5, 8, 4, 5]])
24 |         ]
   |

PT009 Use a regular `assert` instead of unittest-style `assertEqual`
  --> old_leetcode/leetcode_113_PathSum_2.py:28:13
   |
26 |             solution = Solution()
27 |             actual = solution.pathSum(root=case.root, targetSum=case.target)
28 |             self.assertEqual(
   |             ^^^^^^^^^^^^^^^^
29 |                 case.expected,
30 |                 actual,
   |
help: Replace `assertEqual(...)` with `assert ...`

E501 Line too long (123 > 100)
  --> old_leetcode/leetcode_144_PreOrderTraversal.py:22:101
   |
20 |     def test_3_sum(self):
21 |         testcases = [
22 |             TestData(name="case 0", root=TreeNode(val=1, right=TreeNode(val=2, left=TreeNode(val=3))), expected=[1, 2, 3]),
   |                                                                                                     ^^^^^^^^^^^^^^^^^^^^^^^
23 |             TestData(name="case 1", root=None, expected=[])
24 |         ]
   |

PT009 Use a regular `assert` instead of unittest-style `assertListEqual`
  --> old_leetcode/leetcode_144_PreOrderTraversal.py:27:13
   |
25 |         for case in testcases:
26 |             actual = Solution.preorder_traversal(root=case.root)
27 |             self.assertListEqual(
   |             ^^^^^^^^^^^^^^^^^^^^
28 |                 case.expected,
29 |                 actual,
   |
help: Replace `assertListEqual(...)` with `assert ...`

E501 Line too long (102 > 100)
  --> old_leetcode/leetcode_145_PostOrderTraversal.py:25:101
   |
23 |     def test_3_sum(self):
24 |         testcases = [
25 |             TestData(name="case 0", root=TreeNode(val=1, right=TreeNode(val=2, left=TreeNode(val=3))),
   |                                                                                                     ^^
26 |                      expected=[3, 2, 1]),
27 |             TestData(name="case 1", root=None, expected=[])
   |

PT009 Use a regular `assert` instead of unittest-style `assertListEqual`
  --> old_leetcode/leetcode_145_PostOrderTraversal.py:31:13
   |
29 |         for case in testcases:
30 |             actual = Solution.postorder_traversal(root=case.root)
31 |             self.assertListEqual(
   |             ^^^^^^^^^^^^^^^^^^^^
32 |                 case.expected,
33 |                 actual,
   |
help: Replace `assertListEqual(...)` with `assert ...`

PT009 Use a regular `assert` instead of unittest-style `assertListEqual`
  --> old_leetcode/leetcode_145_PostOrderTraversal.py:38:13
   |
36 |         for case in testcases:
37 |             actual = Solution.postorder_traversal_(root=case.root)
38 |             self.assertListEqual(
   |             ^^^^^^^^^^^^^^^^^^^^
39 |                 case.expected,
40 |                 actual,
   |
help: Replace `assertListEqual(...)` with `assert ...`

PT009 Use a regular `assert` instead of unittest-style `assertListEqual`
  --> old_leetcode/leetcode_145_PostOrderTraversal.py:45:13
   |
43 |         for case in testcases:
44 |             actual = Solution.postorder_traversal__(root=case.root)
45 |             self.assertListEqual(
   |             ^^^^^^^^^^^^^^^^^^^^
46 |                 case.expected,
47 |                 actual,
   |
help: Replace `assertListEqual(...)` with `assert ...`

PT009 Use a regular `assert` instead of unittest-style `assertListEqual`
  --> old_leetcode/leetcode_167_2Sum2.py:67:13
   |
65 |         for case in testcases:
66 |             actual = Solution.two_sum_sorted(case.numbers, case.target)
67 |             self.assertListEqual(
   |             ^^^^^^^^^^^^^^^^^^^^
68 |                 case.expected,
69 |                 actual,
   |
help: Replace `assertListEqual(...)` with `assert ...`

PT009 Use a regular `assert` instead of unittest-style `assertEqual`
  --> old_leetcode/leetcode_236_Lowest_Common_Ancestor.py:28:13
   |
26 |             solution = Solution()
27 |             actual = solution.lowestCommonAncestor(case.root, None, None)
28 |             self.assertEqual(
   |             ^^^^^^^^^^^^^^^^
29 |                 case.expected,
30 |                 actual,
   |
help: Replace `assertEqual(...)` with `assert ...`

E501 Line too long (103 > 100)
  --> old_leetcode/leetcode_236_Lowest_Common_Ancestor.py:37:101
   |
35 | class Solution:
36 |
37 |     def lca_recursive(self, root: TreeNode | None, p: TreeNode | None, q: TreeNode | None) -> TreeNode:
   |                                                                                                     ^^^
38 |         pass
   |

F841 Local variable `i` is assigned to but never used
  --> old_leetcode/leetcode_236_Lowest_Common_Ancestor.py:70:9
   |
68 |         print(right)
69 |         # find intersection
70 |         i = 0
   |         ^
71 |         return getTree([3])
72 |         # while i < min(len(left), len(right)):
   |
help: Remove assignment to unused variable `i`

PT009 Use a regular `assert` instead of unittest-style `assertEqual`
  --> old_leetcode/leetcode_392_IsSubsiquence.py:51:13
   |
49 |         for case in testcases:
50 |             actual = Solution.is_subsequence_for_loop(s=case.s, t=case.t)
51 |             self.assertEqual(
   |             ^^^^^^^^^^^^^^^^
52 |                 case.expected,
53 |                 actual,
   |
help: Replace `assertEqual(...)` with `assert ...`

SIM103 Return the condition `root.val == sum_to_match` directly
   --> old_leetcode/trees.py:142:9
    |
140 |           return False
141 |       if not root.left and not root.right:
142 | /         if root.val == sum_to_match:
143 | |             return True
144 | |         else:
145 | |             return False
    | |________________________^
146 |       return False
    |
help: Replace with `return root.val == sum_to_match`

SIM110 Use `return any(nums_sorted[i] == nums_sorted[i - 1] for i in range(1, len(nums_sorted)))` instead of `for` loop
  --> tasks/0217-contains-duplicate/solutions/sorting.py:9:9
   |
 7 |               return False
 8 |           nums_sorted = sorted(nums)
 9 | /         for i in range(1, len(nums_sorted)):
10 | |             if nums_sorted[i] == nums_sorted[i - 1]:
11 | |                 return True
12 | |         return False
   | |____________________^
   |
help: Replace with `return any(nums_sorted[i] == nums_sorted[i - 1] for i in range(1, len(nums_sorted)))`

Found 103 errors.
No fixes available (48 hidden fixes can be enabled with the `--unsafe-fixes` option).
