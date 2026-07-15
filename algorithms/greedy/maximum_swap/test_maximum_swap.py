import unittest
from parameterized import parameterized
from algorithms.greedy.maximum_swap import (
    maximum_swap,
    maximum_swap_suboptimal_greedy,
    maximum_swap_greedy_two_pass,
    maximum_swap_brute_force,
)

MAXIMUM_SWAP_TEST_CASES = [
    (4121, 4211),
    (87654, 87654),
    (1643, 6143),
    (123, 321),
    (14, 41),
    (2736, 7236),
    (9973, 9973),
]


class MaximumSwapTestCase(unittest.TestCase):
    @parameterized.expand(MAXIMUM_SWAP_TEST_CASES)
    def test_maximum_swap(self, num: int, expected: int):
        actual = maximum_swap(num)
        self.assertEqual(expected, actual)

    @parameterized.expand(MAXIMUM_SWAP_TEST_CASES)
    def test_maximum_swap_suboptimal_greedy(self, num: int, expected: int):
        actual = maximum_swap_suboptimal_greedy(num)
        self.assertEqual(expected, actual)

    @parameterized.expand(MAXIMUM_SWAP_TEST_CASES)
    def test_maximum_swap_greedy_two_pass(self, num: int, expected: int):
        actual = maximum_swap_greedy_two_pass(num)
        self.assertEqual(expected, actual)

    @parameterized.expand(MAXIMUM_SWAP_TEST_CASES)
    def test_maximum_swap_brute_force(self, num: int, expected: int):
        actual = maximum_swap_brute_force(num)
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
