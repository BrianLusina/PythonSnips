from typing import Optional, Any, List
from datastructures.trees.heaps.fibonacci.fibonacci_heap import FibonacciHeap
from datastructures.trees.heaps.fibonacci.node import FibonacciHeapNode
from datastructures.trees.heaps.fibonacci.utils import floor_log


class FibonacciMaxHeap(FibonacciHeap):
    def __init__(self):
        super().__init__()
        self.max: Optional[FibonacciHeapNode] = None

    def insert_node(self, value):
        new_tree = FibonacciHeapNode(value)
        self.trees.append(new_tree)
        if self.max is None or value > self.max.data:
            self.max = new_tree
        self.count = self.count + 1

    def get_max(self) -> Optional[Any]:
        if self.max is None:
            return None
        return self.max.data

    def extract_max(self) -> Optional[Any]:
        largest = self.max
        if largest is not None:
            for child in largest.children:
                self.trees.append(child)
            self.trees.remove(largest)
            if not self.trees:
                self.trees = None
            else:
                self.max = self.trees[0]
                self.consolidate()
            self.count = self.count - 1
            return largest.data

    def consolidate(self):
        aux: List[Optional[FibonacciHeapNode]] = (floor_log(self.count) + 1) * [None]

        while self.trees:
            x = self.trees[0]
            order = x.order
            self.trees.remove(x)

            while aux[order] is not None:
                y = aux[order]
                if x.data < y.data:
                    x, y = y, x
                x.add_at_end(y)
                aux[order] = None
                order = order + 1
            aux[order] = x

        self.max = None
        for k in aux:
            if k is not None:
                self.trees.append(k)
                if self.max is None or k.data > self.max.data:
                    self.max = k
