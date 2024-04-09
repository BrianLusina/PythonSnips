import unittest

from datastructures.arrays.lonely_integer import lonely_integer


class LonelyIntegerTestCases(unittest.TestCase):
    def test_1_2_3_4_3_2_1_returns_4(self):
        """a = [1,2,3,4,3,2,1] returns 4"""
        a = [1, 2, 3, 4, 3, 2, 1]
        expected = 4
        actual = lonely_integer(a)
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
