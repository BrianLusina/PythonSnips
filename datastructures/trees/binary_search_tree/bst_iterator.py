from datastructures.stacks import Stack
from datastructures.trees.binary_tree_node import BinaryTreeNode


class BinarySearchTreeIterator:

    def __init__(self, root: BinaryTreeNode):
        self.root = root
        self.stack = Stack()

        self.__leftmost_inorder(root)

    def __leftmost_inorder(self, root: BinaryTreeNode) -> None:
        while root:
            self.stack.push(root)
            root = root.left

    def next(self) -> int:
        """
        Returns the next smallest number in a BST
        """

        # this is the smallest element in the BST
        topmost_node = self.stack.pop()

        # if the node has a right child, call the helper function for the right child to 
        # get the next smallest item
        # We don't need to check for the left child because of the way we have added nodes onto the stack. 
        # The topmost node either won't have a left child or would already have the left subtree processed. 
        # If it has a right child, then we call our helper function on the node's right child. 
        # This would comparatively be a costly operation depending upon the structure of the tree
        if topmost_node.right:
            self.__leftmost_inorder(topmost_node.right)

        return topmost_node.data

    def has_next(self) -> bool:
        return self.stack.is_empty()
