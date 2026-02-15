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


def kth_smallest_element(root: BinaryTreeNode, k: int) -> Optional[BinaryTreeNode]:
    """
    Finds the Kth smallest element in a binary search tree.

    This function recursively performs the inorder traversal(left subtree, root, right subtree) on the binary search
    tree. We will use the inorder traversal to get elements in sorted order.

    While performing the inorder traversal on the tree, decrement k by 1, indicating the number of smaller elements that
    still need to be found. After decrementing k, we check whether the value of k has reached 0. If it is 0, we return
    the current node, indicating the node having the kth smallest element. If not, continue the traversal.

    This approach ensures that we traverse the tree in a depth-first manner while appropriately updating k and
    effectively finding the kth smallest element.

    Time complexity

    The time complexity of this solution is O(n), where n represents the number of nodes in the binary tree.

    Space complexity

    The space complexity of this solution is O(n). This is because our recursive algorithm uses space on the call stack.

    Args:
        root(BinaryTreeNode): The root of the binary search tree
        k(int): The Kth smallest element to find.
    Returns:
        BinaryTreeNode: The Kth smallest element in a binary search tree.
    """
    if not root:
        return None

    counter = k
    kth_smallest = None

    def inorder_traversal(node: Optional[BinaryTreeNode]):
        nonlocal counter
        nonlocal kth_smallest

        if not node:
            return
        inorder_traversal(node.left)
        counter -= 1
        if counter == 0:
            kth_smallest = node.data
        inorder_traversal(node.right)

    inorder_traversal(root)
    return kth_smallest
