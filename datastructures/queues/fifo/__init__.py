from queue import Empty, Full, Queue as Fifo
from .. import Queue, T
from ..exceptions import QueueFullException


class FifoQueue(Queue):
    """
    FifoQueue implementation in Python
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
        self.queue = Fifo(maxsize=maxsize)

    def enqueue(self, data: T):
        """
        Adds item to the end of the queue
        """
        try:
            self.queue.put(data, block=False)
        except Full:
            raise QueueFullException(
                f"Queue has reached limit. Current Size: {self.size}. Capacity: {self.maxsize}"
            )

    def dequeue(self) -> T:
        """
        Removes an item from the front of the queue.
        Returns None if the queue is empty
        """
        try:
            item = self.queue.get(block=False)
            return item
        except Empty:
            return None

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
        """
        Returns True if the queue is full, false otherwise
        :return:
        """
        return self.queue.full()
