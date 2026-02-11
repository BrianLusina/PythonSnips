from abc import ABC, abstractmethod
from typing import Any, List, Optional


class Heap(ABC):
    """
    Heap abstract class that contains methods for all types of heaps
    """

    @abstractmethod
    def insert(self, data: Any):
        """
        Inserts a data value into the heap
        """
        raise NotImplementedError("Not yet implemented")

    @abstractmethod
    def peak(self) -> Optional[Any]:
        """
        Returns data at the top of the heap without removing it
        """
        raise NotImplementedError("Not yet implemented")

    @abstractmethod
    def delete(self) -> Any:
        """
        Deletes a node from the heap. This is typically the root node. This then performs operations to replace the
        deleted node with the appropriate node ensuring that the heap remains complete retaining the property of a heap.
        :return: The deleted node
        """
        raise NotImplementedError("Delete not yet implemented")

    @staticmethod
    def get_parent_index(i: int) -> int:
        return (i - 1) // 2

    @staticmethod
    def get_left_child_index(i: int) -> int:
        return 2 * i + 1

    @staticmethod
    def get_right_child_index(i: int) -> int:
        return 2 * i + 2


class ArrayBasedHeap(Heap):
    """
    Heap data structure that uses an array as the underlying data structure to build a heap.
    """

    def __init__(self, data: Optional[List[Any]] = None):
        super().__init__()
        if data is None:
            data = []
        self.heap: List[Any] = data

    def __len__(self):
        return len(self.heap)

    @property
    def root_node(self) -> Optional[Any]:
        """
        Retrieves the root node of the Heap
        """
        if len(self.heap) == 0:
            raise Exception("Heap is empty")
        return self.heap[0]

    def peak(self) -> Optional[Any]:
        """
        Retrieves the root node of the Heap
        """
        if len(self.heap) == 0:
            raise Exception("Heap is empty")
        return self.heap[0]

    @property
    def last_node(self):
        """
        Returns the last node of the heap
        :return:
        """
        if len(self.heap) == 0:
            raise Exception("Heap is empty")
        return self.heap[len(self.heap) - 1]

    def insert(self, data: Any):
        """
        Inserts a value into the heap
        :param data: element to insert into the heap
        """
        raise NotImplementedError("not yet implemented")

    def delete(self) -> Any:
        """
        Deletes an element from the heap and performs operations to ensure the heap remains complete.
        :return: deleted element to from the heap
        """
        raise NotImplementedError("not yet implemented")
