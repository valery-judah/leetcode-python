from dataclasses import dataclass
from unittest import TestCase


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self) -> str:
        return f"{self.val}: {self.left},{self.right}"


@dataclass
class TestData:
    name: str
    root: TreeNode | None
    expected: list[int]


class TestSolution(TestCase):
    def test_3_sum(self):
        testcases = [
            TestData(
                name="case 0",
                root=TreeNode(val=1, right=TreeNode(val=2, left=TreeNode(val=3))),
                expected=[3, 2, 1],
            ),
            TestData(name="case 1", root=None, expected=[]),
        ]
        for case in testcases:
            actual = Solution.postorder_traversal(root=case.root)
            self.assertListEqual(
                case.expected,
                actual,
                f"failed test {case.name} expected {case.expected}, actual {actual}",
            )
        for case in testcases:
            actual = Solution.postorder_traversal_(root=case.root)
            self.assertListEqual(
                case.expected,
                actual,
                f"failed test {case.name} expected {case.expected}, actual {actual}",
            )
        for case in testcases:
            actual = Solution.postorder_traversal__(root=case.root)
            self.assertListEqual(
                case.expected,
                actual,
                f"failed test {case.name} expected {case.expected}, actual {actual}",
            )


class Solution:
    @staticmethod
    def postorder_traversal(root: TreeNode | None) -> list[int]:
        output = []
        if root is None:
            return output
        visited: list[TreeNode] = []
        s = [root]
        while s:
            curr = s[-1]
            if len(visited) > 0 and visited[-1] == curr:
                output.append(curr.val)
                visited.pop()
                s.pop()
            else:
                visited.append(curr)
                if curr.right:
                    s.append(curr.right)
                if curr.left:
                    s.append(curr.left)
        return output

    @staticmethod
    def postorder_traversal_(root: TreeNode | None) -> list[int]:
        output = []
        if root is None:
            return output
        curr: TreeNode = root
        stack = []
        while stack or curr:
            if curr:
                stack.append(curr)
                output.insert(0, curr.val)
                curr = curr.right
            else:
                curr = stack.pop().left
        return output

    @staticmethod
    def postorder_traversal__(root: TreeNode | None) -> list[int]:
        output = []
        if root is None:
            return output
        stack = [root]
        while stack:
            curr = stack.pop()
            output.insert(0, curr.val)
            if curr.left:
                stack.append(curr.left)
            if curr.right:
                stack.append(curr.right)
        return output
