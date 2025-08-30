from collections import deque
from typing import Optional, List
from dataclasses import dataclass
from unittest import TestCase


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self) -> str:
        return f"(val: {self.val})"


@dataclass
class TestData:
    name: str
    root: Optional[TreeNode]
    expected: int


class TestSolution(TestCase):
    def test(self):
        testcases = [
            TestData(name="case 0", root=TreeNode(val=3, left=TreeNode(9),
                                                  right=TreeNode(val=20, left=TreeNode(val=15), right=TreeNode(7))),
                     expected=3),
            TestData(name="case 1", root=None, expected=0)
        ]

        for case in testcases:
            sol = Solution()
            actual = sol.maxDepth(root=case.root)
            self.assertEqual(
                case.expected,
                actual,
                "failed test {} expected {}, actual {}".format(
                    case.name, case.expected, actual
                )
            )

        for case in testcases:
            actual = sol.maxDepth_BFS(root=case.root)
            self.assertEqual(
                case.expected,
                actual,
                "failed test {} expected {}, actual {}".format(
                    case.name, case.expected, actual
                )
            )


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        else:
            left_max_height = self.maxDepth(root.left)
            right_max_height = self.maxDepth(root.right)
        return max(left_max_height, right_max_height) + 1

    def maxDepth_BFS(self, root: Optional[TreeNode]) -> int:
        depth = 0
        stack = []
        if root:
            stack.append((1, root))
        while stack:
            current_depth, node = stack.pop()
            if node:
                depth = max(depth, current_depth)
                stack.append((current_depth + 1, node.left))
                stack.append((current_depth + 1, node.right))
        return depth
