import unittest
from typing import List
from parameterized import parameterized
from algorithms.intervals.meeting_rooms import most_booked

MOST_BOOKED_MEETING_ROOMS_TEST_CASES = [
    ([[0, 5], [1, 6], [6, 7], [7, 8], [8, 9]], 2, 0),
    ([[0, 10], [1, 11], [2, 12], [3, 13], [4, 14], [5, 15]], 3, 0),
    ([[0, 9], [1, 2], [2, 3], [3, 4], [5, 6], [6, 7], [7, 8], [8, 9]], 3, 1),
    ([[0, 1], [1, 2], [2, 3], [3, 4], [4, 5]], 1, 0),
    ([[0, 4], [1, 3], [2, 4], [3, 5], [4, 6], [5, 7]], 4, 1),
    ([[0, 10], [1, 5], [2, 7], [3, 4]], 2, 0),
    ([[1, 20], [2, 10], [3, 5], [4, 9], [6, 8]], 3, 1),
]


class MostBookedMeetingRoomsTestCase(unittest.TestCase):
    @parameterized.expand(MOST_BOOKED_MEETING_ROOMS_TEST_CASES)
    def test_most_booked(self, meetings: List[List[int]], rooms: int, expected: int):
        actual = most_booked(meetings, rooms)
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
