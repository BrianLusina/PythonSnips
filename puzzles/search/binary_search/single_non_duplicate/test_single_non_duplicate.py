import unittest
from . import single_non_duplicate


class SingleNonDuplicateTestCase(unittest.TestCase):
    def test_1(self):
        """should return 2 for [1,1,2,3,3,4,4,8,8]"""
        nums = [1, 1, 2, 3, 3, 4, 4, 8, 8]
        expected = 2
        actual = single_non_duplicate(nums)
        self.assertEqual(expected, actual)

    def test_2(self):
        """should return 10 for [3,3,7,7,10,11,11]"""
        nums = [3, 3, 7, 7, 10, 11, 11]
        expected = 10
        actual = single_non_duplicate(nums)
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
