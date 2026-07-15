import unittest

from datastructures.trees.binary.tree import BinaryTree
from datastructures.trees.binary.node import BinaryTreeNode


class BinaryTreeCreateTreeTestCases(unittest.TestCase):
    def test_create_tree_1(self):
        """should create a tree from [1, None, 1, 1, 1, None, None, 1, 1, None, 1, None, None, None, 1]"""
        elements = [1, None, 1, 1, 1, None, None, 1, 1, None, 1, None, None, None, 1]
        tree = BinaryTree.create_tree(elements)

        self.assertEqual(1, tree.root.data)
        self.assertIsNone(tree.root.left)


if __name__ == "__main__":
    unittest.main()
