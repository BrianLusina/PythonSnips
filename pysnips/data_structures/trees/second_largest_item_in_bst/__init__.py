from .. import BinaryTreeNode


# class BinaryTreeNode(object):
#
#     def __init__(self, value):
#         self.value = value
#         self.left = None
#         self.right = None
#
#     def insert_left(self, value):
#         self.left = BinaryTreeNode(value)
#         return self.left
#
#     def insert_right(self, value):
#         self.right = BinaryTreeNode(value)
#         return self.right


def find_largest(root_node: BinaryTreeNode):
    """
    Simply finds the largest node in a BST. We walk righward down the BST until the current node has no right child
    and return it
    :param root_node: root node, or current node
    :return: Value of the largest node
    :rtype: object
    """
    current_node = root_node

    while current_node:

        if not current_node.right:
            return current_node.value

        current_node = current_node.right


def find_second_largest(root_node: BinaryTreeNode):
    """
    Finds the second largest node in the Binary Search Tree given a root node
    :param root_node: BinaryTreeNode
    :type root_node BinaryTreeNode
    :return: Value of the second largest Node
    :rtype: object
    """
    if root_node is None or (root_node.left is None and root_node.right is None):
        raise ValueError("Tree must have at least 2 nodes")

    current_node = root_node

    while current_node:

        # if the current node has no right subtree, we step to the left to find the second largest in the current node's
        # left subtree
        if current_node.left and not current_node.right:
            return find_largest(current_node.left)

        # if the current node is the parent of the largest and largest has no children, then the current node is the
        # second largest in the Tree

        if current_node.right and not current_node.right.left and not current_node.right.right:
            return current_node.value

        current_node = current_node.right
