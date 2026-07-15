import unittest
from typing import List
from parameterized import parameterized
from utils.test_utils import custom_test_name_func
from algorithms.trie.replace_words import (
    replace_words_with_prefix_hash,
    replace_words_with_trie,
    replace_words_with_trie_2,
)

REPLACE_WORDS_TEST_CASES = [
    (
        ["cat", "bat", "rat"],
        "the cattle was rattled by the battery",
        "the cat was rat by the bat",
    ),
    (
        ["a", "aa", "aaa", "aaaa"],
        "a aa a aaaa aaa aaa aaa aaaaaa bbb baba ababa",
        "a a a a a a a a bbb baba a",
    ),
    (["a", "b", "c"], "aadsfasf absbs bbab cadsfafs", "a a b c"),
    (
        ["catt", "cat", "bat", "rat"],
        "the cattle was rattled by the battery",
        "the cat was rat by the bat",
    ),
    (
        ["ac", "ab"],
        "it is abnormal that this solution is accepted",
        "it is ab that this solution is ac",
    ),
]


class ReplaceWordsHashTestCases(unittest.TestCase):
    @parameterized.expand(REPLACE_WORDS_TEST_CASES, name_func=custom_test_name_func)
    def test_replace_words_with_prefix_hash(
        self, dictionary: List[str], sentence: str, expected: str
    ):
        actual = replace_words_with_prefix_hash(dictionary, sentence)
        self.assertEqual(expected, actual)

    @parameterized.expand(REPLACE_WORDS_TEST_CASES, name_func=custom_test_name_func)
    def test_replace_words_with_trie(
        self, dictionary: List[str], sentence: str, expected: str
    ):
        actual = replace_words_with_trie(dictionary, sentence)
        self.assertEqual(expected, actual)

    @parameterized.expand(REPLACE_WORDS_TEST_CASES, name_func=custom_test_name_func)
    def test_replace_words_with_trie_2(
        self, dictionary: List[str], sentence: str, expected: str
    ):
        actual = replace_words_with_trie_2(dictionary=dictionary, sentence=sentence)
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
