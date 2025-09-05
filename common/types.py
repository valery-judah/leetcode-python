from __future__ import annotations

"""Common lightweight stubs for LeetCode-style types.

These are minimal implementations to support type annotations, simple
construction in examples, and basic debugging/printing. They are not
intended to be fully featured or optimized.
"""

from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class ListNode:
    val: int = 0
    next: Optional["ListNode"] = None

    def __iter__(self):
        node = self
        while node is not None:
            yield node.val
            node = node.next

    def __repr__(self) -> str:  # pragma: no cover - convenience only
        return f"ListNode({list(self)})"


@dataclass
class RandomListNode:
    val: int = 0
    next: Optional["RandomListNode"] = None
    random: Optional["RandomListNode"] = None


@dataclass
class TreeNode:
    val: int = 0
    left: Optional["TreeNode"] = None
    right: Optional["TreeNode"] = None

    def __repr__(self) -> str:  # pragma: no cover - convenience only
        return f"TreeNode(val={self.val})"


@dataclass
class Node:
    val: int = 0
    children: List["Node"] = field(default_factory=list)


@dataclass
class UndirectedGraphNode:
    val: int = 0
    neighbors: List["UndirectedGraphNode"] = field(default_factory=list)


class NestedInteger:
    """A minimal NestedInteger stub matching common LeetCode interface.

    Can hold a single integer or a nested list of NestedInteger.
    """

    def __init__(self, value: int | None = None):
        self._int: Optional[int] = value
        self._list: Optional[list[NestedInteger]] = None if value is not None else []

    def isInteger(self) -> bool:
        return self._int is not None

    def add(self, elem: "NestedInteger") -> None:
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

    def getInteger(self) -> Optional[int]:
        return self._int

    def getList(self) -> Optional[list["NestedInteger"]]:
        return self._list


__all__ = [
    "ListNode",
    "RandomListNode",
    "TreeNode",
    "Node",
    "UndirectedGraphNode",
    "NestedInteger",
]

