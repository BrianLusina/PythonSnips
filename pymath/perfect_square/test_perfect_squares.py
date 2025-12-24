import unittest
from parameterized import parameterized
from pymath.perfect_square import num_squares, num_squares_2


TEST_CASES = [
    (1, 1),
    (12, 3),
    (13, 2),
    (23, 4),
    (997, 2),
]


class NumOfPerfectSquaresTestCases(unittest.TestCase):
    @parameterized.expand(TEST_CASES)
    def test_num_of_perfect_squares(self, n: int, expected: int):
        actual = num_squares(n)
        (self.assertEqual(expected, actual) @ parameterized.expand(TEST_CASES))

    def test_num_of_perfect_squares_2(self, n: int, expected: int):
        actual = num_squares_2(n)
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
