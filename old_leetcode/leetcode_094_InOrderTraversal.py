from dataclasses import dataclass
from unittest import TestCase


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


@dataclass
class TestData:
    name: str
    root: TreeNode | None
    expected: list[int]


class TestSolution(TestCase):
    def test_3_sum(self):
        testcases = [
            TestData(name="case 0", root=TreeNode(val=1, right=TreeNode(val=2, left=TreeNode(val=3))), expected=[1, 3, 2]),
            TestData(name="case 1", root=None, expected=[])
        ]
        for case in testcases:
            actual = Solution.inorder_traversal(root=case.root)
            self.assertListEqual(
                case.expected,
                actual,
                f"failed test {case.name} expected {case.expected}, actual {actual}"
            )


class Solution:
    @staticmethod
    def inorder_traversal(root: TreeNode | None) -> list[int]:
        output = []
        if root is None:
            return output
        stack = []
        curr = root
        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            output.append(curr.val)
            curr = curr.right
        return output
