import unittest

def sort_array(source_array):
    # Return a sorted array.

class SortTestCases(unittest.TestCase):
    def test_one(self):
        self.assertEqual(sort_array([5, 3, 2, 8, 1, 4]), [1, 3, 2, 8, 5, 4])

    def test_two(self):
        self.assertEqual(sort_array([5, 3, 1, 8, 0]), [1, 3, 5, 8, 0])

    def test_empty_array(self):
        self.assertEqual(sort_array([]),[])
