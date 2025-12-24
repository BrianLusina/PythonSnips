import unittest
from parameterized import parameterized
from pymath.perfect_square import num_squares


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
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
