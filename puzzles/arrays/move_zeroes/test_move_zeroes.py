import unittest
from . import move_zeroes, move_zeroes_one


class MoveZeroesTestCase(unittest.TestCase):
    def test_0_1_0_3_12(self):
        """should modify nums = [0, 1, 0, 3, 12] in place to [1,3,12,0,0]"""
        nums = [0, 1, 0, 3, 12]
        expected = [1, 3, 12, 0, 0]
        move_zeroes(nums)
        self.assertEqual(expected, nums)

    def test_0(self):
        """should modify nums = [0] in place to [0]"""
        nums = [0]
        expected = [0]
        move_zeroes(nums)
        self.assertEqual(expected, nums)

    def test_1_0(self):
        """should modify nums = [1, 0] in place to [1, 0]"""
        nums = [1, 0]
        expected = [1, 0]
        move_zeroes(nums)
        self.assertEqual(expected, nums)


class MoveZeroesOneTestCase(unittest.TestCase):
    def test_0_1_0_3_12(self):
        """should modify nums = [0, 1, 0, 3, 12] in place to [1,3,12,0,0]"""
        nums = [0, 1, 0, 3, 12]
        expected = [1, 3, 12, 0, 0]
        move_zeroes_one(nums)
        self.assertEqual(expected, nums)

    def test_0(self):
        """should modify nums = [0] in place to [0]"""
        nums = [0]
        expected = [0]
        move_zeroes_one(nums)
        self.assertEqual(expected, nums)

    def test_1_0(self):
        """should modify nums = [1, 0] in place to [1, 0]"""
        nums = [1, 0]
        expected = [1, 0]
        move_zeroes_one(nums)
        self.assertEqual(expected, nums)


if __name__ == "__main__":
    unittest.main()
