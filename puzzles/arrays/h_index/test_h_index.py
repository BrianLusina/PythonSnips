import unittest
from . import h_index


class HIndexTestCase(unittest.TestCase):
    def test_1(self):
        """citations = [3,0,6,1,5] should return 3"""
        citations = [3, 0, 6, 1, 5]
        expected = 3
        actual = h_index(citations)
        self.assertEqual(expected, actual)

    def test_2(self):
        """citations = [1,3,1] should return 1"""
        citations = [1, 3, 1]
        expected = 1
        actual = h_index(citations)
        self.assertEqual(expected, actual)

    def test_3(self):
        """citations = [9, 7, 6, 2, 1] should return 3"""
        citations = [9, 7, 6, 2, 1]
        expected = 3
        actual = h_index(citations)
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
