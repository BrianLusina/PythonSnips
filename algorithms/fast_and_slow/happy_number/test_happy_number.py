import unittest
from . import is_happy_number, is_happy_number_2


class HappyNumberTestCase(unittest.TestCase):
    def test_1(self):
        """should return true for 23"""
        number = 23
        actual = is_happy_number(number)
        self.assertTrue(actual)

    def test_2(self):
        """should return false for 2"""
        number = 2
        actual = is_happy_number(number)
        self.assertFalse(actual)

    def test_3(self):
        """should return true for 19"""
        number = 19
        actual = is_happy_number(number)
        self.assertTrue(actual)

    def test_4(self):
        """should return false for 2147483646"""
        number = 2147483646
        actual = is_happy_number(number)
        self.assertFalse(actual)

    def test_5(self):
        """should return true for 1"""
        number = 1
        actual = is_happy_number(number)
        self.assertTrue(actual)

    def test_6(self):
        """should return true for 8"""
        number = 8
        actual = is_happy_number(number)
        self.assertFalse(actual)

    def test_7(self):
        """should return true for 7"""
        number = 7
        actual = is_happy_number(number)
        self.assertTrue(actual)

    def test_8(self):
        """should return false for 5"""
        number = 5
        actual = is_happy_number(number)
        self.assertFalse(actual)

    def test_9(self):
        """should return false for 25"""
        number = 25
        actual = is_happy_number(number)
        self.assertFalse(actual)


class HappyNumberTestCase2(unittest.TestCase):
    def test_1(self):
        """should return true for 23"""
        number = 23
        actual = is_happy_number_2(number)
        self.assertTrue(actual)

    def test_2(self):
        """should return false for 2"""
        number = 2
        actual = is_happy_number_2(number)
        self.assertFalse(actual)

    def test_3(self):
        """should return true for 19"""
        number = 19
        actual = is_happy_number_2(number)
        self.assertTrue(actual)

    def test_4(self):
        """should return false for 2147483646"""
        number = 2147483646
        actual = is_happy_number_2(number)
        self.assertFalse(actual)

    def test_5(self):
        """should return true for 1"""
        number = 1
        actual = is_happy_number_2(number)
        self.assertTrue(actual)

    def test_6(self):
        """should return true for 8"""
        number = 8
        actual = is_happy_number_2(number)
        self.assertFalse(actual)

    def test_7(self):
        """should return true for 7"""
        number = 7
        actual = is_happy_number_2(number)
        self.assertTrue(actual)

    def test_8(self):
        """should return false for 5"""
        number = 5
        actual = is_happy_number_2(number)
        self.assertFalse(actual)

    def test_9(self):
        """should return false for 25"""
        number = 25
        actual = is_happy_number_2(number)
        self.assertFalse(actual)


if __name__ == "__main__":
    unittest.main()
