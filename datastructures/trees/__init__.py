from abc import ABC, abstractmethod


class TreeNode(object):
    """
    Tree node class which will implement Tree Node
    """

    def __init__(self, value):
        """
        Value here can be anything
        """
        self.data = value
        self.left = None
        self.right = None


class Tree(ABC):
    """
    Tree abstract base class that defines common methods & properties of a typical Tree data structure
    """

    @abstractmethod
    def __len__(self) -> int:
        """
        Calculates the number of nodes in the Tree
        :returns: number of nodes in the tree
        """
        raise NotImplementedError("This method has not been implemented")

    @abstractmethod
    def next(self) -> int:
        raise NotImplementedError("This method has not been implemented")

    @abstractmethod
    def height(self) -> int:
        """
        Returns the height of the Tree. That is, the number of edges between the root node and the furthest leaf node.
        This can also be the maximum depth of the Tree
        This is the number of links from the root to the furthces leaf.
        """
        raise NotImplementedError("This method has not been implemented")

    @abstractmethod
    def lowest_common_ancestor(self, node_one: TreeNode, node_two: TreeNode) -> TreeNode:
        """
        Returns the lowest common ancestor of 2 nodes in the Tree.
        :param node_one
        :param node_two
        :returns the lowest common ancestor of the Tree
        :rtype TreeNode
        """
        raise NotImplementedError("This method has not been implemented")

    @abstractmethod
    def has_next(self) -> bool:
        raise NotImplementedError("This method has not been implemented")

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

    @abstractmethod
    def insert_node(self, value) -> TreeNode:
        """
        Based on the type of tree, this inserts a node in the Tree
        """
        raise NotImplementedError("This method has not been implemented")

    @abstractmethod
    def paths(self) -> list:
        """
        Prints all the paths of a Tree from root node to leaf nodes
        """
        raise NotImplementedError("This method has not been implemented")
