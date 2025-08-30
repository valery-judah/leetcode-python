# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from src.utils.Trees import TreeNode, getTree


def test(f):
    tree = getTree([6, 2, 8, 1, 4, 7, 9, None, None, 3, 5, None, None])
    print(tree)


@test
def lowestCommonAncestor(root: "TreeNode", p: "TreeNode", q: "TreeNode") -> "TreeNode":
    pass
