from typing import List, Optional, Any
from datastructures.trees.binary.node import BinaryTreeNode
from queue import Queue
from itertools import chain


def create_tree_from_nodes(nodes: List[Any]) -> Optional[BinaryTreeNode]:
    """
    Factory method to create a BinaryTreeNode given a list of values
    Args:
        nodes: List of values to be used to create the tree
    Returns:
        Optional[BinaryTreeNode]: The root of the created tree
    """
    if len(nodes) == 0:
        return None

    root = BinaryTreeNode(nodes[0])

    queue: Queue[BinaryTreeNode] = Queue()
    queue.put(root)

    i = 1
    while i < len(nodes):
        # Get the next node from the queue
        curr = queue.get()

        # If the node is not None, create a new TreeNode object for its left child,
        # set it as the left child of the current node, and add it to the queue
        if nodes[i] is not None:
            curr.left = BinaryTreeNode(nodes[i])
            queue.put(curr.left)

        i += 1
        # If there are more nodes in the list and the next node is not None, create a new BinaryTreeNode for its
        # right child, set it as the right child of the current node, and add it to the queue
        if i < len(nodes) and nodes[i] is not None:
            curr.right = BinaryTreeNode(nodes[i])
            queue.put(curr.right)

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
