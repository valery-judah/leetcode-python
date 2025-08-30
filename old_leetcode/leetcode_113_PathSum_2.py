from dataclasses import dataclass
from unittest import TestCase

from src.utils.Trees import TreeNode, getTree


@dataclass
class TestData:
    name: str
    root: TreeNode | None
    target: int
    expected: list[list[int]]


class TestSolution(TestCase):
    def test(self):
        testcases = [
            TestData(
                name="case 1-2",
                root=getTree([3, 9, 20, None, None, 15, 7]),
                target=30,
                expected=[[3, 20, 7]],
            ),
            TestData(
                name="case 1-2",
                root=TreeNode(val=1, left=TreeNode(2), right=TreeNode(3)),
                target=5,
                expected=[],
            ),
            TestData(
                name="full case",
                root=getTree([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, None, 5, 1]),
                target=22,
                expected=[[5, 4, 11, 2], [5, 8, 4, 5]],
            ),
        ]
        for case in testcases:
            solution = Solution()
            actual = solution.pathSum(root=case.root, targetSum=case.target)
            assert case.expected == actual, f"failed test {case.name}"


class Solution:
    def pathSum__(self, root: TreeNode | None, targetSum: int) -> list[list[int]]:
        if not root:
            return []
        outputPaths = []
        stack: list[tuple[list[int], int, TreeNode | None]] = [([], targetSum, root)]
        while stack:
            currentPath, currentSum, node = stack.pop()
            if not node:
                continue
            else:
                path = currentPath.copy()
                path.append(node.val)
                if currentSum - node.val == 0 and not node.right and not node.left:
                    outputPaths.append(path)
                else:
                    stack.append((path, currentSum - node.val, node.right))
                    stack.append((path, currentSum - node.val, node.left))
        return outputPaths

    def pathSum(self, root: TreeNode | None, targetSum: int) -> list[list[int]]:
        if root is None:
            return []
        if root.left is None and root.right is None:
            if targetSum == root.val:
                return [[root.val]]
            else:
                return []
        ret = []
        for item in self.pathSum(root.left, targetSum - root.val):
            ret.append([root.val] + item)
        for item in self.pathSum(root.right, targetSum - root.val):
            ret.append([root.val] + item)
        return ret
