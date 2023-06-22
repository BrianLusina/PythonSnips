from typing import Optional
from datastructures.trees.binary.node import BinaryTreeNode, T


class AvlTreeNode(BinaryTreeNode):
    def __init__(self, data: T, left: Optional['AvlTreeNode'] = None, right: Optional['AvlTreeNode'] = None):
        super().__init__(data)
        self.left = left
        self.right = right
        self.height = 1

