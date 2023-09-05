from typing import List, Generic, TypeVar
from abc import ABC, abstractmethod

T = TypeVar("T")


class TreeNode(Generic[T]):
    """
    Tree node class which will implement Tree Node.
    Note that this could be any type of tree node. Not all tree nodes have only left or right children, they could have
    more than one child. In this case `children` property is a list of all the immediate descendants of the node.
    """

    def __init__(self, value: T):
        """
        Value here can be anything
        """
        self.data = value


class Tree(ABC, Generic[T]):
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
        This is the number of links from the root to the furthest leaf.
        """
        raise NotImplementedError("This method has not been implemented")

    @abstractmethod
    def lowest_common_ancestor(
            self, node_one: TreeNode, node_two: TreeNode
    ) -> TreeNode:
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
        Gets the depth of the tree or height of the tree
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

    @abstractmethod
    def level_order_traversal(self) -> List[T]:
        raise NotImplementedError("This method has not been implemented")

    @abstractmethod
    def pre_order_traversal(self) -> List[T]:
        raise NotImplementedError("This method has not been implemented")

    @abstractmethod
    def is_balanced(self) -> bool:
        """
        Checks if this tree is balanced.
        A balanced tree is a tree where every node has 0 or more n children for n-ary trees or for binary trees, where
        the heights of its left and right subtrees differ by at most 1 or 0 and both subtrees are also balanced.
        @return: True if the tree is balanced, false otherwise
        """
        raise NotImplementedError("This method has not yet been implemented")

    @abstractmethod
    def leaf_similar(self, other: 'Tree') -> bool:
        """
        Returns true if this tree has similar leaf value sequence to another tree.
        For example: If this tree has nodes = [3,5,1,6,2,9,8,null,null,7,4] and other tree has nodes =
        [3,5,1,6,7,4,2,null,null,null,null,null,null,9,8]. Then the leaf value sequence of both is [6,7,4,9,8] which is
        similar
        @param other: Other tree
        @return: True if the sequence of both tree's leaves is similar, false otherwise
        """
        raise NotImplementedError("not yet implemented")

    @abstractmethod
    def number_of_good_nodes(self) -> int:
        """
        Finds the number of good nodes in a tree. A good node is a node in which in the path from root to the node there
        are no nodes with a value greater than it
        @return: The number of good nodes
        """
        raise NotImplementedError("not yet implemented")

    @abstractmethod
    def path_sum(self, target: T) -> int:
        """Returns the number of paths where the sum of the values along the path equals target

        Args:
            target (T): The target that the sum of values along the path must equal

        Returns:
            int: The number of paths along which the values equal the target
        """
        raise NotImplementedError("not yet implemented")

    def max_level_sum(self) -> int:
        """Returns the smallest level x such that the sum of all the values of nodes at level x is maximal

        Returns:
            int: maximum value at level x
        """
        raise NotImplementedError("not yet implemented")
