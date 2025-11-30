import unittest
from datastructures.trees.binary.tree.binary_tree import BinaryTree
from datastructures.trees.binary.node import BinaryTreeNode


class MinCameraCoverTestCase(unittest.TestCase):
    def test_1(self):
        right = BinaryTreeNode(
            data=0, right=BinaryTreeNode(data=0), left=BinaryTreeNode(data=0)
        )
        root = BinaryTreeNode(data=0, right=right)
        tree = BinaryTree(root)
        actual = tree.min_camera_cover()
        expected = 1
        self.assertEqual(expected, actual)

    def test_2(self):
        root = BinaryTreeNode(data=0)
        tree = BinaryTree(root)
        actual = tree.min_camera_cover()
        expected = 1
        self.assertEqual(expected, actual)

    def test_3(self):
        right = BinaryTreeNode(
            data=0, right=BinaryTreeNode(data=0), left=BinaryTreeNode(data=0)
        )
        left = BinaryTreeNode(
            data=0, right=BinaryTreeNode(data=0), left=BinaryTreeNode(data=0)
        )
        root = BinaryTreeNode(data=0, right=right, left=left)
        tree = BinaryTree(root)
        actual = tree.min_camera_cover()
        expected = 2
        self.assertEqual(expected, actual)

    def test_4(self):
        left = BinaryTreeNode(data=0, left=BinaryTreeNode(data=0))
        root = BinaryTreeNode(data=0, left=left)
        tree = BinaryTree(root)
        actual = tree.min_camera_cover()
        expected = 1
        self.assertEqual(expected, actual)

    def test_5(self):
        left = BinaryTreeNode(
            data=0,
            right=BinaryTreeNode(
                data=0, left=BinaryTreeNode(data=0, right=BinaryTreeNode(data=0))
            ),
        )
        root = BinaryTreeNode(data=0, left=left)
        tree = BinaryTree(root)
        actual = tree.min_camera_cover()
        expected = 2
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
