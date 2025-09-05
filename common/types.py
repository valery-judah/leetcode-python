from __future__ import annotations

from dataclasses import dataclass, field
from typing import Iterator, List

"""Common lightweight stubs for LeetCode-style types.

These are minimal implementations to support type annotations, simple
construction in examples, and basic debugging/printing. They are not
intended to be fully featured or optimized.
"""


@dataclass
class ListNode:
    val: int = 0
    next: ListNode | None = None

    def __iter__(self) -> Iterator[int]:
        node: ListNode | None = self
        while node is not None:
            yield node.val
            node = node.next

    def __repr__(self) -> str:  # pragma: no cover - convenience only
        return f"ListNode({list(self)})"


@dataclass
class RandomListNode:
    val: int = 0
    next: RandomListNode | None = None
    random: RandomListNode | None = None


@dataclass
class TreeNode:
    val: int = 0
    left: TreeNode | None = None
    right: TreeNode | None = None

    def __repr__(self) -> str:  # pragma: no cover - convenience only
        return f"TreeNode(val={self.val})"


@dataclass
class Node:
    val: int = 0
    children: List[Node] = field(default_factory=list)


@dataclass
class UndirectedGraphNode:
    val: int = 0
    neighbors: List[UndirectedGraphNode] = field(default_factory=list)


class NestedInteger:
    """A minimal NestedInteger stub matching common LeetCode interface.

    Can hold a single integer or a nested list of NestedInteger.
    """

    def __init__(self, value: int | None = None):
        self._int: int | None = value
        self._list: list[NestedInteger] | None = None if value is not None else []

    def isInteger(self) -> bool:
        return self._int is not None

    def add(self, elem: NestedInteger) -> None:
        if self._list is None:
            self._list = []
            if self._int is not None:
                # Convert current integer to list containing it
                self._list.append(NestedInteger(self._int))
                self._int = None
        self._list.append(elem)

    def setInteger(self, value: int) -> None:
        self._int = value
        self._list = None

    def getInteger(self) -> int | None:
        return self._int

    def getList(self) -> list[NestedInteger] | None:
        return self._list


__all__ = [
    "ListNode",
    "RandomListNode",
    "TreeNode",
    "Node",
    "UndirectedGraphNode",
    "NestedInteger",
]
