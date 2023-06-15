from abc import ABC, abstractmethod
from typing import Any, List

from datastructures.trees.binary.tree import BinaryTreeNode


class HeapNode(BinaryTreeNode):
    """
    Represents a Heap node in a Heap datastructure. Heap nodes have either a left or right child so, they inherit from
    a Binary Tree Node which exhibit similar properties.
    """

    def __init__(self, data):
        super().__init__(data)

    @property
    def name(self):
        return self.__class__.__name__


class Heap(ABC):
    """
    Heap abstract class that contains methods for all types of heaps
    """

    def __init__(self):
        self.heap_dict = {}
        self.idx_of_element = {}

    @abstractmethod
    def insert_data(self, data: Any):
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


class ArrayBasedHeap(Heap):
    """
    Heap datastructure that uses an array as the underlying datastructure to build a heap.
    """

    def __init__(self):
        super().__init__()
        self.__data: List[Any] = []

    @property
    def root_node(self):
        """
        Retrieves the root node of the Heap
        :return:
        """
        if len(self.__data) == 0:
            raise Exception("Heap is empty")
        return self.__data[0]

    @property
    def last_node(self):
        """
        Returns the last node of the heap
        :return:
        """
        if len(self.__data) == 0:
            raise Exception("Heap is empty")
        return self.__data[len(self.__data) - 1]

    def insert_data(self, data: Any):
        """
        Inserts a value into the heap
        :param data: element to insert into the heap
        """
        raise NotImplementedError("not yet implemented")

    def __len__(self):
        return len(self.__data)
