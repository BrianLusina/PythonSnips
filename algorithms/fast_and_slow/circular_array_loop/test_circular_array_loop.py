import unittest
from . import circular_array_loop


class CircularArrayLoopTestCase(unittest.TestCase):
    def test_1(self):
        """should return True for [3,1,2]"""
        nums = [3,1,2]
        actual = circular_array_loop(nums)
        self.assertTrue(actual)

    def test_2(self):
        """should return True for [-2, -1, -3]"""
        nums = [-2, -1, -3]
        actual = circular_array_loop(nums)
        self.assertTrue(actual)

    def test_3(self):
        """should return False for [2,1,-1,-2]"""
        nums = [2,1,-1,-2]
        actual = circular_array_loop(nums)
        self.assertFalse(actual)

    def test_4(self):
        """should return True for [3,-3,1,1]"""
        nums = [3,-3,1,1]
        actual = circular_array_loop(nums)
        self.assertTrue(actual)

    def test_5(self):
        """should return True for [1,3,-2,-4,1]"""
        nums = [1,3,-2,-4,1]
        actual = circular_array_loop(nums)
        self.assertTrue(actual)

    def test_6(self):
        """should return True for [2,1,-1,-2]"""
        nums = [2,1,-1,-2]
        actual = circular_array_loop(nums)
        self.assertFalse(actual)

    def test_7(self):
        """should return True for [5,4,-2,-1,3]"""
        nums = [5,4,-2,-1,3]
        actual = circular_array_loop(nums)
        self.assertFalse(actual)

    def test_8(self):
        """should return True for [1,2,-3,3,4,7,1]"""
        nums = [1,2,-3,3,4,7,1]
        actual = circular_array_loop(nums)
        self.assertTrue(actual)

    def test_9(self):
        """should return True for [3,3,1,-1,2]"""
        nums = [3,3,1,-1,2]
        actual = circular_array_loop(nums)
        self.assertTrue(actual)


if __name__ == '__main__':
    unittest.main()
