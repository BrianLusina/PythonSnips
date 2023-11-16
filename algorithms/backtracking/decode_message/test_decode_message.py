import unittest
from . import number_of_ways_to_decode_message


class DecodeWaysTestCases(unittest.TestCase):
    def test_12(self):
        """should return 2 for input of 12"""
        digits = "12"
        expected = 2
        self._assert_test(digits, expected)

    def test_123(self):
        """should return 3 for input of 123"""
        digits = "123"
        expected = 3
        self._assert_test(digits, expected)

    def test_11223(self):
        """should return 8 for input of 11223"""
        digits = "11223"
        expected = 8
        self._assert_test(digits, expected)

    def test_313(self):
        """should return 2 for input of 313"""
        digits = "313"
        expected = 2
        self._assert_test(digits, expected)

    def test_02(self):
        """should return 0 for input of 02"""
        digits = "02"
        expected = 0
        self._assert_test(digits, expected)

    def _assert_test(self, digits: str, expected: int):
        actual = number_of_ways_to_decode_message(digits)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
