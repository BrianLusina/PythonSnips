import unittest

from datastructures.trees.trie import Trie


class TrieTestCases(unittest.TestCase):
    def test_trie_insert_and_search(self):
        """
        Test case for trie.insert() and trie.search()
        """
        trie = Trie()
        trie.insert("apple")

        first_search_result = trie.get_completions("apple")

        self.assertEqual(["apple"], first_search_result)

    def test_trie_search_with_empty_string(self):
        """
        Test case for trie.search() with empty string
        """
        trie = Trie()
        trie.insert("apple")

        second_search_result = trie.get_completions("")

        self.assertEqual([], second_search_result)

    def test_trie_insert_and_search_words_prefixed_with_he(self):
        trie = Trie()
        trie.insert("here")
        trie.insert("hear")
        trie.insert("he")
        trie.insert("hello")
        trie.insert("how ")
        trie.insert("her")

        actual = trie.get_completions("he")
        expected = sorted(["he", "her", "here", "hear", "hello"])

        self.assertEqual(expected, actual)

        actual2 = trie.get_completions("her")
        self.assertEqual(["her", "here"], actual2)

    def test_trie_insert_and_get_words(self):
        trie = Trie()
        trie.insert("here")
        trie.insert("hear")
        trie.insert("he")
        trie.insert("hello")
        trie.insert("how")
        trie.insert("her")

        actual = sorted(trie.get_all_words())
        expected = sorted(["here", "hear", "he", "hello", "how", "her"])

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
