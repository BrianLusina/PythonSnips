import unittest
from . import num_tilings


class NumTilingsTestCase(unittest.TestCase):
    def test_1(self):
        """should return 5 for n = 3"""
        n = 3
        expected = 5
        actual = num_tilings(n)
        self.assertEqual(expected, actual)

    def test_2(self):
        """should return 1 for n = 1"""
        n = 1
        expected = 1
        actual = num_tilings(n)
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
