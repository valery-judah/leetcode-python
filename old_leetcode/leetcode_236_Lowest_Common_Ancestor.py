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
        testcases = [
            TestData(name="case 1-1", root=getTree([3, 9, 20, None, None, 15, 7]),
                     p=getTree([5]), q=getTree([1]), expected=getTree([3]))
            # TestData(name="case 1-1", root=getTree([1, 9, 20, None, None, 15, 7]),
            #          p=getTree([1]), q=getTree([2]), expected=getTree([1]))
        ]

        for case in testcases:
            solution = Solution()
            actual = solution.lowestCommonAncestor(case.root, None, None)
            self.assertEqual(
                case.expected,
                actual,
                f"failed test {case.name} expected {case.expected}, actual {actual}"
            )


class Solution:

    def lca_recursive(self, root: TreeNode | None, p: TreeNode | None, q: TreeNode | None) -> TreeNode:
        pass

    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if root in (None, p, q):
            return root

        stack: list[tuple[TreeNode, list[int]]] = [(root, [])]  # todo add type
        out = []

        left = []
        right = [] 
        while stack:
            curr, path = stack.pop()
            print(f"curr: {curr}, path: {path}")
            out.append(curr.val)

            cpy = path.copy()
            cpy.append(curr.val)

            if curr.val == p.val:
                left = cpy
            if curr.val == q.val:
                right = cpy

            if curr.right:
                stack.append((curr.right, cpy))
            if curr.left:
                stack.append((curr.left, cpy))

        print(left)
        print(right)
        # find intersection
        i = 0
        return getTree([3])
        # while i < min(len(left), len(right)):
        #     if left[i] == right[i]:
        #         return getTree([left[i - 1]])
