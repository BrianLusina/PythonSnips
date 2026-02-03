from typing import Optional
from datastructures.trees.binary.node import BinaryTreeNode
from datastructures.trees import T


def is_valid_bst(root: Optional[BinaryTreeNode]) -> bool:
    """
    Checks if a binary search tree is valid.
    Args:
        root(BinaryTreeNode): The root of the binary search tree.
    Returns:
        bool: True if the binary search tree is valid, False otherwise.
    """
    if not root:
        return True

    def dfs(node: Optional[BinaryTreeNode], min_value: T, max_value: T) -> bool:
        if not node:
            return True

        # Is the current node's value within the given range?
        if node.data <= min_value or node.data >= max_value:
            # If not, return False immediately
            return False

        return dfs(node.left, min_value, node.data) and dfs(
            node.right, node.data, max_value
        )

    return dfs(root, float("-inf"), float("inf"))
