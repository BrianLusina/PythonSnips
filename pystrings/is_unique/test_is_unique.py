import unittest
from . import is_unique


class IsUniqueTestCases(unittest.TestCase):

    def test_1(self):
        """should return true for abCDefGh"""
        input_string = "abCDefGh"
        actual = is_unique(input_string)
        self.assertTrue(actual)

    def test_2(self):
        """should return false for nonunique"""
        input_string = "nonunique"
        actual = is_unique(input_string)
        self.assertFalse(actual)

    def test_3(self):
        """should return true for abCedFghI"""
        input_string = "abCedFghI"
        actual = is_unique(input_string)
        self.assertTrue(actual)

    def test_4(self):
        """should return false for I Am Not Unique"""
        input_string = "I Am Not Unique"
        actual = is_unique(input_string)
        self.assertFalse(actual)

    def test_5(self):
        """should return False for heythere"""
        input_string = "heythere"
        actual = is_unique(input_string)
        self.assertFalse(actual)

    def test_6(self):
        """should return True for hi"""
        input_string = "hi"
        actual = is_unique(input_string)
        self.assertTrue(actual,)


if __name__ == '__main__':
    unittest.main()
