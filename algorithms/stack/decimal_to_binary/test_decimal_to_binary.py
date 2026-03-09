import unittest
from . import convert_int_to_bin


class DecimalToBinTestCase(unittest.TestCase):
    def test_56(self):
        num = 56
        expected = 111000
        actual = convert_int_to_bin(num)
        self.assertEqual(expected, actual)

    def test_2(self):
        num = 2
        expected = 10
        actual = convert_int_to_bin(num)
        self.assertEqual(expected, actual)

    def test_32(self):
        num = 32
        expected = 100000
        actual = convert_int_to_bin(num)
        self.assertEqual(expected, actual)

    def test_10(self):
        num = 10
        expected = 1010
        actual = convert_int_to_bin(num)
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
