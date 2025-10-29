import unittest
from datastructures.trees.binary.search_tree import BinaryTreeNode
from . import find_closest_value_in_bst


class FindClosestValueTestCases(unittest.TestCase):
    def test_something(self):
        root = BinaryTreeNode(
            data=10,
            left=BinaryTreeNode(data=5,
                                left=BinaryTreeNode(
                                    data=2,
                                    left=BinaryTreeNode(data=1),
                                    right=BinaryTreeNode(data=5))
                                ),
            right=BinaryTreeNode(data=15,
                                 left=BinaryTreeNode(
                                     data=13,
                                     right=BinaryTreeNode(
                                         data=14,
                                         right=BinaryTreeNode(data=22)
                                     )
                                 ))
        )
        expected = 13
        actual = find_closest_value_in_bst(root, target=12)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
