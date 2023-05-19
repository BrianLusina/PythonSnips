import unittest

from . import BinaryTree, BinaryTreeNode


class BinaryTreeTestCase(unittest.TestCase):
    def test_something(self):
        self.assertFalse(False)


class BinaryTreeIsFullTestCases(unittest.TestCase):
    def test_returns_false_for_no_root(self):
        tree = BinaryTree()
        actual = tree.is_full()

        self.assertFalse(actual)

    def test_returns_true_for_root_with_no_left_nor_right(self):
        root = BinaryTreeNode(1)
        tree = BinaryTree(root=root)
        actual = tree.is_full()

        self.assertTrue(actual)

    def test_returns_true_for_root_with_1_left_and_1_right(self):
        root = BinaryTreeNode(1)
        left = BinaryTreeNode(2)
        right = BinaryTreeNode(3)
        root.left = left
        root.right = right

        tree = BinaryTree(root=root)
        actual = tree.is_full()

        self.assertTrue(actual)

    def test_returns_false_for_tree_with_0_left_and_1_right(self):
        root = BinaryTreeNode(1)
        right = BinaryTreeNode(3)
        root.right = right

        tree = BinaryTree(root=root)
        actual = tree.is_full()

        self.assertFalse(actual)


if __name__ == '__main__':
    unittest.main()
