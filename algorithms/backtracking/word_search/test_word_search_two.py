import unittest
from typing import List
from parameterized import parameterized
from algorithms.backtracking.word_search import find_strings

TEST_CASES = [
    (
        [
            ["C", "S", "L", "I", "M"],
            ["O", "I", "L", "M", "O"],
            ["O", "L", "I", "E", "O"],
            ["R", "T", "A", "S", "N"],
            ["S", "I", "T", "A", "C"],
        ],
        ["SLIME", "SAILOR", "MATCH", "COCOON"],
        ["SLIME", "SAILOR"],
    ),
    (
        [
            ["C", "S", "L", "I", "M"],
            ["O", "I", "B", "M", "O"],
            ["O", "L", "U", "E", "O"],
            ["N", "L", "Y", "S", "N"],
            ["S", "I", "N", "E", "C"],
        ],
        ["BUY", "STUFF", "ONLINE", "NOW"],
        ["BUY", "ONLINE"],
    ),
    (
        [
            ["C", "O", "L", "I", "M"],
            ["I", "N", "L", "M", "O"],
            ["A", "L", "I", "E", "O"],
            ["R", "T", "A", "S", "N"],
            ["S", "I", "T", "A", "C"],
        ],
        ["REINDEER", "IN", "RAIN"],
        ["IN", "RAIN"],
    ),
    (
        [
            ["P", "S", "L", "A", "M"],
            ["O", "P", "U", "R", "O"],
            ["O", "L", "I", "E", "O"],
            ["R", "T", "A", "S", "N"],
            ["S", "I", "T", "A", "C"],
        ],
        ["TOURISM", "DESTINED", "POPULAR"],
        ["POPULAR"],
    ),
    (
        [
            ["O", "A", "A", "N"],
            ["E", "T", "A", "E"],
            ["I", "H", "K", "R"],
            ["I", "F", "L", "V"],
        ],
        ["OATH", "PEA", "EAT", "RAIN"],
        ["OATH", "EAT"],
    ),
]


class WordSearchTwoTestCase(unittest.TestCase):
    @parameterized.expand(TEST_CASES)
    def test_word_search_two(
        self, grid: List[List[str]], words: List[str], expected: List[str]
    ):
        actual = find_strings(grid, words)
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
