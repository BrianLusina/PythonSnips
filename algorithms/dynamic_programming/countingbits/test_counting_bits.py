import unittest
from typing import List
from parameterized import parameterized
from algorithms.dynamic_programming.countingbits import count_bits

COUNTING_BITS_TEST_CASES = [
    (6, [0, 1, 1, 2, 1, 2, 2]),
    (2, [0, 1, 1]),
    (5, [0, 1, 1, 2, 1, 2]),
    (0, [0]),
    (7, [0, 1, 1, 2, 1, 2, 2, 3]),
    (10, [0, 1, 1, 2, 1, 2, 2, 3, 1, 2, 2]),
]


class CountingBitsTestCase(unittest.TestCase):
    @parameterized.expand(COUNTING_BITS_TEST_CASES)
    def test_counting_bits(self, n: int, expected: List[int]):
        actual = count_bits(n)
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
