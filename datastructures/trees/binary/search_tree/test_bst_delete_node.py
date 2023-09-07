import unittest

from . import BinarySearchTree, BinaryTreeNode


class BinarySearchTreeDeleteNodeTestCases(unittest.TestCase):
    def test_1(self):
        """should delete key of 3 for tree = [5,3,6,2,4,null,7]"""
        left = BinaryTreeNode(3, left=BinaryTreeNode(2), right=BinaryTreeNode(4))
        right = BinaryTreeNode(6, right=BinaryTreeNode(7))
        root = BinaryTreeNode(5, left=left, right=right)
        search_tree = BinarySearchTree(root=root)

        actual = search_tree.delete_node(3)
        expected_root = BinaryTreeNode(5, left=BinaryTreeNode(4, left=BinaryTreeNode(2)),
                                       right=BinaryTreeNode(6, right=BinaryTreeNode(7)))

        self.assertEqual(expected_root.data, actual.data)
        self.assertEqual(expected_root.left.data, actual.left.data)
        self.assertEqual(expected_root.left.left.data, actual.left.left.data)
        self.assertEqual(expected_root.right.data, actual.right.data)
        self.assertEqual(expected_root.right.right.data, actual.right.right.data)

    def test_2(self):
        """should delete key of 0 for tree = [5,3,6,2,4,null,7] and return same root as tree has no key 0"""
        left = BinaryTreeNode(3, left=BinaryTreeNode(2), right=BinaryTreeNode(4))
        right = BinaryTreeNode(6, right=BinaryTreeNode(7))
        root = BinaryTreeNode(5, left=left, right=right)
        search_tree = BinarySearchTree(root=root)

        actual = search_tree.delete_node(0)

        self.assertEqual(search_tree.root, actual)

    def test_3(self):
        """should delete key of 0 for tree = [] and return same root as tree has no key 0 nor root"""
        search_tree = BinarySearchTree()

        actual = search_tree.delete_node(0)

        self.assertEqual(search_tree.root, actual)

    def test_4(self):
        """should delete key of 1 for tree = [1, null, 2] and return [2]"""
        root = BinaryTreeNode(1, right=BinaryTreeNode(2))
        search_tree = BinarySearchTree(root=root)

        actual = search_tree.delete_node(1)
        expected_root = BinaryTreeNode(2)

        self.assertEqual(expected_root.data, actual.data)


if __name__ == '__main__':
    unittest.main()
