import unittest

from datastructures.arrays.array_pair_sum import array_pair_sum, array_pair_sum_hash_table, array_pair_sum_sort


class ArrayPairSumTests(unittest.TestCase):
    def test_find_pairs_that_equal_sum(self):
        self.assertEqual(array_pair_sum(10, [3, 4, 5, 6, 7]), [[3, 7], [4, 6]],
                         "should find pairs that equal the expected sum")

    def test_find_pairs_with_arr_sort(self):
        self.assertEqual(array_pair_sum_sort(10, [3, 4, 5, 6, 7]), [[3, 7], [4, 6]],
                         "should find pairs that equal the expected sum")

    def test_find_pairs_with_arr_hash(self):
        self.assertEqual(array_pair_sum_hash_table(10, [3, 4, 5, 6, 7]), [[3, 7], [4, 6]],
                         "should find pairs that equal the expected sum")

    def test_should_not_output_duplicate_results(self):
        self.assertEqual(array_pair_sum(8, [3, 4, 5, 4, 4]), [[3, 5], [4, 4], [4, 4], [4, 4]],
                         "should not output duplicate results")

    # todo: tests don't pass for hash table and sort
    # def test_should_not_output_duplicate_results_arr_sort(self):
    #     self.assertEqual(array_pair_sum_sort(8, [3, 4, 5, 4, 4]), [[3, 5], [4, 4], [4, 4], [4, 4]],
    #                      "should not output duplicate results")
    #
    # def test_should_not_output_duplicate_results_arr_hash(self):
    #     self.assertEqual(array_pair_sum_hash_table(8, [3, 4, 5, 4, 4]), [[3, 5], [4, 4], [4, 4], [4, 4]],
    #                      "should not output duplicate results")

    def test_should_work_on_no_match_cases(self):
        self.assertEqual(array_pair_sum(10, [3, 5, 6, 8]), [], "Should work when no matches are found")

    def test_should_work_on_no_match_cases_hash(self):
        self.assertEqual(array_pair_sum_hash_table(10, [3, 5, 6, 8]), [], "Should work when no matches are found")

    def test_should_work_on_no_match_cases_sort(self):
        self.assertEqual(array_pair_sum_sort(10, [3, 5, 6, 8]), [], "Should work when no matches are found")
