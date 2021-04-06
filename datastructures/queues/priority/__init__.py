from queue import PriorityQueue as Pq, Empty, Full
from typing import Any, Union, NoReturn, List, Optional


class QueueFullException(Full):
    pass


class PriorityQueue(object):
    """
    Queue implementation in Python
    Methods:
        enqueue adds an item to the queue
        dequeue removes an item from the front of the queue
        size returns the size of the queue
        peek returns the element at the front of the queue, without removing it
        is_full checks if the queue is full
        is_empty checks if the queue is empty
    """

    def __init__(self, size=0):
        self.queue = Pq(maxsize=size)
        self.data = []

    @property
    def size(self) -> int:
        """
        Returns the size of the queue
        """
        return self.queue.qsize()

    def is_empty(self) -> bool:
        """
        Returns True if the queue is empty, false otherwise
        """
        return self.queue.empty()

    def is_full(self) -> bool:
        return self.queue.full()

    @property
    def items(self) -> List:
        return self.data

    def add(self, data: Any) -> NoReturn:
        """
        Adds item to the end of the queue
        """
        try:
            self.queue.put(data, block=False)
            self.data.append(data)
        except Full:
            raise QueueFullException(
                f"Queue has reached limit. Current Size: {self.size}. Capacity: {self.queue.maxsize}")

    def peek(self) -> Optional[Any]:
        return self.data[0]

    def poll(self, block: bool = False) -> Optional[Any]:
        try:
            self.data.pop()
            return self.queue.get(block=block)
        except Empty:
            return None

    def dequeue(self, block: bool = False) -> Union[Any, None]:
        """
        Removes an item from the front of the queue.
        Returns None if the queue is empty
        """
        try:
            self.data.pop()
            return self.queue.get(block=block)
        except Empty:
            return None

    def __repr__(self):
        return f"Size: {self.size}. Queue: {self.items}"
