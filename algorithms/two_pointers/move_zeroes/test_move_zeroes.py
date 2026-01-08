import unittest
from typing import List
from parameterized import parameterized
from algorithms.two_pointers.move_zeroes import move_zeroes, move_zeroes_one

MOVE_ZEROES_TEST_CASES = [
    ([0, 1, 0, 3, 12], [1, 3, 12, 0, 0]),
    ([0], [0]),
    ([0, 0, 0], [0, 0, 0]),
    ([1, 0], [1, 0]),
    ([2, 0, 4, 0, 9], [2, 4, 9, 0, 0]),
    ([1, 0, 4, 0, 3, 0, 1], [1, 4, 3, 1, 0, 0, 0]),
    ([0, 0, 1], [1, 0, 0]),
    ([1, 2, 3], [1, 2, 3]),
]


class MoveZeroesTestCase(unittest.TestCase):
    @parameterized.expand(MOVE_ZEROES_TEST_CASES)
    def test_move_zeroes(self, nums: List[int], expected: [List]):
        move_zeroes(nums)
        self.assertEqual(expected, nums)

    @parameterized.expand(MOVE_ZEROES_TEST_CASES)
    def test_move_zeroes_with_intermediate(self, nums: List[int], expected: List[int]):
        move_zeroes_one(nums)
        self.assertEqual(expected, nums)


if __name__ == "__main__":
    unittest.main()
