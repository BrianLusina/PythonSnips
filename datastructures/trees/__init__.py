from typing import List, Generic, TypeVar, Any
from abc import ABC, abstractmethod
from .node import TreeNode

T = TypeVar("T", bound=Any)


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
        """Traverses the tree in pre-order walking the left subtree before finally walking the right subtree returning
        a list of values on each node

        Complexity:
        Time Complexity O(n): where n is the number of nodes in the tree, as the algorithm has to traverse all the nodes
        in the tree

        Space Complexity O(h), where h is the height of the tree

        Returns:
            list: list of values of each node
        """
        raise NotImplementedError("This method has not been implemented")

    def inorder_traversal(self) -> List[T]:
        """
        Walks the left subtree first, then visits the current node, and finally walks the right subtree
        The algorithm looks something like this:

        1. Check if the current node is empty/null.
        2. Traverse the left subtree by recursively calling the in-order method.
        3. Display the data part of the root (or current node).
        4. Traverse the right subtree by recursively calling the in-order method.

        Complexity:
        Where `n` is the number of nodes in the tree

        Time Complexity: O(n) as each node in the tree is traversed
        Space Complexity: O(n) as each node or node data is stored in a list/collection to be returned

        Returns:
            List: list of nodes or node values/data traversed in inorder traversal fashion.
        """

    def post_order_traversal(self) -> List[T]:
        """
        Walks the left subtree first, then the right subtree and finally visits the current node
        The algorithm looks something like this:

        1. Check if the current node is empty/null.
        2. Traverse the left subtree by recursively calling the post-order method.
        3. Traverse the right subtree by recursively calling the post-order method.
        4. Display the data part of the root (or current node).

        Complexity:
        Where `n` is the number of nodes in the tree

        Time Complexity: O(n) as each node in the tree is traversed
        Space Complexity: O(n) as each node or node data is stored in a list/collection to be returned

        Returns:
            List: list of nodes or node values/data traversed in inorder traversal fashion.
        """

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
    def leaf_similar(self, other: "Tree") -> bool:
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

    @abstractmethod
    def paths_to_target(self, target: T) -> List[T]:
        """Returns the paths where the sum of the values along the path equals to the given target

        Args:
            target (T): The target that the sum of values along the path must equal

        Returns:
            list: The paths along which the values equal the target
        """
        raise NotImplementedError("not yet implemented")

    def max_level_sum(self) -> int:
        """Returns the smallest level x such that the sum of all the values of nodes at level x is maximal

        Returns:
            int: maximum value at level x
        """
        raise NotImplementedError("not yet implemented")

    @abstractmethod
    def serialize(self) -> str:
        """Serializes a tree into a string
        Returns:
            str: string representation of tree.
        """
        raise NotImplementedError("not yet implemented")

    @staticmethod
    def deserialize(tree_str: str) -> "Tree":
        """Serializes a tree into a string
        Args:
            tree_str (str): string representation of tree
        Returns:
            Tree: Tree deserialized from string
        """
        raise NotImplementedError("not yet implemented")
