from __future__ import annotations

from typing import TYPE_CHECKING, Any

"""Centralized helpers for importing common typing stubs used in solutions.

- Primary API: import_common_types(*names) -> tuple[Any, ...]
  Returns the requested classes from common.types. If import fails, provides
  minimal stub classes with matching names so direct execution still works.
"""


def import_common_types(*names: str) -> tuple[Any, ...]:
    try:
        from . import types as _t

        mapping = {
            "ListNode": getattr(_t, "ListNode", None),
            "TreeNode": getattr(_t, "TreeNode", None),
            "Node": getattr(_t, "Node", None),
            "UndirectedGraphNode": getattr(_t, "UndirectedGraphNode", None),
            "RandomListNode": getattr(_t, "RandomListNode", None),
            "NestedInteger": getattr(_t, "NestedInteger", None),
        }
        out: list[Any] = []
        for nm in names:
            cls = mapping.get(nm)
            if cls is None:
                cls = type(nm, (), {"__init__": lambda self, *a, **k: None})  # pragma: no cover
            out.append(cls)
        return tuple(out)
    except Exception:  # pragma: no cover - last-resort stubs
        fallback_out: list[Any] = []
        for nm in names:
            fallback_out.append(type(nm, (), {"__init__": lambda self, *a, **k: None}))
        return tuple(fallback_out)


# Typed names for direct import in solutions: `from common.runtime_imports import ListNode, TreeNode, ...`
if TYPE_CHECKING:  # typing only
    from .types import (
        ListNode as ListNode,
    )
    from .types import (
        NestedInteger as NestedInteger,
    )
    from .types import (
        Node as Node,
    )
    from .types import (
        RandomListNode as RandomListNode,
    )
    from .types import (
        TreeNode as TreeNode,
    )
    from .types import (
        UndirectedGraphNode as UndirectedGraphNode,
    )
try:  # runtime binding
    from .types import (
        ListNode as ListNode,
    )
    from .types import (
        NestedInteger as NestedInteger,
    )
    from .types import (
        Node as Node,
    )
    from .types import (
        RandomListNode as RandomListNode,
    )
    from .types import (
        TreeNode as TreeNode,
    )
    from .types import (
        UndirectedGraphNode as UndirectedGraphNode,
    )
except Exception:  # pragma: no cover
    # Minimal stubs for direct execution if common.types is unavailable
    class ListNode:  # type: ignore[no-redef]
        def __init__(self, *args: Any, **kwargs: Any) -> None: ...

    class TreeNode:  # type: ignore[no-redef]
        def __init__(self, *args: Any, **kwargs: Any) -> None: ...

    class Node:  # type: ignore[no-redef]
        def __init__(self, *args: Any, **kwargs: Any) -> None: ...

    class UndirectedGraphNode:  # type: ignore[no-redef]
        def __init__(self, *args: Any, **kwargs: Any) -> None: ...

    class RandomListNode:  # type: ignore[no-redef]
        def __init__(self, *args: Any, **kwargs: Any) -> None: ...

    class NestedInteger:  # type: ignore[no-redef]
        def __init__(self, *args: Any, **kwargs: Any) -> None: ...
