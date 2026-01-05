import unittest
from typing import List
from parameterized import parameterized
from algorithms.intervals.can_attend_meetings import can_attend_meetings

CAN_ATTEND_MEETINGS_TEST_CASES = [
    ([[1, 5], [3, 9], [6, 8]], False),
    ([[10, 12], [6, 9], [13, 15]], True),
    ([[0, 30], [5, 10], [15, 20]], False),
    ([[7, 10], [2, 4]], True),
    ([[7, 10], [2, 4]], True),
    ([[1, 2], [2, 3], [3, 4]], True),
    ([[1, 3], [2, 4], [4, 6]], False),
    ([[0, 1], [3, 5], [6, 7]], True),
    ([[10, 20], [20, 30], [30, 40]], True),
    ([[1, 5], [6, 10], [11, 15]], True),
    ([[5, 10], [15, 20], [10, 15]], True),
]


class CanAttendMeetingsTestCase(unittest.TestCase):
    @parameterized.expand(CAN_ATTEND_MEETINGS_TEST_CASES)
    def test_can_attend_meetings(self, intervals: List[List[int]], expected: bool):
        actual = can_attend_meetings(intervals)
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
