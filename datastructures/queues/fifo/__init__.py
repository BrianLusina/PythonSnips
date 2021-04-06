from queue import Queue, Empty, Full


class QueueFullException(Full):
    pass


class FifoQueue(object):
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
        self.queue = Queue(maxsize=size)
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

    @property
    def items(self) -> list:
        return self.data

    def enqueue(self, val):
        """
        Adds item to the end of the queue
        """
        try:
            self.queue.put(val, block=False)
            self.data.append(val)
        except Full:
            raise QueueFullException(
                f"Queue has reached limit. Current Size: {self.size}. Capacity: {self.queue.maxsize}")

    def dequeue(self):
        """
        Removes an item from the front of the queue.
        Returns None if the queue is empty
        """
        try:
            item = self.queue.get(block=False)
            self.data.pop(1)
            return item
        except Empty:
            return None

    def __repr__(self):
        return f"Size: {self.size}. Queue: {self.items}"
