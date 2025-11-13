import unittest
from . import reverse_array_in_place


class ReverseArrayInPlaceTestCase(unittest.TestCase):
    def test_1(self):
        """should reverse an array of [1,2,3,4,5,6] in place"""
        collection = [1, 2, 3, 4, 5, 6]
        expected = [6, 5, 4, 3, 2, 1]
        reverse_array_in_place(collection)
        self.assertEqual(collection, expected)


if __name__ == "__main__":
    unittest.main()
