import unittest
from typing import List

from parameterized import parameterized

from algorithms.trie.topkfreqwords import top_k_frequent_words_2, top_k_frequent_words

TOP_K_FREQUENT_WORDS_TEST_CASES = [
    (["i", "love", "leetcode", "i", "love", "coding"], 2, ["i", "love"]),
    (
        ["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"],
        4,
        ["the", "is", "sunny", "day"],
    ),
    (["i", "love", "leetcode", "i", "love", "coding"], 3, ["i", "love", "coding"]),
]


class TopKFrequentWordsTestCase(unittest.TestCase):
    @parameterized.expand(TOP_K_FREQUENT_WORDS_TEST_CASES)
    def test_top_k_frequent_words(self, words: List[str], k: int, expected: List[str]):
        actual = top_k_frequent_words(words, k)
        self.assertEqual(expected, actual)

    @parameterized.expand(TOP_K_FREQUENT_WORDS_TEST_CASES)
    def test_top_k_frequent_words_2(
        self, words: List[str], k: int, expected: List[str]
    ):
        actual = top_k_frequent_words_2(words, k)
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
