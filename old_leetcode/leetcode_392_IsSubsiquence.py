from dataclasses import dataclass
from unittest import TestCase


@dataclass
class TestData:
    name: str
    s: str
    t: str
    expected: bool


# O (n) time; O(1) space
class Solution:

    @staticmethod
    def is_subsequence_for_loop(s: str, t: str):
        if not s:
            return True
        if not t:
            return False
        sIdx = 0
        sLen = len(s)
        for element in t:
            if sIdx == sLen:
                break
            if s[sIdx] == element:
                sIdx += 1
        return sIdx == sLen  # We have matched all elements in subsequence

    @staticmethod
    def is_subsequence_while_loop(s: str, t: str):
        sIdx = 0
        tIdx = 0
        while sIdx < len(s) and tIdx < len(t):
            if s[sIdx] == t[tIdx]:
                sIdx += 1
            tIdx += 1
        return sIdx == len(s)  # We have matched all elements in subsequence


class TestSolution(TestCase):
    def test_solution(self):
        testcases = [
            TestData(name="case 0", s="123", t="01772300", expected=True),
            TestData(name="case 0", s="123", t="01989898989", expected=False),
        ]
        for case in testcases:
            actual = Solution.is_subsequence_for_loop(s=case.s, t=case.t)
            assert case.expected == actual, f"failed test {case.name}"


# reuse 2 sum that it can return all pairs
