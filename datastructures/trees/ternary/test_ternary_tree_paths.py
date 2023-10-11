import unittest
from . import TernaryTree
from .node import TernaryTreeNode


class TernaryTreeTestCase(unittest.TestCase):
    def test_1(self):
        """root(1, children=[(2, children=[3]), 4, 6]) should return ["1->2->3", "1->4", "1->6"]"""
        root = TernaryTreeNode(data=1, children=[TernaryTreeNode(2, children=[TernaryTreeNode(3)]), TernaryTreeNode(4),
                                                 TernaryTreeNode(6)])
        ternary_tree = TernaryTree(root)
        actual = ternary_tree.paths()
        expected = ["1->2->3", "1->4", "1->6"]
        self.assertEqual(expected, actual)

    def test_2(self):
        """root(1, children=[(2, children=[3, 4, 7]), 5, 6]) should return [1->2->3,1->2->4,1->2->7,1->5,1->6]"""

        root_left = TernaryTreeNode(2, children=[TernaryTreeNode(3), TernaryTreeNode(4), TernaryTreeNode(7)])
        root_middle = TernaryTreeNode(5)
        root_right = TernaryTreeNode(6)

        root_children = [root_left, root_middle, root_right]
        root = TernaryTreeNode(data=1, children=root_children)

        ternary_tree = TernaryTree(root)
        actual = ternary_tree.paths()
        expected = ["1->2->3", "1->2->4", "1->2->7", "1->5", "1->6"]
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
