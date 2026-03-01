import unittest
from parameterized import parameterized
from bit_manipulation.sum_two_integers import integer_addition, integer_addition_2

SUM_OF_TWO_INTEGERS_TEST_CASES = [
    (1, -1, 0),
    (2, 5, 7),
    (3, 10, 13),
    (-10, -40, -50),
    (13, 16, 29),
]

class SumOfTwoIntegersTestCase(unittest.TestCase):
    @parameterized.expand(SUM_OF_TWO_INTEGERS_TEST_CASES)
    def test_integer_addition(self, a: int, b: int, expected: int):
        result = integer_addition(a, b)
        self.assertEqual(result, expected)

    @parameterized.expand(SUM_OF_TWO_INTEGERS_TEST_CASES)
    def test_integer_addition_2(self, a: int, b: int, expected: int):
        result = integer_addition_2(a, b)
        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
