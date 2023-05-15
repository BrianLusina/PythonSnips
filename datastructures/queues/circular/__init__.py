from typing import Optional
from .. import Queue, T
from ..exceptions import QueueFullException, QueueEmptyException
from ...linked_lists.singly_linked_list import SingleNode


class CircularQueue(Queue):
    """
    CircularQueue implementation in Python using an Array or list as the underlying implementation. Methods remain similar to
    a normal queue.

    Complexity Analysis of Circular Queue Operations:
    Time Complexity:
        Enqueue: O(1) because no loop is involved for a single enqueue.
        Dequeue: O(1) because no loop is involved for one dequeue operation.
    Auxiliary Space: O(N) as the queue is of size N.
    """

    def __init__(self, maxsize: int):
        super().__init__(maxsize)
        self.queue = [None] * self.maxsize
        self.head = self.tail = -1

    def enqueue(self, data: T):
        if self.is_full():
            raise QueueFullException(
                f"Queue has reached limit. Current Size: {self.size}. Capacity: {self.maxsize}"
            )
        elif self.head == -1:
            self.head = 0
            self.tail = 0
            self.queue[self.tail] = data
        else:
            self.tail = (self.tail + 1) % self.maxsize
            self.queue[self.tail] = data

    def dequeue(self) -> T:
        if self.is_empty():
            raise QueueEmptyException("Queue is empty")
        elif self.head == self.tail:
            data = self.queue[self.head]
            self.head = -1
            self.tail = -1
            return data
        else:
            data = self.queue[self.head]
            self.head = (self.head + 1) % self.maxsize
            return data

    @property
    def size(self) -> int:
        return len(self.queue)

    def is_empty(self) -> bool:
        return self.head == -1

    def is_full(self) -> bool:
        return (self.tail + 1) % self.maxsize == self.head


class CircularLinkedListQueue(Queue):
    """
    Circular Linked List Queue implements a circular queue using a linked list as the underlying implementation.
    """

    def __init__(self, maxsize: int):
        super().__init__(maxsize)
        self.current_size = 0
        self.head: Optional[SingleNode] = None
        self.tail: Optional[SingleNode] = None

    def enqueue(self, data: T):
        if self.is_full():
            raise QueueFullException("Queue is full")

        node = SingleNode(data)

        if self.head is None:
            self.head = node
        else:
            self.tail.next = node

        self.tail = node
        self.tail.next = self.head
        self.current_size += 1

    def dequeue(self) -> T:
        if self.head is None:
            raise QueueEmptyException("queue is empty")

        # if there is no other element in the queue, i.e., we only have 1 element in the queue
        if self.head == self.tail:
            value = self.head.data
            self.head = None
            self.tail = None
        else:
            temp = self.head
            value = temp.data
            self.head = self.head.next
            self.tail.next = self.head
        self.current_size -= 1
        return value

    @property
    def size(self) -> int:
        if self.is_empty():
            return 0
        return self.current_size

    def is_empty(self) -> bool:
        return self.current_size == 0

    def is_full(self) -> bool:
        return self.current_size == self.maxsize
