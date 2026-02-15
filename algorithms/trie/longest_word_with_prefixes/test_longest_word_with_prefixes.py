import unittest
from typing import List
from parameterized import parameterized
from algorithms.trie.longest_word_with_prefixes import longest_word

LONGEST_WORD_WITH_PREFIXES_TEST_CASES = [
    (["a", "ab", "abc", "abd", "abde"], "abde"),
    (["x", "xy", "xyz", "xz"], "xyz"),
    (["m", "ma", "man", "many", "mat"], "many"),
    (["dog", "do", "d", "cat"], "dog"),
    (["car", "ca", "c", "cat"], "car"),
    (["a", "ap", "app", "apple", "apply"], "app"),
]


class LongestWordWithPrefixesTestCase(unittest.TestCase):
    @parameterized.expand(LONGEST_WORD_WITH_PREFIXES_TEST_CASES)
    def test_longest_word_with_prefixes(self, words: List[str], expected: str):
        actual = longest_word(words)
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
