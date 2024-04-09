import unittest

from pymath.plus_minus import plus_minus


class PlusMinusTestCases(unittest.TestCase):
    def test_1_1_0_negative_1_negative_1(self):
        """arr = [1,1,0,-1,-1] should return [0.400000, 0.400000, 0.200000]"""
        arr = [1, 1, 0, -1, -1]
        expected = [0.400000, 0.400000, 0.200000]
        actual = plus_minus(arr)
        self.assertEqual(expected, actual)

    def test_negative_4_3_negative_9_0_4_1(self):
        """arr = [-4, 3, -9, 0, 4, 1] should return [0.500000, 0.333333, 0.166667]"""
        arr = [-4, 3, -9, 0, 4, 1]
        expected = [0.500000, 0.333333, 0.166667]
        actual = plus_minus(arr)
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
