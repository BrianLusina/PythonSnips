import unittest
from parameterized import parameterized
from algorithms.backtracking.letter_tile_possibilities import (
    num_tile_possibilities,
    num_tile_possibilities_with_recursion,
    num_tile_possibilities_with_optimized_recursion,
)

LETTER_TILE_POSSIBILITIES = [
    ("AAB", 8),
    ("ABC", 15),
    ("ABC", 15),
    ("CDB", 15),
    ("ZZZ", 3),
    ("AAABBC", 188),
    ("V", 1),
]


class NumTilePossibilitiesTestCase(unittest.TestCase):
    @parameterized.expand(LETTER_TILE_POSSIBILITIES)
    def test_num_tile_possibilities(self, tiles: str, expected: int):
        actual = num_tile_possibilities(tiles)
        self.assertEqual(expected, actual)

    @parameterized.expand(LETTER_TILE_POSSIBILITIES)
    def test_num_tile_possibilities_with_recursion(self, tiles: str, expected: int):
        actual = num_tile_possibilities_with_recursion(tiles)
        self.assertEqual(expected, actual)

    @parameterized.expand(LETTER_TILE_POSSIBILITIES)
    def test_num_tile_possibilities_with_optimized_recursion(
        self, tiles: str, expected: int
    ):
        actual = num_tile_possibilities_with_optimized_recursion(tiles)
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
