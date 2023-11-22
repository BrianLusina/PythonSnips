import unittest

from . import single_number, single_number_math


class SingleNumberTestCase(unittest.TestCase):
    def test_1(self):
        """should return 1 from nums = [2,2,1]"""
        nums = [2, 2, 1]
        expected = 1
        actual = single_number(nums)
        self.assertEqual(expected, actual)

    def test_2(self):
        """should return 1 from nums = [4,1,2,1,2]"""
        nums = [4, 1, 2, 1, 2]
        expected = 4
        actual = single_number(nums)
        self.assertEqual(expected, actual)

    def test_3(self):
        """should return 1 from nums = [1]"""
        nums = [1]
        expected = 1
        actual = single_number(nums)
        self.assertEqual(expected, actual)


class SingleNumberMathTestCase(unittest.TestCase):
    def test_1(self):
        """should return 1 from nums = [2,2,1]"""
        nums = [2, 2, 1]
        expected = 1
        actual = single_number_math(nums)
        self.assertEqual(expected, actual)

    def test_2(self):
        """should return 1 from nums = [4,1,2,1,2]"""
        nums = [4, 1, 2, 1, 2]
        expected = 4
        actual = single_number_math(nums)
        self.assertEqual(expected, actual)

    def test_3(self):
        """should return 1 from nums = [1]"""
        nums = [1]
        expected = 1
        actual = single_number_math(nums)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
