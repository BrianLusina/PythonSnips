import unittest

from . import BinaryTree, BinaryTreeNode


class BinaryTreeDeserializeTestCases(unittest.TestCase):
    def test_1(self):
        """should return x for a tree with no root"""
        tree = "x"

        expected = None
        actual = BinaryTree.deserialize(tree)

        self.assertEquals(expected, actual)

    def test_2(self):
        """should return root(10, left(86), right(100) for 10 86 x x 100 x x"""
        tree = "10 86 x x 100 x x"

        right = BinaryTreeNode('100')
        left = BinaryTreeNode('86')
        expected = BinaryTreeNode('10', left=left, right=right)

        actual = BinaryTree.deserialize(tree)

        self.assertEquals(expected, actual)

    def test_3(self):
        """should return root(1, left(2), right(3) for 1 2 x x 3 x x"""
        tree = "1 2 x x 3 x x"

        right = BinaryTreeNode('3')
        left = BinaryTreeNode('2')
        expected = BinaryTreeNode('1', left=left, right=right)

        actual = BinaryTree.deserialize(tree)

        self.assertEquals(expected, actual)

    def test_4(self):
        """should return root(6, left(4, left(3), right(5)), right(8) for 6 4 3 x x 5 x x 8 x x"""
        tree = "6 4 3 x x 5 x x 8 x x"

        right = BinaryTreeNode('8')
        left_left = BinaryTreeNode('3')
        left_right = BinaryTreeNode('5')
        left = BinaryTreeNode('4', left=left_left, right=left_right)
        expected = BinaryTreeNode('6', left=left, right=right)

        actual = BinaryTree.deserialize(tree)

        self.assertEquals(expected, actual)


if __name__ == '__main__':
    unittest.main()
