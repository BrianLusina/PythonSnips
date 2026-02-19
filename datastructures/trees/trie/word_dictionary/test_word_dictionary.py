import unittest
from datastructures.trees.trie.word_dictionary import WordDictionary


class WordDictionaryTestCase(unittest.TestCase):
    def test_case_1(self):
        """[[],["bad"],["dad"],["mad"],[],["pad"],["bad"],[".ad"],["b.."],[]]"""
        word_dictionary = WordDictionary()
        word_dictionary.add_word("bad")
        word_dictionary.add_word("dad")
        word_dictionary.add_word("mad")

        expected_words = ["bad", "dad", "mad"]
        actual_get_words_one = word_dictionary.get_words()
        self.assertEqual(expected_words, actual_get_words_one)

        actual_search_one = word_dictionary.search_word("pad")
        self.assertFalse(actual_search_one)

        actual_search_two = word_dictionary.search_word("bad")
        self.assertTrue(actual_search_two)

        actual_search_three = word_dictionary.search_word(".ad")
        self.assertTrue(actual_search_three)

        actual_search_four = word_dictionary.search_word("b..")
        self.assertTrue(actual_search_four)

        actual_get_words_two = word_dictionary.get_words()
        self.assertEqual(expected_words, actual_get_words_two)


if __name__ == "__main__":
    unittest.main()
