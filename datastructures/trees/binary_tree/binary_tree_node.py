from typing import Any, Optional

from .. import TreeNode


class BinaryTreeNode(TreeNode):
    """
    Binary tree node class which will implement Binary tree
    """

    def __init__(self, data: Any):
        """
        Value here can be anything
        """
        super(BinaryTreeNode).__init__(data)
        self.left: Optional[BinaryTreeNode] = None
        self.right: Optional[BinaryTreeNode] = None

    def insert_node(self, data: Any) -> None:
        """
        Inserts a node using a Binary Search approach, where every data insert will be inserted to either the left or
        right based on whether the data is greater than the root node. if the data is greater than the root node,
        then the data will be inserted to the right. If  the data is less than the root node, then the insertion
        will be to the left of the root Node. This will apply for subsequent children of the root node and will
        be recursive.
        Assumption made here is that data insertions are int type
        :param: data, data to insert
        """
        # if the data being inserted is less than the current data and the left node exists
        if data < self.data and self.left:
            self.left.insert_node(data)

        elif data <= self.data:
            self.left = BinaryTreeNode(data)

        elif data > self.data and self.right:
            self.right.insert_node(data)

        else:
            self.right = BinaryTreeNode(data)

    def delete_node(self, data: Any, parent) -> bool:
        """
        Deletes a node from the tree if present and return result of deletion, True if delete was successful and
        False if the deletion was unsuccessful,
        :param data data we want to delete from the tree
        :param parent
        :rtype: bool True if the deletion was a success, false otherwise
        """
        # recursively check that the data is less than the current node data and that there is a left
        if data < self.data and self.left:
            return self.delete_node(data, self)

        if data < self.data:
            return False

        # recursively check that the data is greater than the current node data and that there is a right
        if data > self.data and self.right:
            return self.delete_node(data, self)

        if data > self.data:
            return False

        else:
            if self.left is None and self.right is None and self == parent.left:
                parent.left = None
                self.clear_node()

            elif self.left is None and self.right is None and self == parent.right:
                parent.right = None
                self.clear_node()

            elif self.left and self.right is None and self == parent.left:
                parent.left = self.left
                self.clear_node()

            elif self.left and self.right is None and self == parent.right:
                parent.right = self.left
                self.clear_node()

            elif self.right and self.left is None and self == parent.left:
                parent.left = self.right
                self.clear_node()

            elif self.right and self.left is None and self == parent.right:
                parent.right = self.right
                self.clear_node()

            else:
                self.data = self.right.find_minimum_data()
                self.right.delete_node(self.data, self)

        return True

    def clear_node(self):
        """
        Clears the node and sets the datas to None
        """
        self.data = None
        self.left = None
        self.right = None

    def find_minimum_data(self):
        """
        Find the minimum data by going way down to the left, if we can not find anymore nodes, we have reached the end
        """
        if self.left:
            return self.left.find_minimum_data()
        else:
            return self.data

    def insert_left(self, data: Any):
        """
        Inserts a new data(node) to the left of the current node and return the newly created node
        :param data the data to insert into the new node
        :rtype: BinaryTreeNode
        """
        if self.left is None:
            self.left = BinaryTreeNode(data)
        else:
            # create a new node
            new_node = BinaryTreeNode(data)
            # set the current left child node to become the left of the new node
            new_node.left = self.left
            # set the new left node of the current node to be the newly created node
            self.left = new_node
        return self.left

    def insert_right(self, data: Any):
        """
        Inserts a data to the right of the current node. This will check if the current node has a right child already
        and insert this node as the new right node of the current node and move the previous node (if not None) to
        become the new right node of the newly created node. This will then return the newly inserted node data
        :param data data used to create a new node
        :rtype: BinaryTreeNode
        """
        if self.right is None:
            self.right = BinaryTreeNode(data)
        else:
            new_node = BinaryTreeNode(data)
            new_node.right = self.right
            self.right = new_node
        return self.right
