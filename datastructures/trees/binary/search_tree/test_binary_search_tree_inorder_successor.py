import unittest
from typing import List, Optional
from parameterized import parameterized
from datastructures.trees.binary.search_tree import BinarySearchTree
from datastructures.trees.binary.node import BinaryTreeNode


class BinarySearchTreeInorderSuccessorTestCase(unittest.TestCase):
    @parameterized.expand(
        [
            ([18, 12, 22, 19, 26, 10, 14, 13, 15], 19, 22),
            ([50, 30, 70, 20, 40, 60, 80, 10, 25, 35, 45, 55, 65, 75, 85], 55, 60),
            ([2], 2, None),
            ([10, 8], 10, None),
            ([23, 21, 24, None, 22, None, None], 21, 22),
            ([3, 1, 5, None, 2, None, None], 1, 2),
        ]
    )
    def test_inorder_successor(
        self, data: List[int], p: int, expected_value: Optional[int]
    ):
        tree = BinarySearchTree()
        for d in data:
            tree.insert_node(d)

        node = BinaryTreeNode(p)
        expected = None if not expected_value else BinaryTreeNode(expected_value)
        actual = tree.inorder_successor(node)

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
