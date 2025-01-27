import unittest
from . import check_permutation_with_sorting, check_permutation_with_map


class CheckPermutationWithSortingTestCases(unittest.TestCase):
    def test_1(self):
        """should return True for 'google' and 'ooggle'"""
        word_1 = "google"
        word_2 = "ooggle"
        actual = check_permutation_with_sorting(word_1, word_2)
        self.assertTrue(actual)

    def test_2(self):
        """should return False for 'not' and 'top'"""
        word_1 = "not"
        word_2 = "top"
        actual = check_permutation_with_sorting(word_1, word_2)
        self.assertFalse(actual)


class CheckPermutationWithMapTestCases(unittest.TestCase):
    def test_1(self):
        """should return True for 'google' and 'ooggle'"""
        word_1 = "google"
        word_2 = "ooggle"
        actual = check_permutation_with_map(word_1, word_2)
        self.assertTrue(actual)

    def test_2(self):
        """should return False for 'not' and 'top'"""
        word_1 = "not"
        word_2 = "top"
        actual = check_permutation_with_map(word_1, word_2)
        self.assertFalse(actual)

if __name__ == '__main__':
    unittest.main()
