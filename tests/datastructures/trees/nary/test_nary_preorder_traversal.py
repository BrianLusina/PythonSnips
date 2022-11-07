import unittest

from datastructures.trees import TreeNode
from datastructures.trees.nary import NAryTree


class NaryTreePreorderTestCases(unittest.TestCase):
    def test_one(self):
        """[1,null,3,2,4,null,5,6] should return [1,3,5,6,2,4]"""
        root = TreeNode(1)

        node3 = TreeNode(3)
        node2 = TreeNode(2)
        node4 = TreeNode(4)

        node5 = TreeNode(5)
        node6 = TreeNode(6)
        node3.children = [node5, node6]

        root.children = [node3, node2, node4]

        nary = NAryTree(root)
        actual = nary.pre_order_traversal()
        expected = [1, 3, 5, 6, 2, 4]
        self.assertEqual(expected, actual)

    def test_two(self):
        """[1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14] should return
        [1,2,3,6,7,11,14,4,8,12,5,9,13,10]"""
        root = TreeNode(1)

        node2 = TreeNode(2)
        node3 = TreeNode(3)
        node4 = TreeNode(4)
        node5 = TreeNode(5)

        node6 = TreeNode(6)
        node7 = TreeNode(7)

        node3.children = [node6, node7]

        node11 = TreeNode(11)
        node7.children = [node11]

        node14 = TreeNode(14)
        node11.children = [node14]

        node8 = TreeNode(8)
        node4.children = [node8]

        node12 = TreeNode(12)
        node8.children = [node12]

        node9 = TreeNode(9)
        node10 = TreeNode(10)
        node5.children = [node9, node10]

        node13 = TreeNode(13)
        node9.children = [node13]

        root.children = [node2, node3, node4, node5]

        nary = NAryTree(root)
        actual = nary.pre_order_traversal()
        expected = [1, 2, 3, 6, 7, 11, 14, 4, 8, 12, 5, 9, 13, 10]
        self.assertEqual(expected, actual)

    def test_three_with_duplicate_values(self):
        """[8,null,1,null,8,5] should return [8,1,8,5]"""
        root = TreeNode(8)

        node1 = TreeNode(1)
        root.children = [node1]

        node8 = TreeNode(8)
        node5 = TreeNode(5)
        node1.children = [node8, node5]

        nary = NAryTree(root)
        actual = nary.pre_order_traversal()
        expected = [8, 1, 8, 5]
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
