import unittest
from parameterized import parameterized
from utils.test_utils import custom_test_name_func

from pymath.my_pow import my_pow, my_pow_rec, my_pow_iter

POW_TEST_CASES = [
    (2.00000, 10, 1024.00000),
    (2.10000, 3, 9.26100),
    (2.00000, -2, 0.25000),
    (3, 4, 81),
    (4, -3, 0.015625),
    (-3, 3, -27),
    (-2, 4, 16),
    (7.5, 0, 1),
    (-1, 2147483647, -1.00000),
]


class MyPowTestCase(unittest.TestCase):
    @parameterized.expand(POW_TEST_CASES, name_func=custom_test_name_func)
    def test_power(self, x: int | float, n: int, expected: float | int):
        actual = round(my_pow(x, n), 6)
        self.assertEqual(expected, actual)

    @parameterized.expand(POW_TEST_CASES, name_func=custom_test_name_func)
    def test_power_rec(self, x: int | float, n: int, expected: float | int):
        actual = round(my_pow_rec(x, n), 6)
        self.assertEqual(expected, actual)

    @parameterized.expand(POW_TEST_CASES, name_func=custom_test_name_func)
    def test_power_iter(self, x: int | float, n: int, expected: float | int):
        actual = round(my_pow_iter(x, n), 6)
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
