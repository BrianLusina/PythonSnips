import unittest

from datastructures.trees.trie import Trie


class TrieTestCases(unittest.TestCase):
    def test_trie_insert_and_search(self):
        """
        Test case for trie.insert() and trie.search()
        """
        trie = Trie()
        trie.insert("apple")

        first_search_result = trie.search("apple")

        self.assertEqual(["apple"], first_search_result)

    def test_trie_search_with_empty_string(self):
        """
        Test case for trie.search() with empty string
        """
        trie = Trie()
        trie.insert("apple")

        second_search_result = trie.search("")

        self.assertEqual([], second_search_result)

    def test_trie_insert_and_search_words_prefixed_with_he(self):
        trie = Trie()
        trie.insert("here")
        trie.insert("hear")
        trie.insert("he")
        trie.insert("hello")
        trie.insert("how ")
        trie.insert("her")

        actual = trie.search("he")

        self.assertEqual(['he', 'her', 'here', 'hear', 'hello'], actual)

        actual2 = trie.search("her")
        self.assertEqual(['her', 'here'], actual2)


if __name__ == "__main__":
    unittest.main()
