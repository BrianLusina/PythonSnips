import unittest
from . import int_to_str


class IntToStrTestCase(unittest.TestCase):
    def test_1(self):
        """should return '123' for 123"""
        input_int = 123
        expected = "123"
        actual = int_to_str(input_int)
        self.assertEqual(expected, actual)

    def test_2(self):
        """should return '12332' for 12332"""
        input_int = 12332
        expected = "12332"
        actual = int_to_str(input_int)
        self.assertEqual(expected, actual)

    def test_3(self):
        """should return '554' for 554"""
        input_int = 554
        expected = "554"
        actual = int_to_str(input_int)
        self.assertEqual(expected, actual)

    def test_4(self):
        """should return '-554' for -554"""
        input_int = -554
        expected = "-554"
        actual = int_to_str(input_int)
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
