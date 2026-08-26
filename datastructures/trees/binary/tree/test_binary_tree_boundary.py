import unittest
from typing import List
from parameterized import parameterized
from utils.test_utils import custom_test_name_func
from datastructures.trees.binary.tree import BinaryTree
from datastructures.trees.binary.tree.binary_tree_utils import create_tree_from_nodes

BINARY_TREE_BOUNDARY_TEST_CASES = [
    ([42], [42]),
    ([20, 15, None, 10, None, 8, None], [20, 15, 10, 8]),
    ([4, 2, 6, 1, 3, 5, 7], [4, 2, 1, 3, 5, 7, 6]),
    ([10, 5, 20, None, 8, 15, 25], [10, 5, 8, 15, 25, 20]),
    ([0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0]),
    ([1, None, 2, None, 3, None, 4], [1, 4, 3, 2]),
]


class BinaryTreeBoundaryTestCase(unittest.TestCase):
    @parameterized.expand(
        BINARY_TREE_BOUNDARY_TEST_CASES, name_func=custom_test_name_func
    )
    def test_boundary(self, data: List[int], expected: List[int]):
        root = create_tree_from_nodes(data)
        binary_tree = BinaryTree(root=root)
        actual = binary_tree.boundary()

        self.assertEqual(expected, actual)

    @parameterized.expand(
        BINARY_TREE_BOUNDARY_TEST_CASES, name_func=custom_test_name_func
    )
    def test_boundary_iterative(self, data: List[int], expected: List[int]):
        root = create_tree_from_nodes(data)
        binary_tree = BinaryTree(root=root)
        actual = binary_tree.boundary_iterative()

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
