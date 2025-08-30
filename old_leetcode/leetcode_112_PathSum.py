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
    target: int
    expected: bool


class TestSolution(TestCase):
    def test(self):
        testcases = [
            TestData(name="case 1-2", root=TreeNode(val=1, left=TreeNode(2)),
                     target=1, expected=False),
            TestData(name="case -2 -3", root=TreeNode(val=-2, right=TreeNode(-3)),
                     target=-5, expected=True),
            TestData(name="case 1",
                     root=TreeNode(1, left=TreeNode(2, left=TreeNode(3), right=TreeNode(4)),
                                   right=TreeNode(2, left=TreeNode(4), right=TreeNode(3))),
                     target=6, expected=True)
        ]
        for case in testcases:
            actual = Solution.has_path_sum(root=case.root, targetSum=case.target)
            self.assertEqual(
                case.expected,
                actual,
                f"failed test {case.name} expected {case.expected}, actual {actual}"
            )
        for case in testcases:
            solution = Solution()
            actual = solution.has_path_sum_recursive(root=case.root, targetSum=case.target)
            self.assertEqual(
                case.expected,
                actual,
                f"failed test {case.name} expected {case.expected}, actual {actual}"
            )


class Solution:
    @staticmethod
    def has_path_sum(root: TreeNode | None, targetSum: int) -> bool:
        print("------------------------------------------")
        if not root:
            return False
        stack = [(targetSum, root)]
        while stack:
            target, node = stack.pop()
            print(f"{target}, {node}")
            if node:
                left = node.left
                right = node.right
                if target - node.val == 0 and (not right and not left):
                    return True
                else:
                    stack.append((target - node.val, node.right))
                    stack.append((target - node.val, node.left))
        return False

    def has_path_sum_recursive(self, root: TreeNode | None, targetSum: int) -> bool:
        if not root:
            return False
        targetSum -= root.val
        if targetSum == 0 and not (root.left or root.right):
            return True
        return self.has_path_sum_recursive(root.left, targetSum) or self.has_path_sum_recursive(root.right, targetSum)
