import unittest
from datastructures.arrays.dynamic_array import dynamic_array


class DynamicArrayTestCases(unittest.TestCase):
    def test_one(self):
        """should return [7,3] for input of n=2, queries=[[1,0,5], [1, 1, 7], [1, 0, 3],[2, 1, 0],[2, 1, 1]]"""
        expected = [7, 3]
        n = 2
        queries = [[1, 0, 5], [1, 1, 7], [1, 0, 3], [2, 1, 0], [2, 1, 1]]
        actual = dynamic_array(n, queries)

        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
