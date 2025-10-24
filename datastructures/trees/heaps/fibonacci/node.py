from typing import List
from ..node import HeapNode


class FibonacciHeapNode(HeapNode):
    def __init__(self, data, key):
        super().__init__(data, key)
        self.children: List[FibonacciHeapNode] = []
        self.order = 0

    def add_at_end(self, t: "FibonacciHeapNode"):
        self.children.append(t)
        self.order = self.order + 1
