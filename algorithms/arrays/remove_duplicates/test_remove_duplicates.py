import unittest

from . import remove_duplicates_from_sorted_list, remove_duplicates_two


class RemoveDuplicateTestCase(unittest.TestCase):
    def test_1(self):
        """nums = [1,1,2] should return 2"""
        nums = [1, 1, 2]
        actual = remove_duplicates_from_sorted_list(nums)
        expected = 2

        self.assertEqual(expected, actual)

    def test_2(self):
        """nums = [1, 2, 2, 3, 3] should return 3"""
        nums = [1, 2, 2, 3, 3]
        actual = remove_duplicates_from_sorted_list(nums)
        expected = 3

        self.assertEqual(expected, actual)

    def test_3(self):
        """nums = [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
        1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3,
        3 ] should return 4"""
        nums = [
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            1,
            2,
            2,
            2,
            2,
            2,
            2,
            2,
            2,
            2,
            2,
            2,
            2,
            3,
            3,
            3,
            3,
            3,
            3,
            3,
            3,
            3,
            3,
            3,
            3,
            3,
            3,
            3,
            3,
            3,
            3,
            3,
            3,
            3,
            3,
        ]
        actual = remove_duplicates_from_sorted_list(nums)
        expected = 4

        self.assertEqual(expected, actual)


class RemoveDuplicatesTwoTestCase(unittest.TestCase):
    def test_1(self):
        """nums = [1,1,1,2,2,3] should return 5"""
        nums = [1, 1, 1, 2, 2, 3]
        expected = 5
        actual = remove_duplicates_two(nums)

        self.assertEqual(expected, actual)

    def test_2(self):
        """nums = [0,0,1,1,1,1,2,3,3] should return 7"""
        nums = [0, 0, 1, 1, 1, 1, 2, 3, 3]
        expected = 7
        actual = remove_duplicates_two(nums)

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
