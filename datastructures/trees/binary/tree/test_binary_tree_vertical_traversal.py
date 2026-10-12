import unittest
from parameterized import parameterized
from utils.test_utils import custom_test_name_func
from datastructures.trees.binary.tree import BinaryTree

BINARY_TREE_VERTICAL_TRAVERSAL_TEST_CASES = [
    ([3, 9, 20, None, None, 15, 7], [[9], [3, 15], [20], [7]]),
    ([1, 2, 3, 4, 5, 6, 7], [[4], [2], [1, 5, 6], [3], [7]]),
    ([1, 2, 3, 4, 6, 5, 7], [[4], [2], [1, 5, 6], [3], [7]]),
    (
        [100, 50, 200, 25, 75, 300, 10, 350, 15],
        [[350], [25], [50, 15], [100, 75, 300], [200], [10]],
    ),
    ([20, 40, 50, 90, 67, 94], [[90], [40], [20, 67, 94], [50]]),
    ([20, 40, 50, 90, 67, 94], [[90], [40], [20, 67, 94], [50]]),
    ([10, 23, 45, 25, 46], [[25], [23], [10, 46], [45]]),
    ([10, 23, 45, 25, 46], [[25], [23], [10, 46], [45]]),
    ([9, 7, None, None, 1, 8, 10, None, 12], [[7, 8], [9, 1, 12], [10]]),
    ([3, 2, 3, None, 3, None, 1], [[2], [3, 3], [3], [1]]),
]


class BinaryTreeVerticalTraversalTestCase(unittest.TestCase):
    @parameterized.expand(
        BINARY_TREE_VERTICAL_TRAVERSAL_TEST_CASES, name_func=custom_test_name_func
    )
    def test_vertical_traversal(self, data: list[int], expected: list[int]):
        binary_tree = BinaryTree.create_tree(data)
        actual = binary_tree.vertical_traversal()
        self.assertEqual(expected, actual)

    @parameterized.expand(
        BINARY_TREE_VERTICAL_TRAVERSAL_TEST_CASES, name_func=custom_test_name_func
    )
    def test_vertical_traversal_bfs(self, data: list[int], expected: list[int]):
        binary_tree = BinaryTree.create_tree(data)
        actual = binary_tree.vertical_traversal_bfs()
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
