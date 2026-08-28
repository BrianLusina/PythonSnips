import unittest
from typing import Any

from parameterized import parameterized
from utils.test_utils import custom_test_name_func
from datastructures.trees.binary.tree import BinaryTree
from datastructures.trees.binary.tree.binary_tree_utils import create_tree_from_nodes

BINARY_TREE_MIN_DEPTH_TEST_CASES = [
    ([3, 9, 20, None, None, 15, 7], 2),
    ([2, None, 3, None, 4, None, 5, None, 6], 5),
]


class BinaryTreeMinDepthTestCase(unittest.TestCase):
    @parameterized.expand(
        BINARY_TREE_MIN_DEPTH_TEST_CASES, name_func=custom_test_name_func
    )
    def test_min_depth_recursive(self, data: list[Any], expected: int):
        root = create_tree_from_nodes(data)
        binary_tree = BinaryTree(root=root)
        actual = binary_tree.min_depth_recursive()
        self.assertEqual(expected, actual)

    @parameterized.expand(
        BINARY_TREE_MIN_DEPTH_TEST_CASES, name_func=custom_test_name_func
    )
    def test_min_depth_iterative(self, data: list[Any], expected: int):
        root = create_tree_from_nodes(data)
        binary_tree = BinaryTree(root=root)
        actual = binary_tree.min_depth_iterative()
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
