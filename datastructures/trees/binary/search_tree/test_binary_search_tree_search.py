import unittest

from . import BinarySearchTree


class BinarySearchTreeSearchTestCases(unittest.TestCase):
    def test_1(self):
        """should return true when searching for 10 in tree = [8,3,10,1,6]"""
        data = [8, 3, 10, 1, 6]
        search_tree = BinarySearchTree()

        for d in data:
            search_tree.insert_node(d)

        expected = search_tree.search_node(10)

        self.assertTrue(expected)


if __name__ == "__main__":
    unittest.main()
