import unittest
from typing import List
from parameterized import parameterized
from algorithms.sliding_window.max_points_from_cards import max_score


MAX_POINTS_FROM_PICKING_K_CARDS = [
    ([1, 2, 3, 4, 5, 6, 1], 3, 12),
    ([2, 2, 2], 2, 4),
    ([9, 7, 7, 9, 7, 7, 9], 7, 55),
    ([2, 11, 4, 5, 3, 9, 2], 3, 17),
    ([1, 100, 10, 0, 4, 5, 6], 3, 111),
    ([1, 1000, 1], 1, 1),
    ([1, 79, 80, 1, 1, 1, 200, 1], 3, 202),
    ([100, 40, 17, 9, 73, 75], 3, 248),
    ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5, 40),
]


class MaxPointsFromPickingKCardsTestCase(unittest.TestCase):
    @parameterized.expand(MAX_POINTS_FROM_PICKING_K_CARDS)
    def test_max_points_from_k_cards(self, cards: List[int], k: int, expected: int):
        actual = max_score(cards, k)
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
