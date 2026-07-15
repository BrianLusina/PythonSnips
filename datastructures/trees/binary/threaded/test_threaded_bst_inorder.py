import unittest
from typing import List
from parameterized import parameterized
from utils.test_utils import custom_test_name_func
from datastructures.trees.binary.threaded.threaded_binary_search_tree import (
    ThreadedBinarySearchTree,
)

THREADED_BST_INORDER_TESTCASES = [([4, 2, 6, 1, 3, 5, 7], [1, 2, 3, 4, 5, 6, 7])]

THREADED_BST_REVERSE_INORDER_TESTCASES = [
    ([4, 2, 6, 1, 3, 5, 7], [7, 6, 5, 4, 3, 2, 1])
]


class ThreadedBinarySearchTreeInorderTraversalTestCase(unittest.TestCase):
    @parameterized.expand(
        THREADED_BST_INORDER_TESTCASES, name_func=custom_test_name_func
    )
    def test_inorder_traversal(self, values: List[int], expected: List[int]):
        tree = ThreadedBinarySearchTree()
        for value in values:
            tree.insert_node(value)

        actual = tree.inorder_traversal()
        self.assertEqual(expected, actual)

    @parameterized.expand(
        THREADED_BST_REVERSE_INORDER_TESTCASES, name_func=custom_test_name_func
    )
    def test_reverse_inorder_traversal(self, values: List[int], expected: List[int]):
        tree = ThreadedBinarySearchTree()
        for value in values:
            tree.insert_node(value)

        actual = tree.reverse_inorder_traversal()
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
