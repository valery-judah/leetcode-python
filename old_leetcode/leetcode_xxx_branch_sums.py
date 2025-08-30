
from src.utils.Trees import TreeNode, getTree


def getPathSumsHelper(root: TreeNode, pathSums: list[int], runningSum):
    if not root:
        return

    nextSum = runningSum + root.val
    if not (root.right or root.left):  # leaf node
        pathSums.append(nextSum)

    getPathSumsHelper(root.left, pathSums, nextSum)
    getPathSumsHelper(root.right, pathSums, nextSum)

    return


def getPathSums(root: TreeNode | None) -> list[int]:
    sums = []
    getPathSumsHelper(root, sums, 0)
    return sums


if __name__ == "__main__":
    expected = [18, 20, 47, 52]
    tree = getTree([10, 5, 15, 2, 5, 13, 22, 1, None, None, None, None, 14, None, None])
    print(getPathSums(root=tree))
    print(expected == getPathSums(root=tree))
