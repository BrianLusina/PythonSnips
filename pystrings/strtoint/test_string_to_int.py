import unittest
from . import str_to_int, str_to_int_v2


class StrToIntTestCases(unittest.TestCase):
    def test_1(self):
        """should convert '123' to 123"""
        input_str = "123"
        expected = 123
        actual = str_to_int(input_str)
        self.assertEqual(expected, actual)

    def test_2(self):
        """should convert '-12332' to -12332"""
        input_str = "-12332"
        expected = -12332
        actual = str_to_int(input_str)
        self.assertEqual(expected, actual)

    def test_3(self):
        """should convert '554' to 554"""
        input_str = "554"
        expected = 554
        actual = str_to_int(input_str)
        self.assertEqual(expected, actual)

    def test_4(self):
        """should convert '0' to 0"""
        input_str = "0"
        expected = 0
        actual = str_to_int(input_str)
        self.assertEqual(expected, actual)

    def test_5(self):
        """should convert '-1293' to -1293"""
        input_str = "-1293"
        expected = -1293
        actual = str_to_int(input_str)
        self.assertEqual(expected, actual)

    def test_6(self):
        """should convert '529' to 529"""
        input_str = "529"
        expected = 529
        actual = str_to_int(input_str)
        self.assertEqual(expected, actual)

    def test_7(self):
        """should convert '-999' to -999"""
        input_str = "-999"
        expected = -999
        actual = str_to_int(input_str)
        self.assertEqual(expected, actual)


class StrToIntV2TestCases(unittest.TestCase):
    def test_1(self):
        """should convert '123' to 123"""
        input_str = "123"
        expected = 123
        actual = str_to_int_v2(input_str)
        self.assertEqual(expected, actual)

    def test_2(self):
        """should convert '-12332' to -12332"""
        input_str = "-12332"
        expected = -12332
        actual = str_to_int_v2(input_str)
        self.assertEqual(expected, actual)

    def test_3(self):
        """should convert '554' to 554"""
        input_str = "554"
        expected = 554
        actual = str_to_int_v2(input_str)
        self.assertEqual(expected, actual)

    def test_4(self):
        """should convert '0' to 0"""
        input_str = "0"
        expected = 0
        actual = str_to_int_v2(input_str)
        self.assertEqual(expected, actual)

    def test_5(self):
        """should convert '-1293' to -1293"""
        input_str = "-1293"
        expected = -1293
        actual = str_to_int_v2(input_str)
        self.assertEqual(expected, actual)

    def test_6(self):
        """should convert '529' to 529"""
        input_str = "529"
        expected = 529
        actual = str_to_int_v2(input_str)
        self.assertEqual(expected, actual)

    def test_7(self):
        """should convert '-999' to -999"""
        input_str = "-999"
        expected = -999
        actual = str_to_int_v2(input_str)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
