import unittest

from . import BinarySearchTree, BinaryTreeNode


class BinarySearchTreeInsertNodeTestCases(unittest.TestCase):
    def test_1(self):
        """should insert nodes in tree = [8,3,10,1,6]"""
        data = [8, 3, 10, 1, 6]
        search_tree = BinarySearchTree()

        for d in data:
            search_tree.insert_node(d)

        expected_root = BinaryTreeNode(
            data=8,
            left=BinaryTreeNode(
                data=3,
                left=BinaryTreeNode(data=1),
                right=BinaryTreeNode(data=6)
            ),
            right=BinaryTreeNode(data=10),
        )

        self.assertEqual(expected_root.data, search_tree.root.data)
        self.assertEqual(expected_root.left.data, search_tree.root.left.data)
        self.assertEqual(expected_root.right.data, search_tree.root.right.data)
        self.assertEqual(expected_root.left.left.data, search_tree.root.left.left.data)
        self.assertEqual(expected_root.left.right.data, search_tree.root.left.right.data)


if __name__ == "__main__":
    unittest.main()
