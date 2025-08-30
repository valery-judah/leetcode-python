from collections import deque
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
    expected: list[list[int]]


class TestSolution(TestCase):
    def test_3_sum(self):
        testcases = [
            TestData(
                name="case 0",
                root=TreeNode(
                    val=3,
                    left=TreeNode(9),
                    right=TreeNode(val=20, left=TreeNode(val=15), right=TreeNode(7)),
                ),
                expected=[[3], [9, 20], [15, 7]],
            ),
            TestData(name="case 1", root=None, expected=[]),
        ]
        for case in testcases:
            actual = Solution.level_order_traversal(root=case.root)
            self.assertListEqual(
                case.expected,
                actual,
                f"failed test {case.name} expected {case.expected}, actual {actual}",
            )


class Solution:
    @staticmethod
    def level_order_traversal(root: TreeNode | None) -> list[list[int]]:
        levels = []
        if root is None:
            return levels
        queue = deque(
            [
                root,
            ]
        )
        current_level = []
        while queue:
            for i in range(len(queue)):
                elem = queue.popleft()
                current_level.append(elem.val)
                left = elem.left
                right = elem.right
                if left:
                    queue.append(left)
                if right:
                    queue.append(right)
            levels.append(current_level.copy())
            current_level.clear()
        return levels
