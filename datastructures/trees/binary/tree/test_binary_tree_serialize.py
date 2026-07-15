import unittest

from datastructures.trees.binary.tree import BinaryTree
from datastructures.trees.binary.node import BinaryTreeNode


class BinaryTreeSerializeTestCases(unittest.TestCase):
    def test_1(self):
        """should return x for a tree with no root"""
        tree = BinaryTree()

        expected = "x"
        actual = tree.serialize()

        self.assertEquals(expected, actual)

    def test_2(self):
        """should return 10 86 x x 100 x x for root(10, left(86), right(100)"""
        right = BinaryTreeNode(100)
        left = BinaryTreeNode(86)
        root = BinaryTreeNode(10, left=left, right=right)

        tree = BinaryTree(root)

        expected = "10 86 x x 100 x x"
        actual = tree.serialize()

        self.assertEquals(expected, actual)

    def test_3(self):
        """should return 1 2 x x 3 x x for root(1, left(2), right(3)"""
        right = BinaryTreeNode(3)
        left = BinaryTreeNode(2)
        root = BinaryTreeNode(1, left=left, right=right)

        tree = BinaryTree(root)

        expected = "1 2 x x 3 x x"
        actual = tree.serialize()

        self.assertEquals(expected, actual)

    def test_4(self):
        """should return 6 4 3 x x 5 x x 8 x x for root(6, left(4, left(3), right(5)), right(8)"""
        right = BinaryTreeNode(8)
        left_left = BinaryTreeNode(3)
        left_right = BinaryTreeNode(5)
        left = BinaryTreeNode(4, left=left_left, right=left_right)
        root = BinaryTreeNode(6, left=left, right=right)

        tree = BinaryTree(root)

        expected = "6 4 3 x x 5 x x 8 x x"
        actual = tree.serialize()

        self.assertEquals(expected, actual)


if __name__ == "__main__":
    unittest.main()
