from typing import Optional, Self, Any
from datastructures.linked_lists import Node, T


class CircularNode(Node):
    """
    CircularNode implementation in a circular linked list
    """

    def __init__(
        self, value: T, next_: Optional[Self] = None, key: Optional[Any] = None
    ):
        super().__init__(value, next_, key)
