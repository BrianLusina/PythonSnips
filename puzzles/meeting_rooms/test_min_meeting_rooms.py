import unittest

from . import find_minimum_meeting_rooms, find_minimum_meeting_rooms_priority_queue


class MinimumMeetingRoomsTestCase(unittest.TestCase):
    def test_0(self):
        """should return 0 from input of A = []"""
        a = []
        expected = 0
        actual = find_minimum_meeting_rooms(a)
        self.assertEqual(expected, actual)

    def test_1(self):
        """should return 2 from input of A = [[0, 30],[5, 10],[15, 20]]"""
        a = [[0, 30], [5, 10], [15, 20]]
        expected = 2
        actual = find_minimum_meeting_rooms(a)
        self.assertEqual(expected, actual)

    def test_2(self):
        """should return 4 from input of A = [[1, 18], [18, 23], [15, 29], [4, 15],[2, 11], [5, 13]]"""
        a = [[1, 18], [18, 23], [15, 29], [4, 15], [2, 11], [5, 13]]
        expected = 4
        actual = find_minimum_meeting_rooms(a)
        self.assertEqual(expected, actual)

    def test_0_priority_queue(self):
        """should return 0 from input of A = []"""
        a = []
        expected = 0
        actual = find_minimum_meeting_rooms_priority_queue(a)
        self.assertEqual(expected, actual)

    def test_1_priority_queue(self):
        """should return 2 from input of A = [[0, 30],[5, 10],[15, 20]]"""
        a = [[0, 30], [5, 10], [15, 20]]
        expected = 2
        actual = find_minimum_meeting_rooms_priority_queue(a)
        self.assertEqual(expected, actual)

    def test_2_priority_queue(self):
        """should return 4 from input of A = [[1, 18], [18, 23], [15, 29], [4, 15],[2, 11], [5, 13]]"""
        a = [[1, 18], [18, 23], [15, 29], [4, 15], [2, 11], [5, 13]]
        expected = 4
        actual = find_minimum_meeting_rooms_priority_queue(a)
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
