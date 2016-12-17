import unittest
from algorithms.bubble_sort import BubbleSort


class BubbleSortTests(unittest.TestCase):
    def test_1(self):
        bubbles = BubbleSort([54, 26, 93, 17, 77, 31, 44, 55, 20])
        self.assertEqual(bubbles.bubbly_ascend(), sorted([54, 26, 93, 17, 77, 31, 44, 55, 20]))

    def test_2(self):
        bubbles = BubbleSort([54, 26, 93, 17, 77, 31, 44, 55, 20])
        self.assertEqual(bubbles.bubbly_descend(), sorted([54, 26, 93, 17, 77, 31, 44, 55, 20], reverse=True))