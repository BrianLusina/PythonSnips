from typing import List, Optional, Any
from datastructures.trees.binary.node import BinaryTreeNode
from collections import deque
from itertools import chain


def create_tree_from_nodes(nodes: List[Any]) -> Optional[BinaryTreeNode]:
    """
    Factory method to create a BinaryTreeNode given a list of values
    Args:
        nodes: List of values to be used to create the tree
    Returns:
        Optional[BinaryTreeNode]: The root of the created tree
    """
    if not nodes or nodes[0] is None:
        return None

    root = BinaryTreeNode(nodes[0])

    queue = deque([root])

    i = 1
    while i < len(nodes):
        # Get the next node from the queue
        curr = queue.popleft()

        # If the node is not None, create a new TreeNode object for its left child,
        # set it as the left child of the current node, and add it to the queue
        if nodes[i] is not None:
            curr.left = BinaryTreeNode(nodes[i])
            queue.append(curr.left)

        i += 1
        # If there are more nodes in the list and the next node is not None, create a new BinaryTreeNode for its
        # right child, set it as the right child of the current node, and add it to the queue
        if i < len(nodes) and nodes[i] is not None:
            curr.right = BinaryTreeNode(nodes[i])
            queue.append(curr.right)

        i += 1

    # Return the root of the binary tree
    return root


def level_order_traversal(root: Optional[BinaryTreeNode]) -> List[Any]:
    if not root:
        return []

    current_level: List[Optional[BinaryTreeNode]] = [root]
    levels: List[List[Any]] = []

    while current_level:
        level: List[Any] = []
        next_level: List[Optional[BinaryTreeNode]] = []

        for node in current_level:
            if not node:
                level.append(None)
                next_level.append(None)
            else:
                level.append(node.data)

                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)

        levels.append(level)
        current_level = next_level

    return list(chain.from_iterable(levels))


def longest_uni_value_path(root: Optional[BinaryTreeNode]) -> int:
    """
    Returns the length of the longest path, where each node in the path has the same value. This path may or may
    not pass through the root.

    The length of the path between two nodes is represented by the number of edges between them.
    """
    max_length = 0

    def dfs(node: Optional[BinaryTreeNode]) -> int:
        nonlocal max_length

        if not node:
            return 0

        left_value = dfs(node.left)
        right_value = dfs(node.right)

        left_arrow, right_arrow = 0, 0
        if node.left and node.left.data == node.data:
            left_arrow = left_value + 1
        if node.right and node.right.data == node.data:
            right_arrow = right_value + 1

        max_length = max(max_length, left_arrow + right_arrow)
        return max(left_arrow, right_arrow)

    dfs(root)
    return max_length
