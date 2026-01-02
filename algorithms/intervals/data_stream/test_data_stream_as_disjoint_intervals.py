import unittest
from typing import List
from parameterized import parameterized
from algorithms.intervals.data_stream import SummaryRanges, SummaryRangesV2

TEST_CASES = [
    ([5], [[5, 5]]),
    ([5, 5], [[5, 5]]),
    ([1, 3, 2], [[1, 3]]),
    ([1, 7, 3], [[1, 1], [3, 3], [7, 7]]),
    ([10, 12, 11], [[10, 12]]),
    ([1, 4, 2, 9, 3], [[1, 4], [9, 9]]),
]


class DataStreamAsDisjointIntervalTestCase(unittest.TestCase):
    @parameterized.expand(TEST_CASES)
    def test_data_stream_as_disjoint_intervals(
        self, data: List[int], expected: List[List[int]]
    ):
        summary_ranges = SummaryRanges()
        for d in data:
            summary_ranges.add_num(d)
        actual = summary_ranges.get_intervals()
        self.assertEqual(expected, actual)

    @parameterized.expand(TEST_CASES)
    def test_data_stream_as_disjoint_intervals_v2(
        self, data: List[int], expected: List[List[int]]
    ):
        summary_ranges = SummaryRangesV2()
        for d in data:
            summary_ranges.add_num(d)
        actual = summary_ranges.get_intervals()
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
