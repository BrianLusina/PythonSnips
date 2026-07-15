from typing import Dict, Optional, Any
from datastructures.linked_lists.doubly_linked_list.node import DoubleNode


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.lookup: Dict[str | int, DoubleNode] = {}
        self.size = 0
        # Using sentinel head and tail nodes avoids null checks when adding/removing nodes at boundaries. This means
        # every real node always has non-null prev/next pointers, simplifying insertion and deletion logic dramatically
        self.head = DoubleNode(0)
        self.tail = DoubleNode(0)
        self.head.next = self.tail
        self.tail.previous = self.head

    @staticmethod
    def __delete_node(node: DoubleNode):
        node.previous.next = node.next
        node.next.previous = node.previous

    def __add_to_head(self, node: DoubleNode):
        node.next = self.head.next
        node.next.previous = node
        node.previous = self.head
        self.head.next = node

    def get(self, key: str | int) -> Optional[Any]:
        if key in self.lookup:
            node = self.lookup[key]
            data = node.data
            self.__delete_node(node)
            self.__add_to_head(node)
            return data
        return None

    def put(self, key: str | int, value: int) -> None:
        if key in self.lookup:
            node = self.lookup[key]
            node.data = value
            self.__delete_node(node)
            self.__add_to_head(node)
        else:
            node = DoubleNode(key=key, data=value)
            self.lookup[key] = node
            if self.size < self.capacity:
                self.size += 1
                self.__add_to_head(node)
            else:
                del self.lookup[self.tail.previous.key]
                self.__delete_node(self.tail.previous)
                self.__add_to_head(node)
