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

    def test_case_2(self):
        word_dictionary = WordDictionary()
        actual_words_1 = word_dictionary.get_words()
        self.assertEqual([], actual_words_1)

        word_dictionary.add_word("apple")
        word_dictionary.add_word("grape")
        actual_words_2 = word_dictionary.get_words()
        expected_words_1 = ["apple", "grape"]
        self.assertEqual(expected_words_1, actual_words_2)

        actual_search_word_1 = word_dictionary.search_word("strawberry")
        self.assertFalse(actual_search_word_1)

        word_dictionary.add_word("banana")
        word_dictionary.add_word("banan")

        actual_search_word_2 = word_dictionary.search_word("bana..")
        self.assertTrue(actual_search_word_2)

        actual_search_word_3 = word_dictionary.search_word("ba...a")
        self.assertTrue(actual_search_word_3)

        actual_get_words_3 = word_dictionary.get_words()
        expected_words_2 = ["apple", "banan", "banana", "grape"]
        self.assertEqual(sorted(expected_words_2), sorted(actual_get_words_3))


if __name__ == "__main__":
    unittest.main()
