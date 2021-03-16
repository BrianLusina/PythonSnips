from abc import ABC, abstractmethod

class TreeNode(object):
    """
    Tree node class which will implement Tree Node
    """

    def __init__(self, value):
        """
        Value here can be anything
        """
        self.value = value
        self.left = None
        self.right = None

class Tree(ABC):
    """
    Tree abstract base class that defines common methods & properties of a typical Tree data structure
    """
    
    @abstractmethod
    def increasing_order_traversal(self) -> TreeNode:
        """
        Rearranges the tree in in-order so that the leftmost node in the tree is now the root of the tree
        and every node has no left child and only one right child
        :returns root of tree of new tree
        """
        raise NotImplementedError("This method has not been implemented")

    @abstractmethod
    def get_depth(self) -> int:
        """
        Gets the depth of the tree or hight of the tree
        :returns height/depth of the tree
        """
        raise NotImplementedError("This method has not been implemented")

