from typing import Optional
from datastructures.trees.binary.search_tree import BinaryTreeNode


def find_closest_value_in_bst(node: BinaryTreeNode, target: int) -> Optional[int]:
    # edge case for empty nodes, if none is provided, we can't find a value that is close to the target
    if not node:
        return None

    # if the node's data is the target, exit early by returning it
    if node.data == target:
        return node.data

    # this keeps track of the minimum on both the left and the right
    closest_value = node.data
    min_diff = abs(target - node.data)
    current = node

    # while the queue is not empty, we pop off nodes from the queue and check for their values
    while current:
        current_diff = abs(target - current.data)

        if current_diff < min_diff:
            min_diff = current_diff
            closest_value = current.data

        if current.data == target:
            return current.data

        if target < current.data:
            current = current.left
        else:
            current = current.right

    return closest_value
