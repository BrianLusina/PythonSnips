import unittest

from . import reverse_words


class ReverseWordsTests(unittest.TestCase):
    def test_one_word(self):
        message = "vault"
        actual = reverse_words(message)
        expected = "vault"
        self.assertEqual(expected, actual)

    def test_two_words(self):
        message = "thief cake"
        actual = reverse_words(message)
        expected = "cake thief"
        self.assertEqual(expected, actual)

    def test_three_words(self):
        message = "one another get"
        actual = reverse_words(message)
        expected = "get another one"
        self.assertEqual(expected, actual)

    def test_multiple_words_same_length(self):
        message = "rat the ate cat the"
        actual = reverse_words(message)
        expected = "the cat ate the rat"
        self.assertEqual(expected, actual)

    def test_multiple_words_different_lengths(self):
        message = "yummy is cake bundt chocolate"
        actual = reverse_words(message)
        expected = "chocolate bundt cake is yummy"
        self.assertEqual(expected, actual)

    def test_empty_string(self):
        message = ""
        actual = reverse_words(message)
        expected = ""
        self.assertEqual(expected, actual)

    def test_string_with_spaces_at_both_ends(self):
        message = "  hello world  "
        actual = reverse_words(message)
        expected = "world hello"
        self.assertEqual(expected, actual)

    def test_string_with_multiple_spaces_in_between_words(self):
        message = "a good   example"
        actual = reverse_words(message)
        expected = "example good a"
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
