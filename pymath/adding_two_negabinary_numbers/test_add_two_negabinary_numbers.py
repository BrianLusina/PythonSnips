import unittest
from typing import List
from parameterized import parameterized
from utils.test_utils import custom_test_name_func
from pymath.adding_two_negabinary_numbers import add_negabinary, add_negabinary_2

ADD_TWO_NEGABINARY_NUMBERS_TEST_CASES = [
    ([0], [0], [0]),
    ([0], [1], [1]),
    ([1], [1], [1, 1, 0]),
    ([1, 0], [1], [1, 1]),
    ([1, 1, 1, 1, 1], [1, 0, 1], [1, 0, 0, 0, 0]),
    ([1, 0, 0], [0], [1, 0, 0]),
    ([1, 1, 0], [1, 0, 1], [1, 1, 0, 1, 1]),
    ([1, 1], [1], [0]),
]


class AddTwoNegabinaryNumbersTestCase(unittest.TestCase):
    @parameterized.expand(
        ADD_TWO_NEGABINARY_NUMBERS_TEST_CASES, name_func=custom_test_name_func
    )
    def test_add_two_negabinary_numbers(
        self, arr1: List[int], arr2: List[int], expected: List[int]
    ):
        actual = add_negabinary(arr1, arr2)
        self.assertEqual(expected, actual)

    @parameterized.expand(
        ADD_TWO_NEGABINARY_NUMBERS_TEST_CASES, name_func=custom_test_name_func
    )
    def test_add_two_negabinary_numbers_2(
        self, arr1: List[int], arr2: List[int], expected: List[int]
    ):
        actual = add_negabinary_2(arr1, arr2)
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
