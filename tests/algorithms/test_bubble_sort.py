import unittest

from algorithms.sorting.bubble_sort import BubbleSort


class BubbleSortTests(unittest.TestCase):
    def test_1(self):
        bubbles = BubbleSort([54, 26, 93, 17, 77, 31, 44, 55, 20])
        self.assertEqual(bubbles.bubbly_ascend(), sorted([54, 26, 93, 17, 77, 31, 44, 55, 20]))

    def test_2(self):
        bubbles = BubbleSort([54, 26, 93, 17, 77, 31, 44, 55, 20])
        self.assertEqual(bubbles.bubbly_descend(), sorted([54, 26, 93, 17, 77, 31, 44, 55, 20], reverse=True))

    def test_invalid_input_should_throw_error_on_None_input(self):
        with self.assertRaises(ValueError):
            bubbles = BubbleSort(None)

    def test_invalid_str_input_should_throw_error(self):
        with self.assertRaises(ValueError):
            bubbles = BubbleSort("")

    def test_invalid_list_input_should_throw_error(self):
        with self.assertRaises(ValueError):
            bubbles = BubbleSort([12, 34, 564, "854"])

    def test_valid_list_of_ints_and_floats_does_not_throw_error(self):
        bubbles = BubbleSort([12, 3.5, 56, 7.89])
        self.assertListEqual(bubbles.bubbly_ascend(), sorted([12, 3.5, 56, 7.89]))


if __name__ == "__main__":
    unittest.main()
