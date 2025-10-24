import unittest

from puzzles.queue_to_do import queue_to_do


class QueueToDoTestCases(unittest.TestCase):
    def test_start_of_0_and_length_3_returns_2(self):
        """Should return 2 for start of 0 & length of 3"""
        start = 0
        length = 3
        expected = 2
        actual = queue_to_do(start, length)
        self.assertEqual(expected, actual)

    def test_start_of_17_and_length_of_4_returns_14(self):
        """Should return 14 for start of 17 & length of 4"""
        start = 17
        length = 4
        expected = 14
        actual = queue_to_do(start, length)
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
