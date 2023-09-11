from typing import Optional, Any, List
from .. import FibonacciHeap
from ..node import FibonacciHeapNode
from ..utils import floor_log


class FibonacciMinHeap(FibonacciHeap):
    def __init__(self):
        super().__init__()
        self.least: Optional[FibonacciHeapNode] = None

    def insert_node(self, value):
        new_tree = FibonacciHeapNode(value)
        self.trees.append(new_tree)
        if self.least is None or value < self.least.data:
            self.least = new_tree
        self.count = self.count + 1

    def get_min(self) -> Optional[Any]:
        if self.least is None:
            return None
        return self.least.data

    def extract_min(self) -> Optional[Any]:
        smallest = self.least
        if smallest is not None:
            for child in smallest.children:
                self.trees.append(child)
            self.trees.remove(smallest)
            if not self.trees:
                self.trees = None
            else:
                self.least = self.trees[0]
                self.consolidate()
            self.count = self.count - 1
            return smallest.data

    def consolidate(self):
        aux: List[Optional[FibonacciHeapNode]] = (floor_log(self.count) + 1) * [None]

        while self.trees:
            x = self.trees[0]
            order = x.order
            self.trees.remove(x)

            while aux[order] is not None:
                y = aux[order]
                if x.data > y.data:
                    x, y = y, x
                x.add_at_end(y)
                aux[order] = None
                order = order + 1
            aux[order] = x

        self.least = None
        for k in aux:
            if k is not None:
                self.trees.append(k)
                if self.least is None or k.data < self.least.data:
                    self.least = k
