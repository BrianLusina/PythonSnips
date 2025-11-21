import unittest
from . import is_prefix_of_word


class IsPrefixOfWordTestCase(unittest.TestCase):
    def test_1(self):
        sentence = "i love coding"
        search_word = "lov"
        expected = 2
        actual = is_prefix_of_word(sentence, search_word)
        self.assertEqual(expected, actual)

    def test_2(self):
        sentence = "hello world"
        search_word = "he"
        expected = 1
        actual = is_prefix_of_word(sentence, search_word)
        self.assertEqual(expected, actual)

    def test_3(self):
        sentence = "please playground player"
        search_word = "pla"
        expected = 2
        actual = is_prefix_of_word(sentence, search_word)
        self.assertEqual(expected, actual)

    def test_4(self):
        sentence = "open source ai"
        search_word = "deep"
        expected = -1
        actual = is_prefix_of_word(sentence, search_word)
        self.assertEqual(expected, actual)

    def test_5(self):
        sentence = "cats dog cattle category"
        search_word = "cat"
        expected = 1
        actual = is_prefix_of_word(sentence, search_word)
        self.assertEqual(expected, actual)

    def test_6(self):
        sentence = "this is fine"
        search_word = "fi"
        expected = 3
        actual = is_prefix_of_word(sentence, search_word)
        self.assertEqual(expected, actual)

    def test_7(self):
        sentence = "hello world"
        search_word = "x"
        expected = -1
        actual = is_prefix_of_word(sentence, search_word)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
