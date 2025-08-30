import collections
from collections import deque
from typing import List, Optional


class TreeNode:
    def __repr__(self) -> str:
        return f"({self.val}: {self.left}, {self.right})"

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def traverse_by_level_iterative0(root: Optional[TreeNode]) -> List[List[int]]:
    """OLD. Traverse by level in iterative manner version 0.1
    My version"""
    result = []
    queue = [root]

    # todo create & check invariant: all children of all nodes is on queue??
    # check for null or emptiness
    while len(queue) > 0:               # When there are no nodes to process in next level
        list_to_process = []
        while len(queue) > 0:
            list_to_process.append(queue.pop(0))
        # todo refactor to map
        sublist = []
        for node in list_to_process:
            if node is not None:
                sublist.append(node.val)
                if node.left is not None:
                    queue.append(node.left)
                if node.right is not None:
                    queue.append(node.right)
        result.append(sublist)
    return result


def traverse_by_level_iterative(root: Optional[TreeNode]) -> List[List[int]]:
    """Traverse in iterative manner version 0.2
    My version with functional features (list comprehensions)."""
    result = []
    if root is None:
        return result
    queue = [root]
    import itertools
    while queue:
        list_to_process = queue
        result.append([x.val for x in list_to_process])
        children = [[node.left, node.right] for node in list_to_process if node is not None]
        queue = [n for n in list(itertools.chain(*children)) if n is not None]
    return result


def traverse_by_level_iterative1(root: Optional[TreeNode]) -> List[List[int]]:
    """ in iterative manner version 0.3"""
    result = []
    if root is None:
        return result
    queue = deque()
    queue.append(root)
    while queue:
        level_size = len(queue)
        current_level = []
        for _ in range(level_size):
            node = queue.popleft()
            current_level.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        result.append(current_level)
    return result


def traverse_zig_zag(root: Optional[TreeNode]) -> List[List[int]]:
    """ Zig zag traversing based on version 0.3"""
    result = []
    if root is None:
        return result

    queue = deque()
    queue.append(root)
    reverse = False

    while queue:
        level_size = len(queue)
        current_level = collections.deque()
        for _ in range(level_size):
            node = queue.popleft()
            add_value(current_level, node, reverse)
            add_children(node, queue)
        reverse = not reverse
        result.append(list(current_level))
    return result


def add_children(node, queue):
    if node.left:
        queue.append(node.left)
    if node.right:
        queue.append(node.right)


def add_value(current_level, node, reverse):
    if reverse:
        current_level.appendleft(node.val)
    else:
        current_level.append(node.val)


def get_min_depth(root: Optional[TreeNode]) -> int:
    if root is None:
        return 0
    if not root.left and not root.right:
        return 1
    queue = deque()
    queue.append(root)
    nodes_number = 0
    while queue:
        nodes_number += 1
        level_size = len(queue)
        for _ in range(level_size):
            node = queue.popleft()
            if not (node.left and node.right):
                return nodes_number
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
    return nodes_number

###################################################################
# BFS


def has_path(root: Optional[TreeNode], sum_to_match: int):
    if root is None:
        return False
    if not root.left and not root.right:
        if root.val == sum_to_match:
            return True
        else:
            return False
    return False

