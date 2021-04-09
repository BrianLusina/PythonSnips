import unittest

from datastructures.lists.bus_stops import number


class BusStopsTests(unittest.TestCase):
    def test_1(self):
        self.assertEqual(number([[10, 0], [3, 5], [5, 8]]), 5)

    def test_2(self):
        self.assertEqual(number([[3, 0], [9, 1], [4, 10], [12, 2], [6, 1], [7, 10]]), 17)

    def test_3(self):
        self.assertEqual(number([[3, 0], [9, 1], [4, 8], [12, 2], [6, 1], [7, 8]]), 21)
