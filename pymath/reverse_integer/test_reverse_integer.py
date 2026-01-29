import unittest
from parameterized import parameterized
from pymath.reverse_integer import reverse_int, reverse_int_2

REVERSE_INTEGER_TEST_CASES = [
    (345, 543),
    (-5678, -8765),
    (452100, 1254),
    (1534536429, 0),
    (72, 27),
    (-7145, -5417),
    (8573400, 43758),
    (-584384000, -483485),
    (123, 321),
    (-123, -321),
    (120, 21),
]


class ReverseIntegerTestCase(unittest.TestCase):
    @parameterized.expand(REVERSE_INTEGER_TEST_CASES)
    def test_reverse_integer(self, num: int, expected: int):
        actual = reverse_int(num)
        self.assertEqual(expected, actual)

    @parameterized.expand(REVERSE_INTEGER_TEST_CASES)
    def test_reverse_integer_2(self, num: int, expected: int):
        actual = reverse_int_2(num)
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
