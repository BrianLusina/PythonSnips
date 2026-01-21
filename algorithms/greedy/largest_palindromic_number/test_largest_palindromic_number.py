import unittest
from parameterized import parameterized
from algorithms.greedy.largest_palindromic_number import (
    largest_palindromic_number,
    largest_palindromic_number_v2,
)

LARGEST_PALINDROMIC_NUMBER_TEST_CASES = [
    ("2012", "212"),
    ("000001", "1"),
    ("111222333", "3213123"),
    ("000000", "0"),
    ("123456789123456789", "987654321123456789"),
    ("444947137", "7449447"),
    ("00009", "9"),
]


class LargestPalindromicNumberTestCase(unittest.TestCase):
    @parameterized.expand(LARGEST_PALINDROMIC_NUMBER_TEST_CASES)
    def test_largest_palindromic_number(self, num: str, expected: str):
        actual = largest_palindromic_number(num)
        self.assertEqual(expected, actual)

    @parameterized.expand(LARGEST_PALINDROMIC_NUMBER_TEST_CASES)
    def test_largest_palindromic_number_v2(self, num: str, expected: str):
        actual = largest_palindromic_number_v2(num)
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
