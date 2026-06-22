import unittest
from parameterized import parameterized
from utils.test_utils import custom_test_name_func
from pymath.power_of_three import (
    is_power_of_three_with_log,
    is_power_of_three_with_mod,
    is_power_of_three_with_loop,
)

POWER_OF_THREE_TEST_CASES = [
    (27, True),
    (0, False),
    (-1, False),
    (9, True),
    (11, False),
    (45, False),
    (243, True),
    (10, False),
]


class PowerOfThreeTestCases(unittest.TestCase):
    @parameterized.expand(POWER_OF_THREE_TEST_CASES, name_func=custom_test_name_func)
    def test_power_of_three_using_logs(self, n: int, expected: bool):
        actual = is_power_of_three_with_log(n)
        self.assertEqual(expected, actual)

    @parameterized.expand(POWER_OF_THREE_TEST_CASES, name_func=custom_test_name_func)
    def test_power_of_three_using_mod(self, n: int, expected: bool):
        actual = is_power_of_three_with_mod(n)
        self.assertEqual(expected, actual)

    @parameterized.expand(POWER_OF_THREE_TEST_CASES, name_func=custom_test_name_func)
    def test_power_of_three_using_loop(self, n: int, expected: bool):
        actual = is_power_of_three_with_loop(n)
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
