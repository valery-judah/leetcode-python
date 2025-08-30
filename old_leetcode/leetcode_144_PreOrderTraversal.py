from typing import Optional, List
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
    root: Optional[TreeNode]
    expected: List[int]


class TestSolution(TestCase):
    def test_3_sum(self):
        testcases = [
            TestData(name="case 0", root=TreeNode(val=1, right=TreeNode(val=2, left=TreeNode(val=3))), expected=[1, 2, 3]),
            TestData(name="case 1", root=None, expected=[])
        ]
        for case in testcases:
            actual = Solution.preorder_traversal(root=case.root)
            self.assertListEqual(
                case.expected,
                actual,
                "failed test {} expected {}, actual {}".format(
                    case.name, case.expected, actual
                )
            )


class Solution:
    @staticmethod
    def preorder_traversal(root: Optional[TreeNode]) -> List[int]:
        nodes = []
        if root is None:
            return nodes
        stack = [root, ]
        while stack:
            root = stack.pop()
            nodes.append(root.val)
            if root.right:
                stack.append(root.right)
            if root.left:
                stack.append(root.left)
        return nodes
