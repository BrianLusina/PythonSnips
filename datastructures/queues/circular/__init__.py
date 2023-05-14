from .. import Queue, T
from ..exceptions import QueueFullException, QueueEmptyException


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
