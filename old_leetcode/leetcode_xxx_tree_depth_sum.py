from src.utils.Trees import TreeNode, getTree

# todo understand


def helper(root: TreeNode, nodeDepth):
    if not root:
        return 0
    return nodeDepth + helper(root.left, nodeDepth + 1) + helper(root.right, nodeDepth + 1)


def getDepthsSum(root: TreeNode | None):
    return helper(root, 0)


def getDepthsSum_iterative(root):
    depthSum = 0
    stack = [(root, 0)]
    while stack:
        node, depth = stack.pop()
        if not node:
            continue
        depthSum += depth
        stack.append((node.left, depth + 1))
        stack.append((node.right, depth + 1))
    return depthSum


if __name__ == "__main__":
    expected = 16
    tree = getTree([10, 5, 15, 2, 5, 13, 22, 1, None, None, None, None, 14, None, None])
    print(getDepthsSum_iterative(root=tree))
