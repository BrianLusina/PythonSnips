import unittest
from parameterized import parameterized
from pymath.power_of_two import is_power_of_two

POWER_OF_TWO_TEST_CASES = [
    (1, True),
    (16, True),
    (4, True),
    (3, False),
    (-512, False),
    (123456, False),
]


class PowerOfTwoTestCase(unittest.TestCase):
    @parameterized.expand(POWER_OF_TWO_TEST_CASES)
    def test_power_of_two(self, n: int, expected: bool):
        actual = is_power_of_two(n)
        self.assertEqual(actual, expected)


if __name__ == "__main__":
    unittest.main()
