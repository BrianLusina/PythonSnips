import unittest

from . import next_greater


class NextGreaterTestCase(unittest.TestCase):
    def test_1(self):
        """should return [5, 10, 10, -1] from an input [4, 5, 2, 10]"""
        nums = [4, 5, 2, 10]
        expected = [5, 10, 10, -1]
        actual = next_greater(nums)
        self.assertEqual(expected, actual)

    def test_2(self):
        """should return [-1, -1, -1] from an input [3, 2, 1]"""
        nums = [3, 2, 1]
        expected = [-1, -1, -1]
        actual = next_greater(nums)
        self.assertEqual(expected, actual)

    def test_3(self):
        """should return [-1, -1, -1] from an input [4, 5, 2, 25]"""
        nums = [4, 5, 2, 25]
        expected = [5, 25, 25, -1]
        actual = next_greater(nums)
        self.assertEqual(expected, actual)

    def test_4(self):
        """should return [-1, 12, 12, -1] from an input [13, 7, 6, 12 ]"""
        nums = [13, 7, 6, 12]
        expected = [-1, 12, 12, -1]
        actual = next_greater(nums)
        self.assertEqual(expected, actual)

    def test_5(self):
        """should return [-1] from an input [1]"""
        nums = [1]
        expected = [-1]
        actual = next_greater(nums)
        self.assertEqual(expected, actual)

    def test_6(self):
        """should return [35 42 42 -1 28 39 -1 28 -1] from an input [34, 35, 27, 42, 5, 28, 39, 20, 28]"""
        nums = [34, 35, 27, 42, 5, 28, 39, 20, 28]
        expected = [35, 42, 42, -1, 28, 39, -1, 28, -1]
        actual = next_greater(nums)
        self.assertEqual(expected, actual)

    def test_7(self):
        """should return [13, 21,-1,-1] from an input [11, 13, 21, 3]"""
        nums = [11, 13, 21, 3]
        expected = [13, 21, -1, -1]
        actual = next_greater(nums)
        self.assertEqual(expected, actual)

    def test_8(self):
        """should return [8 -1 1 3 -1 ] from an input [6, 8, 0, 1, 3]"""
        nums = [6, 8, 0, 1, 3]
        expected = [8, -1, 1, 3, -1]
        actual = next_greater(nums)
        self.assertEqual(expected, actual)

    def test_9(self):
        """should return [8 -1 6 2 6 7 -1 -1] from an input [3, 8, 4, 1, 2, 6, 7, 2]"""
        nums = [3, 8, 4, 1, 2, 6, 7, 2]
        expected = [8, -1, 6, 2, 6, 7, -1, -1]
        actual = next_greater(nums)
        self.assertEqual(expected, actual)

    def test_10(self):
        """should return [3 4 4 -1] from an input [1, 3, 2, 4]"""
        nums = [1, 3, 2, 4]
        expected = [3, 4, 4, -1]
        actual = next_greater(nums)
        self.assertEqual(expected, actual)

    def test_11(self):
        """should return [3 4 4 -1] from an input [7 8 1 4]"""
        nums = [7, 8, 1, 4]
        expected = [8, -1, 4, -1]
        actual = next_greater(nums)
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
