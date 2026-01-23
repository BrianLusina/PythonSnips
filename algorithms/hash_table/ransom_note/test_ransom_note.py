import unittest
from parameterized import parameterized
from algorithms.hash_table.ransom_note import can_construct, can_construct_2

RANSOM_NOTE_TEST_CASES = [
    ("codinginterviewquestions", "aboincsdefoetingvqtniewonoregessnutins", True),
    ("code", "coingd", False),
    ("codinginterview", "vieewidingcodinter", True),
    ("program", "programming", True),
    ("me", "meme", True),
    ("a", "b", False),
    ("aa", "ab", False),
    ("aa", "aab", True),
]


class RansomNoteTestCase(unittest.TestCase):
    @parameterized.expand(RANSOM_NOTE_TEST_CASES)
    def test_can_construct(self, ransom_note: str, magazine: str, expected: bool):
        actual = can_construct(ransom_note, magazine)
        self.assertEqual(expected, actual)

    @parameterized.expand(RANSOM_NOTE_TEST_CASES)
    def test_can_construct_2(self, ransom_note: str, magazine: str, expected: bool):
        actual = can_construct_2(ransom_note, magazine)
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
