from typing import Optional, List
from datastructures.trees.binary.search_tree import BinarySearchTree
from datastructures.trees.binary.node import BinaryTreeNode
from datastructures.trees.types import T


class ThreadedBinarySearchTree(BinarySearchTree):
    """
    A fully (double-)threaded binary search tree.

    Every node's left/right pointer is EITHER a real child link OR a "thread" -
    a shortcut straight to that node's inorder predecessor / successor. Which
    one it is gets tracked with a boolean flag per side. This lets us traverse
    the whole tree in sorted order with O(1) extra space: no recursion, no
    explicit stack.
    """

    def insert_node(self, value: Optional[T]) -> None:
        if self.root is None:
            self.root = BinaryTreeNode(value)
            return None
        current = self.root

        while True:
            # No duplicates
            if value == current.data:
                return None
            if value < current.data:
                if not current.left_thread and current.left is not None:
                    current = current.left
                    continue

                new_node = BinaryTreeNode(value)
                new_node.left = current.left  # inherit current's predecessor
                new_node.left_thread = True
                new_node.right = current  # current is the new successor
                new_node.right_thread = True
                current.left = new_node
                current.left_thread = False
                return None
            else:
                if not current.right_thread and current.right is not None:
                    current = current.right
                    continue
                new_node = BinaryTreeNode(value)
                new_node.right = current.right  # inherit current's successor
                new_node.right_thread = True
                new_node.left = current  # current is the new predecessor
                new_node.left_thread = True
                current.right = new_node
                current.right_thread = False
                return None

    @staticmethod
    def _leftmost(node: Optional[BinaryTreeNode]) -> Optional[BinaryTreeNode]:
        if node is None:
            return None
        while not node.left_thread and node.left is not None:
            node = node.left
        return node

    @staticmethod
    def _rightmost(node: Optional[BinaryTreeNode]) -> Optional[BinaryTreeNode]:
        if node is None:
            return None
        while not node.right_thread and node.right is not None:
            node = node.right
        return node

    def successor(self, node: BinaryTreeNode) -> Optional[BinaryTreeNode]:
        if node.right_thread:
            return node.right
        return self._leftmost(node.right)

    def predecessor(self, node: BinaryTreeNode) -> Optional[BinaryTreeNode]:
        if node.left_thread:
            return node.left
        return self._rightmost(node.left)

    def inorder_traversal(self) -> List[T]:
        """Iterative inorder traversal using threads only - no stack needed."""
        result = []
        cur = self._leftmost(self.root)
        while cur is not None:
            result.append(cur.data)
            cur = self.successor(cur)
        return result

    def reverse_inorder_traversal(self) -> List[T]:
        """Same idea, walking predecessor threads right-to-left."""
        result = []
        cur = self._rightmost(self.root)
        while cur is not None:
            result.append(cur.data)
            cur = self.predecessor(cur)
        return result
