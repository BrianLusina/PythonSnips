from typing import List
from datastructures.trees.binary.node import BinaryTreeNode


class Solution:
    def level_order(self, root: BinaryTreeNode) -> List[List[int]]:
        self.result = []
        self.traverse(root, 0)
        return self.result

    def traverse(self, root: BinaryTreeNode, level):
        if root is None:
            return

        if level + 1 > len(self.result):
            self.result.append([root.data])
        else:
            self.result[level].append(root.data)

        self.traverse(root.left, level + 1)
        self.traverse(root.right, level + 1)


def level_order(root: BinaryTreeNode) -> List[List[int]]:
    """
    This takes 16ms to compute
    """
    if not root:
        return []

    curr = [root]
    res = []

    while curr:
        level_node = []
        next_level = []
        for node in curr:
            level_node.append(node.data)

            if node.left:
                next_level.append(node.left)
            if node.right:
                next_level.append(node.right)

        res.append(level_node)
        curr = next_level

    return res
