import unittest
from random import randint

from datastructures.arrays.highest_rank import highest_rank


class HighestRankTestCases(unittest.TestCase):
    def test_should_return_12_for_nums_12_10_8_12_7_6_4_10_12(self):
        """Should return 12 for input of [12, 10, 8, 12, 7, 6, 4, 10, 12]"""
        nums = [12, 10, 8, 12, 7, 6, 4, 10, 12]
        expected = 12
        actual = highest_rank(nums)
        self.assertEqual(expected, actual)

    def test_should_return_12_for_nums_12_10_8_12_7_6_4_10_10(self):
        """Should return 10 for input of [12, 10, 8, 12, 7, 6, 4, 10, 10]"""
        nums = [12, 10, 8, 12, 7, 6, 4, 10, 10]
        expected = 10
        actual = highest_rank(nums)
        self.assertEqual(expected, actual)

    def test_should_return_12_for_nums_12_10_8_8_3_3_3_3_2_4_10_12_10(self):
        """Should return 3 for input of [12, 10, 8, 8, 3, 3, 3, 3, 2, 4, 10, 12, 10]"""
        nums = [12, 10, 8, 8, 3, 3, 3, 3, 2, 4, 10, 12, 10]
        expected = 3
        actual = highest_rank(nums)
        self.assertEqual(expected, actual)

    def test_random(self):
        """Random test cases"""
        for _ in range(100):
            arr = [randint(0, 50) for _ in range(randint(5, 25))]
            exp = sorted(arr, key=lambda k: (-{x: arr.count(x) for x in arr}[k], -k))[0]
            self.assertEqual(highest_rank(arr), exp)


if __name__ == '__main__':
    unittest.main()
