from datastructures.linked_lists.doubly_linked_list import DoublyLinkedList
from .. import Queue, T
from ..exceptions import QueueFullException


class FifoDllQueue(Queue):
    """
    FifoQueue implementation in Python with a DoublyLinkedList as the underlying data structure.
    Methods:
        enqueue adds an item to the queue
        dequeue removes an item from the front of the queue
        size returns the size of the queue
        peek returns the element at the front of the queue, without removing it
        is_full checks if the queue is full
        is_empty checks if the queue is empty
    """

    def __init__(self, maxsize=0):
        super().__init__(maxsize)
        self.current_size = 0
        self.queue = DoublyLinkedList()

    def enqueue(self, data: T):
        """
        Adds item to the end of the queue
        """
        if self.is_full():
            raise QueueFullException(
                f"Queue has reached limit. Current Size: {self.size}. Capacity: {self.maxsize}"
            )
        self.current_size += 1
        self.queue.append(data)

    def dequeue(self) -> T:
        """
        Removes an item from the front of the queue.
        Returns None if the queue is empty
        """
        if self.is_empty():
            return None
        self.current_size -= 1
        item = self.queue.shift()
        return item

    @property
    def size(self) -> int:
        """
        Returns the size of the queue
        """
        return self.current_size

    def is_empty(self) -> bool:
        """
        Returns True if the queue is empty, false otherwise
        """
        if self.current_size == 0:
            return True
        return False

    def is_full(self) -> bool:
        """
        Returns True if the queue is full, false otherwise
        :return:
        """
        if self.maxsize == 0:
            # this is an unbounded queue, so, we return False
            return False
        return self.current_size == self.maxsize
