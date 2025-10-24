import unittest

from . import can_jump, jump


class CanJumpTestCase(unittest.TestCase):
    def test_1(self):
        """nums = [2,3,1,1,4] should return true"""
        nums = [2, 3, 1, 1, 4]
        actual = can_jump(nums)
        self.assertTrue(actual)

    def test_2(self):
        """nums = [3,2,1,0,4] should return false"""
        nums = [3, 2, 1, 0, 4]
        actual = can_jump(nums)
        self.assertFalse(actual)

    def test_3(self):
        """nums = [2, 3, 0, 1, 4] should return true"""
        nums = [2, 3, 0, 1, 4]
        actual = can_jump(nums)
        self.assertTrue(actual)


class JumpTestCase(unittest.TestCase):
    def test_1(self):
        """nums = [2,3,1,1,4] should return 2"""
        nums = [2, 3, 1, 1, 4]
        actual = jump(nums)
        expected = 2
        self.assertEqual(expected, actual)

    def test_3(self):
        """nums = [2, 3, 0, 1, 4] should return 2"""
        nums = [2, 3, 0, 1, 4]
        actual = jump(nums)
        expected = 2
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
