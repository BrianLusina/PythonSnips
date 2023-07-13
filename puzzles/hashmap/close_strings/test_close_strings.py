import unittest

from . import close_strings, close_strings2


class CloseStringsTestCase(unittest.TestCase):
    def test_abc_and_bca_should_return_true(self):
        """should return true for word1=abc and word2=bca"""
        word1 = "abc"
        word2 = "bca"
        actual = close_strings(word1, word2)
        self.assertTrue(actual)

    def test_a_and_aa_should_return_false(self):
        """should return false for word1=a and word2=aa"""
        word1 = "a"
        word2 = "aa"
        actual = close_strings(word1, word2)
        self.assertFalse(actual)

    def test_cabbba_and_abbccc_should_return_true(self):
        """should return true for word1=cabbba and word2=abbccc"""
        word1 = "cabbba"
        word2 = "abbccc"
        actual = close_strings(word1, word2)
        self.assertTrue(actual)


class CloseStrings2TestCase(unittest.TestCase):
    def test_abc_and_bca_should_return_true(self):
        """should return true for word1=abc and word2=bca"""
        word1 = "abc"
        word2 = "bca"
        actual = close_strings2(word1, word2)
        self.assertTrue(actual)

    def test_a_and_aa_should_return_false(self):
        """should return false for word1=a and word2=aa"""
        word1 = "a"
        word2 = "aa"
        actual = close_strings2(word1, word2)
        self.assertFalse(actual)

    def test_cabbba_and_abbccc_should_return_true(self):
        """should return true for word1=cabbba and word2=abbccc"""
        word1 = "cabbba"
        word2 = "abbccc"
        actual = close_strings2(word1, word2)
        self.assertTrue(actual)


if __name__ == '__main__':
    unittest.main()
