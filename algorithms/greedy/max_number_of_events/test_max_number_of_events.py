import unittest
from parameterized import parameterized
from utils.test_utils import custom_test_name_func
from algorithms.greedy.max_number_of_events import (
    max_events,
    max_events_2,
    max_events_3,
)

MAX_NUMBER_OF_EVENTS_TEST_CASES = [
    ([], 0),
    ([[1, 2], [2, 3], [3, 4]], 3),
    ([[1, 2], [2, 3], [3, 4], [1, 2]], 4),
    ([[7, 7]], 1),
    ([[12, 12], [12, 12], [12, 12], [12, 12]], 1),
    ([[2, 2], [4, 4], [6, 6], [8, 8], [10, 10]], 5),
    ([[3, 6], [3, 6], [3, 6], [3, 6], [3, 6], [3, 6], [3, 6]], 4),
    ([[1, 4], [1, 1], [2, 2], [2, 3], [3, 3], [4, 4]], 4),
]


class MaxNumberOfEventsTestCases(unittest.TestCase):
    @parameterized.expand(
        MAX_NUMBER_OF_EVENTS_TEST_CASES, name_func=custom_test_name_func
    )
    def test_max_number_of_events(self, events: list[list[int]], expected: int):
        actual = max_events(events)
        self.assertEqual(actual, expected)

    @parameterized.expand(
        MAX_NUMBER_OF_EVENTS_TEST_CASES, name_func=custom_test_name_func
    )
    def test_max_number_of_events_2(self, events: list[list[int]], expected: int):
        actual = max_events_2(events)
        self.assertEqual(actual, expected)

    @parameterized.expand(
        MAX_NUMBER_OF_EVENTS_TEST_CASES, name_func=custom_test_name_func
    )
    def test_max_number_of_events_3(self, events: list[list[int]], expected: int):
        actual = max_events_3(events)
        self.assertEqual(actual, expected)


if __name__ == "__main__":
    unittest.main()
