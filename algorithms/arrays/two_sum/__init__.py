from typing import List, Deque, Set
from collections import deque
from datastructures.trees.binary.node import BinaryTreeNode


def two_sum(numbers: List[int], target: int) -> List[int]:
    """
    Finds two numbers in a given list of integers which sum up to the target. This assumes the numbers are sorted in
    ascending order.

    Complexity:
    Where n is the number of elements in the list.

    Time: O(n) as the algorithm has to iterate through each element in the list
    Space: O(n) as the algorithm stores each element in a dictionary that it uses to check if the element that has been
    seen already sums up to the target with the current element the algorithm is iterating over.

    Args:
        numbers List: list of numbers
        target int: Target number
    Returns:
        List of two numbers that sum up to the target
    """
    m = {}

    for idx, num in enumerate(numbers, start=1):
        complement = target - num

        if complement in m:
            return [m[complement], idx]
        m[num] = idx
    return []


def two_sum_with_pointers(numbers: List[int], target: int) -> List[int]:
    """
    Finds two numbers in a given list of integers which sum up to the target. This assumes the numbers are sorted in
    ascending order.

    Complexity:
    Where n is the number of elements in the list.

    Time: O(n) as the algorithm has to iterate through each element in the list
    Space: O(1) as the algorithm does not store elements in a data structure and simply iterates through each element
     comparing the element on the left with the element on the right

    Args:
        numbers List: list of numbers
        target int: Target number
    Returns:
        List of indices of the two numbers that sum up to the target
    """
    first_pointer = 0
    last_pointer = len(numbers) - 1

    while first_pointer < last_pointer:
        result = numbers[first_pointer] + numbers[last_pointer]
        if result == target:
            return [first_pointer, last_pointer]
        elif result < target:
            first_pointer += 1
        else:
            last_pointer -= 1
    return []


def two_sum_find_target(root: BinaryTreeNode, k: int) -> bool:
    """
    Checks if two nodes in the binary search tree add up to the given target number

    Args:
        root (BinaryTreeNode): root of the binary search tree
        k (int): target number
    Returns:
        bool: True if there are two nodes in the binary search tree that add up to the target, False otherwise
    """
    if not root:
        return False

    # store the seen values so far during the traversal
    seen: Set[int] = set()

    # Keep track of visited nodes, we start with the root node. We use a FIFO queue here
    queue: Deque[BinaryTreeNode] = deque()
    queue.append(root)

    while queue:
        # dequeue the first node, the front of the queue.
        curr = queue.popleft()

        if curr:
            # check if the complement of this node's value exists in the values we have seen so far
            if (k - curr.data) in seen:
                return True

            # if not, add the value
            seen.add(curr.data)

            # enqueue the left and right children of the current node
            queue.append(curr.left)
            queue.append(curr.right)

    # if we reach here, we have not found two nodes that add up to the target
    return False
