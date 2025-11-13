from typing import Any, Optional

from datastructures.linked_lists import Node


class DoubleNode(Node):
    """
    Node implementation of DoubleLinkedList
    """

    def __init__(
        self,
        data: Any,
        previous: Optional["DoubleNode"] = None,
        next_: Optional["DoubleNode"] = None,
        key: Optional[Any] = None,
    ):
        super().__init__(data=data, next_=next_, key=key)
        self.previous = previous
        self.next = next_
