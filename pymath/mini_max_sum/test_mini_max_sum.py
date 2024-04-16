import unittest

from pymath.mini_max_sum import mini_max_sum


class MiniMaxSumTestCases(unittest.TestCase):
    def test_1_3_5_7_9_returns_16_24(self):
        """arr = [1,3,5,7,9] should return [16, 24]"""
        arr = [1, 3, 5, 7, 9]
        expected = [16, 24]
        actual = mini_max_sum(arr)
        self.assertEqual(expected, actual)

    def test_1_2_3_4_5returns_10_14(self):
        """arr = [1,2,3,4,5] should return [10, 14]"""
        arr = [1, 2, 3, 4, 5]
        expected = [10, 14]
        actual = mini_max_sum(arr)
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
