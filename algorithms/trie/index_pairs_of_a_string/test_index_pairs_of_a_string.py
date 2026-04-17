import unittest
from typing import List
from parameterized import parameterized
from algorithms.trie.index_pairs_of_a_string import index_pairs

INDEX_PAIRS_OF_A_STRING = [
    (
        "thestoryofeducativeandme",
        ["story", "feduc", "educative"],
        [[3, 7], [9, 13], [10, 18]],
    ),
    ("xyxyx", ["xyx", "xy"], [[0, 1], [0, 2], [2, 3], [2, 4]]),
    ("howareyou", ["how", "are", "you"], [[0, 2], [3, 5], [6, 8]]),
    ("weather", ["weather"], [[0, 6]]),
    (
        "aquickbrownfoxjumpsoverthelazydog",
        ["quick", "fox", "dog"],
        [[1, 5], [11, 13], [30, 32]],
    ),
]


class IndexPairsOfAStringTestCase(unittest.TestCase):
    @parameterized.expand(INDEX_PAIRS_OF_A_STRING)
    def test_index_pairs_of_a_string(
        self, text: str, words: List[str], expected: List[List[int]]
    ):
        actual = index_pairs(text, words)
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
