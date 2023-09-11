from datastructures.trees.binary.tree import BinaryTreeNode, T


class HeapNode(BinaryTreeNode):
    """
    Represents a Heap node in a Heap datastructure. Heap nodes have either a left or right child so, they inherit from
    a Binary Tree Node which exhibit similar properties.
    """

    def __init__(self, data: T, key: T):
        super().__init__(data)
        self.key = key

    @property
    def name(self):
        return self.__class__.__name__
