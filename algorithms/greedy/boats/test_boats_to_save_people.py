import unittest
from typing import List
from parameterized import parameterized
from algorithms.greedy.boats import rescue_boats

TEST_CASES = [
    ([2, 1, 1], 3, 2),
    ([3, 1, 4, 2, 4], 4, 4),
    ([1, 1, 1, 1, 2], 3, 3),
    ([1, 2], 3, 1),
    ([5, 5, 5, 5], 5, 4),
    ([3, 2, 5, 5], 5, 3),
    ([1, 1, 1], 10, 2),
    ([5], 5, 1),
    ([3, 3, 3, 3], 3, 4),
]


class RescueBoatsTestCase(unittest.TestCase):
    @parameterized.expand(TEST_CASES)
    def test_rescue_boats(self, people: List[int], limit: int, expected: int):
        actual = rescue_boats(people, limit)
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
