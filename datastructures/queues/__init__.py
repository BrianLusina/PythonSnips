from abc import abstractmethod, ABC
from typing import TypeVar

T = TypeVar("T")


class Queue(ABC):
    """
    Fifo Queue implementation in Python
    Methods:
        enqueue adds an item to the queue
        dequeue removes an item from the front of the queue
        size returns the size of the queue
        peek returns the element at the front of the queue, without removing it
        is_full checks if the queue is full
        is_empty checks if the queue is empty
    """

    def __init__(self, maxsize=0):
        """
        Creates an instance of a Queue
        :param maxsize: Maximum size of queue. Defaults to 0. If set to 0, this will create an infinite queue.
        """
        if maxsize < 0:
            raise ValueError("Maximum size can not be less than 0")
        self.maxsize = maxsize

    @property
    @abstractmethod
    def size(self) -> int:
        """
        Returns the current size of the queue
        """
        raise NotImplementedError("Not implemented")

    @abstractmethod
    def is_empty(self) -> bool:
        """
        Returns True if the queue is empty, false otherwise
        """
        raise NotImplementedError("Not yet implemented")

    @abstractmethod
    def is_full(self) -> bool:
        """
        Returns True if the queue is full, false otherwise
        """
        raise NotImplementedError("Not yet implemented")

    @abstractmethod
    def enqueue(self, data: T):
        """
        Adds item to the end of the queue
        """
        raise NotImplementedError("Not yet implemented")

    @abstractmethod
    def dequeue(self) -> T:
        """
        Removes an item from the front of the queue.
        Returns None if the queue is empty
        """
        raise NotImplementedError("Not yet implemented")

    def __len__(self):
        return self.size
