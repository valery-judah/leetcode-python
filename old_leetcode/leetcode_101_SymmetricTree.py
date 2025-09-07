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
    root: TreeNode | None
    expected: bool


class TestSolution(TestCase):
    def test(self):
        testcases = [
            TestData(
                name="case 0",
                root=TreeNode(
                    val=3,
                    left=TreeNode(9),
                    right=TreeNode(val=20, left=TreeNode(val=15), right=TreeNode(7)),
                ),
                expected=False,
            ),
            TestData(
                name="case 1",
                root=TreeNode(
                    1,
                    left=TreeNode(2, left=TreeNode(3), right=TreeNode(4)),
                    right=TreeNode(2, left=TreeNode(4), right=TreeNode(3)),
                ),
                expected=True,
            ),
        ]
        for case in testcases:
            actual = Solution.is_symmetric(root=case.root)
            assert case.expected == actual, f"failed test {case.name}"


class Solution:
    @staticmethod
    def is_symmetric(root: TreeNode | None) -> bool:
        nodes = [root, root]
        while nodes:
            left = nodes.pop()
            right = nodes.pop()
            print(f"[{left},{right}]")
            if not left and not right:
                continue
            if not left or not right:
                return False
            if left.val != right.val:
                return False
            nodes.append(left.right)
            nodes.append(right.left)
            nodes.append(left.left)
            nodes.append(right.right)
        return True
