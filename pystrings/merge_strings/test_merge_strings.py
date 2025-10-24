import unittest

from . import merge_alternately, merge_alternately_2


class MergeStringsAlternativelyTestCase(unittest.TestCase):
    def test_abc_and_pqr(self):
        """should return apbqcr for word1=abc and word2=pqr"""
        word1 = "abc"
        word2 = "pqr"
        expected = "apbqcr"
        actual = merge_alternately(word1, word2)

        self.assertEqual(expected, actual)

    def test_ab_and_pqrs(self):
        """should return apbqrs for word1=ab and word2=pqrs"""
        word1 = "ab"
        word2 = "pqrs"
        expected = "apbqrs"
        actual = merge_alternately(word1, word2)

        self.assertEqual(expected, actual)

    def test_abcd_and_pq(self):
        """should return apbqcd for word1=abcd and word2=pq"""
        word1 = "abcd"
        word2 = "pq"
        expected = "apbqcd"
        actual = merge_alternately(word1, word2)

        self.assertEqual(expected, actual)

    def test_cf_and_eee(self):
        """should return cefee for word1=cf and word2=eee"""
        word1 = "cf"
        word2 = "eee"
        expected = "cefee"
        actual = merge_alternately(word1, word2)

        self.assertEqual(expected, actual)


class MergeStringsAlternatively2TestCase(unittest.TestCase):
    def test_abc_and_pqr(self):
        """should return apbqcr for word1=abc and word2=pqr"""
        word1 = "abc"
        word2 = "pqr"
        expected = "apbqcr"
        actual = merge_alternately_2(word1, word2)

        self.assertEqual(expected, actual)

    def test_ab_and_pqrs(self):
        """should return apbqrs for word1=ab and word2=pqrs"""
        word1 = "ab"
        word2 = "pqrs"
        expected = "apbqrs"
        actual = merge_alternately_2(word1, word2)

        self.assertEqual(expected, actual)

    def test_abcd_and_pq(self):
        """should return apbqcd for word1=abcd and word2=pq"""
        word1 = "abcd"
        word2 = "pq"
        expected = "apbqcd"
        actual = merge_alternately_2(word1, word2)

        self.assertEqual(expected, actual)

    def test_cf_and_eee(self):
        """should return cefee for word1=cf and word2=eee"""
        word1 = "cf"
        word2 = "eee"
        expected = "cefee"
        actual = merge_alternately_2(word1, word2)

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
