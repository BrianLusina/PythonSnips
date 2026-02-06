import unittest
from typing import List
from parameterized import parameterized
from algorithms.graphs.single_cycle_check import has_single_cycle

SINGLE_CYCLE_CHECK_TEST_CASES = [
    ([2, 3, 1, -4, -4, 2], True),
]


class SingleCycleCheckTestCase(unittest.TestCase):
    @parameterized.expand(SINGLE_CYCLE_CHECK_TEST_CASES)
    def test_has_single_cycle(self, array: List[int], expected: bool):
        actual = has_single_cycle(array)
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
