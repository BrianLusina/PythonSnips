import unittest
from typing import List
from parameterized import parameterized
from datastructures.trees.binary.utils import (
    lowest_common_ancestor,
    lowest_common_ancestor_ptr,
    connect_all_siblings,
    connect_all_siblings_ptr,
)
from datastructures.trees.binary.node import BinaryTreeNode


class LowestCommonAncestorTestCase(unittest.TestCase):
    def test_1(self):
        """
        Test to ensure that the lowest common ancestor function returns the correct node for a given binary tree.

        The binary tree is structured as follows:
            10
            /   \
           11     22
          / \   / \
         6   5  19  14
        / \
       13  15

        The function should return the node with value 5, given the nodes with values 13 and 15.
        """
        root = BinaryTreeNode(data=10)

        # left subtree
        root.left = BinaryTreeNode(data=11, parent=root)
        root.left.left = BinaryTreeNode(data=6, parent=root.left)
        root.left.right = BinaryTreeNode(data=5, parent=root.left)
        root.left.right.left = BinaryTreeNode(data=13, parent=root.left.right)
        root.left.right.right = BinaryTreeNode(data=15, parent=root.left.right)

        # right subtree
        root.right = BinaryTreeNode(data=22, parent=root)
        root.right.right = BinaryTreeNode(data=14, parent=root.right)
        root.right.left = BinaryTreeNode(data=19, parent=root.right)

        node_one = root.left.right.left
        node_two = root.left.right.right
        expected = root.left.right
        actual = lowest_common_ancestor(node_one, node_two)
        self.assertEqual(expected, actual)

    def test_2(self):
        root = BinaryTreeNode(data=10)
        root.left = BinaryTreeNode(data=11, parent=root)
        node_one = BinaryTreeNode(data=6, parent=root.left)
        root.left.left = node_one
        root.left.right = BinaryTreeNode(data=5, parent=root.left)
        root.left.right.left = BinaryTreeNode(data=13, parent=root.left.right)
        root.left.right.right = BinaryTreeNode(data=15, parent=root.left.right)

        root.right = BinaryTreeNode(data=22, parent=root)
        root.right.left = BinaryTreeNode(data=19, parent=root.right)
        root.right.right = BinaryTreeNode(data=14, parent=root.right)
        node_two = root.right.right

        expected = root
        actual = lowest_common_ancestor(node_one, node_two)
        self.assertEqual(expected, actual)

    def test_3(self):
        root = BinaryTreeNode(data=10)

        # left subtree from root
        root.left = BinaryTreeNode(data=11, parent=root)
        root.left.left = BinaryTreeNode(data=6, parent=root.left)
        root.left.right = BinaryTreeNode(data=5, parent=root.left)
        root.left.right.left = BinaryTreeNode(data=13, parent=root.left.right)
        root.left.right.right = BinaryTreeNode(data=15, parent=root.left.right)

        # right subtree from root
        root.right = BinaryTreeNode(data=17, parent=root)
        root.right.left = BinaryTreeNode(data=19, parent=root.right)
        root.right.right = BinaryTreeNode(data=14, parent=root.right)

        node_one = root.left
        node_two = root.left.right.right
        expected = node_one
        actual = lowest_common_ancestor(node_one, node_two)
        self.assertEqual(expected, actual)

    def test_4(self):
        root = BinaryTreeNode(data=17)

        # left subtree from root
        root.left = BinaryTreeNode(data=3, parent=root)
        root.left.left = BinaryTreeNode(data=6, parent=root.left)
        root.left.right = BinaryTreeNode(data=5, parent=root.left)

        # right subtree from root
        root.right = BinaryTreeNode(data=16, parent=root)
        root.right.left = BinaryTreeNode(data=19, parent=root.right)
        root.right.right = BinaryTreeNode(data=14, parent=root.right)

        node_one = root.left.right
        node_two = root.right.left
        expected = root
        actual = lowest_common_ancestor(node_one, node_two)
        self.assertEqual(expected, actual)


