import unittest
from typing import List
from parameterized import parameterized
from puzzles.arrays.candy import candy


class CandyTestCase(unittest.TestCase):
    @parameterized.expand(
        [
            ([1], 1),
            ([1, 0, 2], 5),
            ([1, 2, 2], 4),
            ([1, 3, 4, 5, 2], 11),
            ([1, 3, 4, 5, 2], 11),
            ([1, 2, 3, 4, 5], 15),
            ([5, 4, 3, 2, 1], 15),
            ([5, 5, 5, 5, 5, 5, 5, 5], 8),
        ]
    )
    def test_candy(self, ratings: List[int], expected: int):
        actual = candy(ratings)
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
