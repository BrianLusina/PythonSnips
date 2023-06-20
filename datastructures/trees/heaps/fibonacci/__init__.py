from abc import abstractmethod, ABC
from typing import List, Any
from .. import HeapNode


class FibonacciHeapNode(HeapNode):
    def __init__(self, data):
        super().__init__(data)
        self.children: List[FibonacciHeapNode] = []
        self.order = 0

    def add_at_end(self, t: 'FibonacciHeapNode'):
        self.children.append(t)
        self.order = self.order + 1


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
