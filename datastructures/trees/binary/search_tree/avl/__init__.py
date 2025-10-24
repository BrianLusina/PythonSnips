from typing import Optional, List
from datastructures.trees import Tree, T
from .node import AvlTreeNode


class AVLTree(Tree):
    """
    Represents an AVL Tree implementation
    """

    def __init__(self, root: Optional[AvlTreeNode] = None):
        self.root = root

    def insert_node(self, value: T) -> AvlTreeNode:
        """Inserts a value into the AVL Tree returning the inserted node"""
        if not self.root:
            self.root = AvlTreeNode(data=value)
            return self.root

        def insert_node_helper(root: AvlTreeNode, data: T) -> AvlTreeNode:
            if not root:
                return AvlTreeNode(data=value)

            elif data < root.data:
                root.left = insert_node_helper(root.left, data)
            else:
                root.right = insert_node_helper(root.right, data)
            root.height = 1 + max(
                self.__get_height(root.left), self.__get_height(root.right)
            )

            # update the balance factor
            balance_factor = self.__get_balance_factor_of_node(root)

            if balance_factor > 1:
                if data < root.left.data:
                    return self.right_rotate(root)
                else:
                    root.left = self.left_rotate(root.left)
                    return self.right_rotate(root)

            if balance_factor < -1:
                if data > root.right.data:
                    return self.left_rotate(root)
                else:
                    root.right = self.right_rotate(root.right)
                    return self.left_rotate(root)
            return root

        return insert_node_helper(self.root, value)

    def delete_node(self, value: T) -> Optional[AvlTreeNode]:
        """
        Finds the node that contains the value and then performs a deletion of the node from the tree
        Deletes a node from the tree, returning it after re-balancing the tree

        @param value: Value to be deleted.
        @return: Deleted node if the tree has a root, otherwise returns None
        """
        if not self.root:
            return None

        def delete_node_helper(root: AvlTreeNode, data: T) -> Optional[AvlTreeNode]:
            if not root:
                return root
            elif data < root.data:
                root.left = delete_node_helper(root.left, data)
            elif data > root.data:
                root.right = delete_node_helper(root.right, data)
            else:
                if root.left is None:
                    temp = root.right
                    root = None
                    return temp
                elif root.right is None:
                    temp = root.left
                    root = None
                    return temp
                temp = self.get_min_value_node(root.right)
                root.data = temp.data
                root.right = delete_node_helper(root.right, temp.data)

            if root is None:
                return root

            # update the balance factor of nodes
            root.height = 1 + max(
                self.__get_height(root.left), self.__get_height(root.right)
            )

            balance_factor = self.__get_balance_factor_of_node(root)

            # balance the tree
            if balance_factor > 1:
                if self.__get_balance_factor_of_node(root.left) >= 0:
                    return self.right_rotate(root)
                else:
                    root.left = self.left_rotate(root.left)
                    return self.right_rotate(root)

            if balance_factor < -1:
                if self.__get_balance_factor_of_node(root.right) <= 0:
                    return self.left_rotate(root)
                else:
                    root.right = self.right_rotate(root.right)
                    return self.left_rotate(root)

            return root

        return delete_node_helper(self.root, value)

    @staticmethod
    def __get_height(root: AvlTreeNode) -> int:
        """Gets the height of a node"""
        if not root:
            return 0
        return root.height

    def __get_balance_factor_of_node(self, root: AvlTreeNode) -> int:
        """Gets the balance factor of a node"""
        if not root:
            return 0
        return self.__get_height(root.left) - self.__get_height(root.right)

    def right_rotate(self, root: AvlTreeNode) -> AvlTreeNode:
        """Performs right rotation of a node"""
        y = root.left
        t3 = y.right
        y.right = root
        root.left = t3
        root.height = 1 + max(
            self.__get_height(root.left), self.__get_height(root.right)
        )
        y.height = 1 + max(self.__get_height(y.left), self.__get_height(y.right))
        return y

    def left_rotate(self, root: AvlTreeNode) -> AvlTreeNode:
        """Performs a left rotation of a node"""
        y = root.right
        t2 = y.left
        y.left = root
        root.right = t2
        root.height = 1 + max(
            self.__get_height(root.left), self.__get_height(root.right)
        )
        y.height = 1 + max(self.__get_height(y.left), self.__get_height(y.right))
        return y

    def get_min_value_node(self, root: AvlTreeNode) -> Optional[AvlTreeNode]:
        if root is None or root.left is None:
            return root
        return self.get_min_value_node(root.left)

    def pre_order_traversal(self) -> List[T]:
        data = []
        if not self.root:
            return data

        def pre_order_helper(root: AvlTreeNode):
            if not root:
                return
            data.append(root.data)
            pre_order_helper(root.left)
            pre_order_helper(root.right)

        pre_order_helper(self.root)
        return data
