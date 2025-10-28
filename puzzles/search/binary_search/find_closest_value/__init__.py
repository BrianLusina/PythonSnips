from typing import Optional
from queue import Queue
from datastructures.trees.binary.search_tree import BinaryTreeNode


def find_closest_value_in_bst(node: BinaryTreeNode, target: int) -> Optional[int]:
    # edge case for empty nodes, if none is provided, we can't find a value that is close to the target
    if not node:
        return None

    # if the node's data is the target, exit early by returning it
    if node.data == target:
        return node.data

    # this keeps track of the minimum on both the left and the right
    min_diff = min_diff_left = min_diff_right = float("inf")
    closest_value = None
    fifo_queue = Queue()
    fifo_queue.put(node)

    # while the queue is not empty, we pop off nodes from the queue and check for their values
    while not fifo_queue.empty():
        current_node = fifo_queue.get()

        min_diff_left = abs(target - current_node.data)
        min_diff_right = abs(target - current_node.data)

        if min_diff_left < min_diff:
            min_diff = min_diff_left
            closest_value = current_node.data

        if min_diff_right < min_diff:
            min_diff = min_diff_right
            closest_value = current_node.data

        if current_node.left:
            fifo_queue.put(current_node.left)

        if current_node.right:
            fifo_queue.put(current_node.right)

    return closest_value
