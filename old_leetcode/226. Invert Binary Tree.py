# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return f"({self.left}<-{self.val}->{self.right})"


def test(f):
    tree = TreeNode(4, TreeNode(2), TreeNode(1))
    print(f(tree))


@test
def invertTree(root: Optional[TreeNode]) -> Optional[TreeNode]:
    def helper(root):
        if not root:
            return None
        root.left, root.right = root.right, root.left
        helper(root.left)
        helper(root.right)

    helper(root)
    return root
