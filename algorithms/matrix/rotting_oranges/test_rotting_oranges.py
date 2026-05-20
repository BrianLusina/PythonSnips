import unittest
from typing import List
from parameterized import parameterized
from utils.test_utils import custom_test_name_func
from algorithms.matrix.rotting_oranges import oranges_rotting

ROTTING_ORANGES_TEST_CASES = [
    ([[2, 1, 1], [1, 1, 0], [0, 1, 1]], 4),
    ([[2, 1, 1], [0, 1, 1], [1, 0, 1]], -1),
    ([[0, 2]], 0),
    ([[0, 1, 2], [1, 0, 2], [0, 2, 1]], -1),
    ([[0, 1, 1], [1, 0, 1], [0, 1, 1]], -1),
]


class RottingOrangesTestCase(unittest.TestCase):
    @parameterized.expand(ROTTING_ORANGES_TEST_CASES, name_func=custom_test_name_func)
    def test_oranges_rotting(self, grid: List[List[int]], expected: int):
        actual = oranges_rotting(grid)
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
