from abc import ABC, abstractmethod
from typing import Any


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

