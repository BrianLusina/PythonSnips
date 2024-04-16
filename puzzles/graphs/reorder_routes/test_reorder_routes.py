import unittest
from . import Solution


class ReorderRoutesTestCase(unittest.TestCase):
    def test_1(self):
        """should return 3 from input n = 6, connections = [[0,1],[1,3],[2,3],[4,0],[4,5]]"""
        connections = [[0, 1], [1, 3], [2, 3], [4, 0], [4, 5]]
        n = 6
        expected = 3
        actual = Solution().min_reorder(n, connections)
        self.assertEqual(expected, actual)

    def test_2(self):
        """should return 2 from input n = 5, connections = [[1,0],[1,2],[3,2],[3,4]]"""
        connections = [[1, 0], [1, 2], [3, 2], [3, 4]]
        n = 5
        expected = 2
        actual = Solution().min_reorder(n, connections)
        self.assertEqual(expected, actual)

    def test_3(self):
        """should return 0 from input n = 3, connections = [[1,0],[2,0]]"""
        connections = [[1, 0], [2, 0]]
        n = 3
        expected = 0
        actual = Solution().min_reorder(n, connections)
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
