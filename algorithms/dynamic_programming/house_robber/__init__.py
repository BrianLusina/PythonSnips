from typing import List, Optional, Dict

from datastructures.trees.binary.node import BinaryTreeNode


def rob(nums: List[int]) -> int:
    """Uses a top-down approach using Rolling Window technique where the idea is to only remember what is the maximum
    gain at the next three houses from the current position."""
    current, previous = 0, 0

    for house in nums:
        current, previous = max(previous + house, current), current

    return current


def rob_iii_recursion(root: Optional[BinaryTreeNode]) -> int:
    if not root:
        return 0
    res = root.data

    if root.left:
        res += rob_iii_recursion(root.left.left) + rob_iii_recursion(root.left.right)
    if root.right:
        res += rob_iii_recursion(root.right.left) + rob_iii_recursion(root.right.right)

    res = max(res, rob_iii_recursion(root.left) + rob_iii_recursion(root.right))
    return res


def rob_iii_dynamic_programming_top_down(root: Optional[BinaryTreeNode]) -> int:
    if not root:
        return 0

    cache: Dict[BinaryTreeNode, int] = {}

    def dfs(node: Optional[BinaryTreeNode]) -> int:
        if not node:
            return 0

        if node in cache:
            return cache[node]

        cache[node] = node.data

        if node.left:
            cache[node] += dfs(node.left.left) + dfs(node.left.right)
        if node.right:
            cache[node] += dfs(node.right.left) + dfs(node.right.right)

        cache[node] = max(cache[node], dfs(node.left) + dfs(node.right))
        return cache[node]

    return dfs(root)


def rob_iii_dynamic_programming_bottom_up(root: Optional[BinaryTreeNode]) -> int:
    if not root:
        return 0

    def dfs(node: Optional[BinaryTreeNode]) -> List[int]:
        # Empty tree case
        if not node:
            return [0, 0]

        # Recursively calculating the maximum amount that can be robbed from the left subtree of the root
        left_subtree = dfs(node.left)
        # Recursively calculating the maximum amount that can be robbed from the right subtree of the root
        right_subtree = dfs(node.right)

        # include_root contains the maximum amount of money that can be robbed with the parent node included
        include_root = node.data + left_subtree[1] + right_subtree[1]

        # exclude_root contains the maximum amount of money that can be robbed with the parent node excluded
        exclude_root = max(left_subtree) + max(right_subtree)

        return [include_root, exclude_root]

    # Returns maximum value from the pair: [include_root, exclude_root]
    return max(dfs(root))
