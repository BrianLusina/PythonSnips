from abc import ABCMeta
from typing import Any, List
from datastructures.trees.heaps.heap import Heap


class ArrayBasedHeap(Heap, metaclass=ABCMeta):
    """
    Heap data structure that uses an array as the underlying data structure to build a heap.
    """

    def __init__(self):
        super().__init__()
        self.data: List[Any] = []

    def __len__(self):
        return len(self.data)

    @property
    def root_node(self):
        """
        Retrieves the root node of the Heap
        :return:
        """
        if len(self.data) == 0:
            raise Exception("Heap is empty")
        return self.data[0]

    @property
    def last_node(self):
        """
        Returns the last node of the heap
        :return:
        """
        if len(self.data) == 0:
            raise Exception("Heap is empty")
        return self.data[len(self.data) - 1]
