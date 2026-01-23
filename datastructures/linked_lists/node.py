from typing import Any, Optional, Generic, TypeVar
from abc import ABCMeta
from datastructures.linked_lists.types import T


class Node(Generic[T]):
    """
    Node object in the Linked List
    """

    __metaclass__ = ABCMeta

    def __init__(
        self,
        data: Optional[T] = None,
        next_: Optional["Node[Generic[T]]"] = None,
        key: Any = None,
    ):
        self.data = data
        self.next = next_
        # if no key is provided, the hash of the data becomes the key
        self.key = key or hash(data)

    def __str__(self) -> str:
        return f"Node(data={self.data}, key={self.key})"

    def __repr__(self) -> str:
        return f"Node(data={self.data}, key={self.key})"

    def __eq__(self, other: "Node") -> bool:
        return self.key == other.key
