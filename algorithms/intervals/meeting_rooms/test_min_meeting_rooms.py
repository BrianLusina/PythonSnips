import unittest
from typing import List
from parameterized import parameterized
from . import find_minimum_meeting_rooms, find_minimum_meeting_rooms_priority_queue


class MinimumMeetingRoomsTestCase(unittest.TestCase):
    @parameterized.expand(
        [
            ([], 0),
            ([[0, 30], [5, 10], [15, 20]], 2),
            ([[1, 18], [18, 23], [15, 29], [4, 15], [2, 11], [5, 13]], 4),
            ([[2, 8], [3, 4], [3, 9], [5, 11], [8, 20], [11, 15]], 3),
            ([[1, 7], [2, 6], [3, 7], [4, 8], [5, 8], [2, 9], [1, 8]], 7),
            ([[1, 6], [4, 8], [1, 5], [6, 8], [8, 11], [8, 9], [5, 10]], 3),
            ([[1, 3], [2, 6], [8, 10], [9, 15], [12, 14]], 2),
            ([[1, 2], [4, 6], [3, 4], [7, 8]], 1),
            ([[1, 7], [2, 6], [3, 7], [4, 8], [5, 8]], 5),
            ([[1, 2], [1, 2], [1, 2]], 3),
        ]
    )
    def test_find_minimum_meeting_rooms(self, meetings: List[List[int]], expected: int):
        actual = find_minimum_meeting_rooms(meetings)
        self.assertEqual(expected, actual)

    @parameterized.expand(
        [
            ([], 0),
            ([[0, 30], [5, 10], [15, 20]], 2),
            ([[1, 18], [18, 23], [15, 29], [4, 15], [2, 11], [5, 13]], 4),
            ([[2, 8], [3, 4], [3, 9], [5, 11], [8, 20], [11, 15]], 3),
            ([[1, 7], [2, 6], [3, 7], [4, 8], [5, 8], [2, 9], [1, 8]], 7),
            ([[1, 6], [4, 8], [1, 5], [6, 8], [8, 11], [8, 9], [5, 10]], 3),
            ([[1, 3], [2, 6], [8, 10], [9, 15], [12, 14]], 2),
            ([[1, 2], [4, 6], [3, 4], [7, 8]], 1),
            ([[1, 7], [2, 6], [3, 7], [4, 8], [5, 8]], 5),
            ([[1, 2], [1, 2], [1, 2]], 3),
        ]
    )
    def test_find_minimum_meeting_rooms_priority_queue(
        self, meetings: List[List[int]], expected: int
    ):
        actual = find_minimum_meeting_rooms_priority_queue(meetings)
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
