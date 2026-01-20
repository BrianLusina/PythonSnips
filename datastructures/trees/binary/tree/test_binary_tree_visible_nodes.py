import unittest

from datastructures.trees.binary.tree import BinaryTree
from datastructures.trees.binary.node import BinaryTreeNode


class BinaryTreeVisibleNodesTestCases(unittest.TestCase):
    def test_1(self):
        """should return 3 from a tree of
          5 <- visible
        / \
       4   6 <- visible
      / \
     3   8 <- visible"""
        left = BinaryTreeNode(4, left=BinaryTreeNode(3), right=BinaryTreeNode(8))
        right = BinaryTreeNode(6)
        root = BinaryTreeNode(5, left=left, right=right)

        tree = BinaryTree(root=root)

        expected = 3
        actual = tree.visible_tree_nodes()

        self.assertEquals(expected, actual)


if __name__ == "__main__":
    unittest.main()
