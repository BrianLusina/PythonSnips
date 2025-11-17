from abc import abstractmethod, ABC
from typing import List, Any
from .node import FibonacciHeapNode


class FibonacciHeap(ABC):
    def __init__(self):
        self.trees: List[FibonacciHeapNode] = []
        self.count = 0

    @abstractmethod
    def insert_node(self, value: Any):
        raise NotImplementedError("not yet implemented")

    @abstractmethod
    def consolidate(self):
        raise NotImplementedError("not yet implemented")
