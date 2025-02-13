import unittest

from . import find_duplicate, find_duplicate_floyd_algo


class FindDuplicateTestCases(unittest.TestCase):
    def test_1(self):
        """nums = [3, 4, 1, 4, 2] should return 4"""
        nums = [3, 4, 1, 4, 2]
        expected = 4
        actual = find_duplicate(nums)

        self.assertEqual(expected, actual)

    def test_2(self):
        """nums = [1, 2, 3] should return -1"""
        nums = [1, 2, 3]
        expected = -1
        actual = find_duplicate(nums)

        self.assertEqual(expected, actual)

    def test_3(self):
        """nums = [3, 4, 1, 4, 1] should return 1 or 4"""
        nums = [3, 4, 1, 4, 1]
        expected_1 = 1
        expected_4 = 4

        actual = find_duplicate(nums)

        self.assertIn(actual, [expected_1, expected_4])


class FindDuplicateWithFastAndSlowPointersTestCases(unittest.TestCase):
    def test_1(self):
        """nums = [3, 4, 1, 4, 2] should return 4"""
        nums = [3, 4, 1, 4, 2]
        expected = 4
        actual = find_duplicate_floyd_algo(nums)

        self.assertEqual(expected, actual)

    # @unittest.skip("Failing due to IndexError. Needs further investigation")
    def test_2(self):
        """nums = [1, 2, 3] should return -1"""
        nums = [1, 2, 3]
        expected = -1
        actual = find_duplicate_floyd_algo(nums)

        self.assertEqual(expected, actual)

    def test_3(self):
        """nums = [3, 4, 1, 4, 1] should return 1 or 4"""
        nums = [3, 4, 1, 4, 1]
        expected_1 = 1
        expected_4 = 4

        actual = find_duplicate_floyd_algo(nums)

        self.assertIn(actual, [expected_1, expected_4])

    def test_4(self):
        """nums = [1, 3, 3, 4, 2, 5] should return 3"""
        nums = [1, 3, 3, 4, 2, 5]
        expected = 3

        actual = find_duplicate_floyd_algo(nums)

        self.assertEqual(actual, expected)

    def test_5(self):
        """nums = [1, 5, 3, 4, 2, 5] should return 5"""
        nums = [1, 5, 3, 4, 2, 5]
        expected = 5

        actual = find_duplicate_floyd_algo(nums)

        self.assertEqual(actual, expected)

    def test_6(self):
        """nums = [1, 2, 3, 4, 5, 6, 6, 7] should return 6"""
        nums = [1, 2, 3, 4, 5, 6, 6, 7]
        expected = 6

        actual = find_duplicate_floyd_algo(nums)

        self.assertEqual(actual, expected)

    def test_7(self):
        """nums = [4, 6, 7, 7, 3, 5, 2, 8, 1] should return 7"""
        nums = [4, 6, 7, 7, 3, 5, 2, 8, 1]
        expected = 7

        actual = find_duplicate_floyd_algo(nums)

        self.assertEqual(actual, expected)

    def test_8(self):
        """nums = [9, 8, 7, 6, 2, 3, 5, 4, 1, 9] should return 9"""
        nums = [9, 8, 7, 6, 2, 3, 5, 4, 1, 9]
        expected = 9

        actual = find_duplicate_floyd_algo(nums)

        self.assertEqual(actual, expected)

    def test_9(self):
        """nums = [3, 4, 4, 4, 2] should return 4"""
        nums = [3, 4, 4, 4, 2]
        expected = 4

        actual = find_duplicate_floyd_algo(nums)

        self.assertEqual(actual, expected)

    def test_10(self):
        """nums = [1, 1] should return 1"""
        nums = [1, 1]
        expected = 1

        actual = find_duplicate_floyd_algo(nums)

        self.assertEqual(actual, expected)

    def test_11(self):
        """nums = [1,3,4,2,2] should return 2"""
        nums = [1,3,4,2,2]
        expected = 2

        actual = find_duplicate_floyd_algo(nums)

        self.assertEqual(actual, expected)

    def test_12(self):
        """nums = [1,3,6,2,7,3,5,4] should return 3"""
        nums = [1,3,6,2,7,3,5,4]
        expected = 3

        actual = find_duplicate_floyd_algo(nums)

        self.assertEqual(actual, expected)

    def test_13(self):
        """nums = [1,2,2] should return 2"""
        nums = [1,2,2]
        expected = 2

        actual = find_duplicate_floyd_algo(nums)

        self.assertEqual(actual, expected)


if __name__ == "__main__":
    unittest.main()
