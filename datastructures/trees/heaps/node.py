from typing import Optional
from datastructures.trees.binary.tree import BinaryTreeNode, T


class HeapNode(BinaryTreeNode):
    """
    Represents a Heap node in a Heap datastructure. Heap nodes have either a left or right child so, they inherit from
    a Binary Tree Node which exhibit similar properties.
    """

    def __init__(self, data: T, key: Optional[T] = None):
        super().__init__(data)
        self.key = key

    @property
    def name(self):
        return self.__class__.__name__

    def __eq__(self, other: 'HeapNode') -> bool:
        return self.data == other.data

    def __lt__(self, other: 'HeapNode') -> bool:
        return self.data < other.data

    def __gt__(self, other: 'HeapNode') -> bool:
        return self.data > other.data

    def __le__(self, other: 'HeapNode') -> bool:
        return self.data <= other.data

    def __ge__(self, other: 'HeapNode') -> bool:
        return self.data >= other.data

    def __ne__(self, other: 'HeapNode') -> bool:
        return self.data != other.data

    def __hash__(self) -> int:
        return hash(self.data)
