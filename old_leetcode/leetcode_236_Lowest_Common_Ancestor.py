from dataclasses import dataclass
from unittest import TestCase

from src.utils.Trees import TreeNode, getTree


@dataclass
class TestData:
    name: str
    root: TreeNode
    p: TreeNode
    q: TreeNode
    expected: TreeNode


class TestSolution(TestCase):
    def test(self):
        root = getTree([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4])
        p = root.left  # 5
        q = root.right  # 1
        expected = root  # 3

        solution = Solution()
        actual = solution.lowestCommonAncestor(root, p, q)
        assert expected == actual


class Solution:
    def lowestCommonAncestor(self, root: "TreeNode", p: "TreeNode", q: "TreeNode") -> "TreeNode":
        if not root or root in (p, q):
            return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if left and right:
            return root
        return left or right
