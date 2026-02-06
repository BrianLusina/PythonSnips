import unittest
from typing import List
from parameterized import parameterized
from datastructures.trees.binary.search_tree import BinarySearchTree
from datastructures.trees.binary.search_tree.bst_utils import is_valid_bst

IS_VALID_BST_TEST_CASES = [
    ([8, 3, 10, 1, 6], True),
    ([2, 1, 4], True),
    ([1, None, 1], False),
    ([6, 2, 8, None, None, 7, 11], True),
]


class BinarySearchTreeIsValidTestCases(unittest.TestCase):
    @parameterized.expand(IS_VALID_BST_TEST_CASES)
    def test_is_valid(self, data: List[int], expected: bool):
        search_tree = BinarySearchTree()
        for d in data:
            search_tree.insert_node(d)

        actual = search_tree.is_valid()

        self.assertEqual(expected, actual)

    @parameterized.expand(IS_VALID_BST_TEST_CASES)
    def test_is_valid_recursive(self, data: List[int], expected: bool):
        search_tree = BinarySearchTree()
        for d in data:
            search_tree.insert_node(d)

        actual = search_tree.is_valid_recursive()

        self.assertEqual(expected, actual)

    @parameterized.expand(IS_VALID_BST_TEST_CASES)
    def test_is_valid_util(self, data: List[int], expected: bool):
        search_tree = BinarySearchTree()
        for d in data:
            search_tree.insert_node(d)

        actual = is_valid_bst(search_tree.root)

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
