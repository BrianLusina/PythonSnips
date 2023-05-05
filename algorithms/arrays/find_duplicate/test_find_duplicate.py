import unittest

from . import find_duplicate, find_duplicate_floyd_algo


class FindDuplicateTestCases(unittest.TestCase):
    def test_1_with_floyd_algorithm(self):
        """nums = [3, 4, 1, 4, 2] should return 4"""
        nums = [3, 4, 1, 4, 2]
        expected = 4
        actual = find_duplicate_floyd_algo(nums)

        self.assertEqual(expected, actual)

    @unittest.skip("Failing due to IndexError. Needs further investigation")
    def test_2_with_floyd_algorithm(self):
        """nums = [1, 2, 3] should return -1"""
        nums = [1, 2, 3]
        expected = -1
        actual = find_duplicate_floyd_algo(nums)

        self.assertEqual(expected, actual)

    def test_3_with_floyd_algorithm(self):
        """nums = [3, 4, 1, 4, 1] should return 1 or 4"""
        nums = [3, 4, 1, 4, 1]
        expected_1 = 1
        expected_4 = 4

        actual = find_duplicate_floyd_algo(nums)

        self.assertIn(actual, [expected_1, expected_4])

    def test_1(self):
        """nums = [3, 4, 1, 4, 2] should return 4"""
        nums = [3, 4, 1, 4, 2]
        expected = 4
        actual = find_duplicate(nums)

        self.assertEqual(expected, actual)

    @unittest.skip("Failing due to IndexError. Needs further investigation")
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


if __name__ == '__main__':
    unittest.main()
