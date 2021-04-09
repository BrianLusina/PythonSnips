import unittest

from pymath.binary.binary_converter import binary_converter


class BinaryConverterTestCases(unittest.TestCase):
    def test_conversion_one(self):
        result = binary_converter(0)
        self.assertEqual(result, '0', msg='Invalid conversion')

    def test_conversion_two(self):
        result = binary_converter(62)
        self.assertEqual(result, '111110', msg='Invalid conversion')

    def test_no_negative_numbers(self):
        result = binary_converter(-1)
        self.assertEqual(result, 'Invalid input', msg='Input below 0 not allowed')

    def test_no_numbers_above_255(self):
        result = binary_converter(300)
        self.assertEqual(result, 'Invalid input', msg='Input above 255 not allowed')