class LowestCommonAncestorPtrTestCase(unittest.TestCase):
    def test_1(self):
        root = BinaryTreeNode(data=10)

        # left subtree
        root.left = BinaryTreeNode(data=11, parent=root)
        root.left.left = BinaryTreeNode(data=6, parent=root.left)
        root.left.right = BinaryTreeNode(data=5, parent=root.left)
        root.left.right.left = BinaryTreeNode(data=13, parent=root.left.right)
        root.left.right.right = BinaryTreeNode(data=15, parent=root.left.right)

        # right subtree
        root.right = BinaryTreeNode(data=22, parent=root)
        root.right.right = BinaryTreeNode(data=14, parent=root.right)
        root.right.left = BinaryTreeNode(data=19, parent=root.right)

        node_one = root.left.right.left
        node_two = root.left.right.right
        expected = root.left.right
        actual = lowest_common_ancestor_ptr(node_one, node_two)
        self.assertEqual(expected, actual)

    def test_2(self):
        root = BinaryTreeNode(data=10)
        root.left = BinaryTreeNode(data=11, parent=root)
        node_one = BinaryTreeNode(data=6, parent=root.left)
        root.left.left = node_one
        root.left.right = BinaryTreeNode(data=5, parent=root.left)
        root.left.right.left = BinaryTreeNode(data=13, parent=root.left.right)
        root.left.right.right = BinaryTreeNode(data=15, parent=root.left.right)

        root.right = BinaryTreeNode(data=22, parent=root)
        root.right.left = BinaryTreeNode(data=19, parent=root.right)
        root.right.right = BinaryTreeNode(data=14, parent=root.right)
        node_two = root.right.right

        expected = root
        actual = lowest_common_ancestor_ptr(node_one, node_two)
        self.assertEqual(expected, actual)

    def test_3(self):
        root = BinaryTreeNode(data=10)

        # left subtree from root
        root.left = BinaryTreeNode(data=11, parent=root)
        root.left.left = BinaryTreeNode(data=6, parent=root.left)
        root.left.right = BinaryTreeNode(data=5, parent=root.left)
        root.left.right.left = BinaryTreeNode(data=13, parent=root.left.right)
        root.left.right.right = BinaryTreeNode(data=15, parent=root.left.right)

        # right subtree from root
        root.right = BinaryTreeNode(data=17, parent=root)
        root.right.left = BinaryTreeNode(data=19, parent=root.right)
        root.right.right = BinaryTreeNode(data=14, parent=root.right)

        node_one = root.left
        node_two = root.left.right.right
        expected = node_one
        actual = lowest_common_ancestor_ptr(node_one, node_two)
        self.assertEqual(expected, actual)

    def test_4(self):
        root = BinaryTreeNode(data=17)

        # left subtree from root
        root.left = BinaryTreeNode(data=3, parent=root)
        root.left.left = BinaryTreeNode(data=6, parent=root.left)
        root.left.right = BinaryTreeNode(data=5, parent=root.left)

        # right subtree from root
        root.right = BinaryTreeNode(data=16, parent=root)
        root.right.left = BinaryTreeNode(data=19, parent=root.right)
        root.right.right = BinaryTreeNode(data=14, parent=root.right)

        node_one = root.left.right
        node_two = root.right.left
        expected = root
        actual = lowest_common_ancestor_ptr(node_one, node_two)
        self.assertEqual(expected, actual)


CONNECT_ALL_SIBLINGS_TEST_CASES = [
    (
        BinaryTreeNode(
            data=100,
            left=BinaryTreeNode(
                data=50, left=BinaryTreeNode(data=25), right=BinaryTreeNode(data=75)
            ),
            right=BinaryTreeNode(
                data=200, left=BinaryTreeNode(data=300), right=BinaryTreeNode(data=10)
            ),
        ),
        [100, 50, 200, 25, 75, 300, 10],
    ),
]


class ConnectAllSiblingsTestCase(unittest.TestCase):
    @parameterized.expand(CONNECT_ALL_SIBLINGS_TEST_CASES)
    def test_connect_all_siblings(self, root: BinaryTreeNode, expected: List[int]):
        actual = connect_all_siblings(root)
        current = actual
        for expected_val in expected:
            self.assertEqual(current.data, expected_val)
            current = current.next
        self.assertIsNone(current)

    @parameterized.expand(CONNECT_ALL_SIBLINGS_TEST_CASES)
    def test_connect_all_siblings_ptr(self, root: BinaryTreeNode, expected: List[int]):
        actual = connect_all_siblings_ptr(root)
        current = actual
        for expected_val in expected:
            self.assertEqual(current.data, expected_val)
            current = current.next
        self.assertIsNone(current)


if __name__ == "__main__":
    unittest.main()
