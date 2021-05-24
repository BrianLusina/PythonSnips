from abc import abstractmethod, ABC
from typing import Any

from .. import TreeNode


class HeapNode(TreeNode):
    def __init__(self, data, name):
        super().__init__(data)
        self.name = name


class Heap(ABC):

    def __init__(self):
        self.heap_dict = {}
        self.idx_of_element = {}

    @abstractmethod
    def __getitem__(self, idx: int):
        raise NotImplementedError("Not yet implemented")

    @abstractmethod
    def __setitem__(self, idx: int, data):
        raise NotImplementedError("Not yet implemented")

    @abstractmethod
    def __bubble_up(self, idx: int):
        raise NotImplementedError("Not yet implemented")

    @abstractmethod
    def __bubble_down(self, idx: int):
        raise NotImplementedError("Not yet implemented")

    @abstractmethod
    def insert_data(self, data: Any):
        """
        Inserts a data value into the heap
        """
        raise NotImplementedError("Not yet implemented")

    @abstractmethod
    def insert_node(self, node: HeapNode):
        """
        Inserts a node into the heap
        """
        raise NotImplementedError("Not yet implemented")

    @staticmethod
    def get_parent_index(i: int) -> int:
        return (i - 1) // 2

    @staticmethod
    def get_left_child_index(i: int) -> int:
        return 2 * i + 1

    @staticmethod
    def get_right_child_index(i: int) -> int:
        return 2 * i + 2
