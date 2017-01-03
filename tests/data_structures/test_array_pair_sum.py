import unittest
from pysnips.data_structures.lists.array_pair_sum import array_pair_sum


class ArrayPairSumTests(unittest.TestCase):
    def test_find_pairs_that_equal_sum(self):
        self.assertEqual([[3, 7], [4, 6]], array_pair_sum(10, [3, 4, 5, 6, 7]),
                         "should find pairs that equal the expected sum")

    def test_should_not_output_duplicate_results(self):
        self.assertEqual([[3, 5], [4, 4], [4, 4], [4, 4]], array_pair_sum(8, [3, 4, 5, 4, 4]),
                         "should not output duplicate results")

    def test_should_work_on_no_matche_cases(self):
        self.assertEqual([], array_pair_sum(10, [3, 5, 6, 8]), "Should work when no matches are found")
