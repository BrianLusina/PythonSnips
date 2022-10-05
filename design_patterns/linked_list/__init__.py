from typing import Optional


class Node:
    def __init__(self, data, next_=None):
        self.data = data
        self.next = next_


class LinkedList:

    def __init__(self):
        self.head: Optional[Node] = None

    def __len__(self):
        size = 0
        current = self.head
        while current:
            size += 1
            current = current.next
        return size

    def get(self, index: int) -> int:
        if index < 0:
            return -1
        size = len(self)
        if size < index + 1:
            return -1
        previous = None
        current = self.head
        for _ in range(index + 1):
            previous = current
            current = current.next
        return previous.data

    def addAtHead(self, val: int) -> None:
        node = Node(val)
        if not self.head:
            self.head = node
        else:
            node.next = self.head
            self.head = node

    def addAtTail(self, val: int) -> None:
        node = Node(val)

        if not self.head:
            self.head = node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = node

    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0:
            return
        size = len(self)
        if index < 0 or index > size:
            return
        if index == 0:
            self.addAtHead(val)
        else:
            node = Node(val)
            current = self.head

            for _ in range(index - 1):
                current = current.next

            node.next = current.next
            current.next = node

    def deleteAtIndex(self, index: int) -> None:
        size = len(self)
        if size < index + 1:
            return

        current = self.head
        previous = None

        for _ in range(index):
            previous = current
            current = current.next

        if previous:
            if current.next:
                previous.next = current.next
            else:
                previous.next = None
                current = None
        else:
            self.head = current.next
