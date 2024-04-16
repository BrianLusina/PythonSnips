import unittest
from .palindrome_index import palindrome_index, palindrome_index_two


class PalindromeIndexTests(unittest.TestCase):
    def test_aaab_should_return_3(self):
        word = "aaab"
        expected = 3
        actual = palindrome_index(word)
        self.assertEqual(expected, actual)

    def test_baa_should_return_0(self):
        word = "baa"
        expected = 0
        actual = palindrome_index(word)
        self.assertEqual(expected, actual)

    def test_aaa_should_return_negative_1(self):
        word = "aaa"
        expected = -1
        actual = palindrome_index(word)
        self.assertEqual(expected, actual)


class PalindromeIndexTwoTests(unittest.TestCase):
    def test_aaab_should_return_3(self):
        word = "aaab"
        expected = 3
        actual = palindrome_index_two(word)
        self.assertEqual(expected, actual)

    def test_baa_should_return_0(self):
        word = "baa"
        expected = 0
        actual = palindrome_index_two(word)
        self.assertEqual(expected, actual)

    def test_aaa_should_return_negative_1(self):
        word = "aaa"
        expected = -1
        actual = palindrome_index_two(word)
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
