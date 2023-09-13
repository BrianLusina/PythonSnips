import unittest
from datastructures.trees.binary.node import BinaryTreeNode
from . import path_sum


class PathSumTestCases(unittest.TestCase):
    def test_1(self):
        """
        should return [[5,4,11,2], [5,8,4,5]] Given the below binary tree and sum = 22,

              5
             / \
            4   8
           /   / \
          11  13  4
         /  \    / \
        7    2  5   1
        """
        left = BinaryTreeNode(4, left=BinaryTreeNode(11, left=BinaryTreeNode(7), right=BinaryTreeNode(2)))
        right = BinaryTreeNode(8, left=BinaryTreeNode(13),
                               right=BinaryTreeNode(4, left=BinaryTreeNode(5), right=BinaryTreeNode(1)))
        root = BinaryTreeNode(5, left=left, right=right)

        expected = [[5, 4, 11, 2], [5, 8, 4, 5]]
        target = 22
        actual = path_sum(root, target)

        self.assertEqual(expected, actual)

    def test_2(self):
        """
        should return [] Given no root binary tree and sum = 22
        """
        expected = []
        target = 22
        actual = path_sum(None, target)

        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
