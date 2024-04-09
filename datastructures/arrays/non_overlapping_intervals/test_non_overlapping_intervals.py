import unittest

from . import erase_overlap_intervals


class NonOverlappingIntervalsTestCase(unittest.TestCase):
    def test_1(self):
        """intervals = [[1,2],[2,3],[3,4],[1,3]] should return 1"""
        intervals = [[1, 2], [2, 3], [3, 4], [1, 3]]
        expected = 1
        actual = erase_overlap_intervals(intervals)
        self.assertEqual(expected, actual)

    def test_2(self):
        """intervals = [[1,2],[1,2],[1,2]] should return 2"""
        intervals = [[1, 2], [1, 2], [1, 2]]
        expected = 2
        actual = erase_overlap_intervals(intervals)
        self.assertEqual(expected, actual)

    def test_3(self):
        """intervals = [[1,2],[2,3]] should return 0"""
        intervals = [[1, 2], [2, 3]]
        expected = 0
        actual = erase_overlap_intervals(intervals)
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
