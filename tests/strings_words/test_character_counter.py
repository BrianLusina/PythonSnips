from pysnips.strings_words.character_counter import total_characters
from pysnips.errors import PySnipsError
import unittest


class CharacterCounterTest(unittest.TestCase):
    def shortDescription(self):
        return "Tests for {}".format(total_characters.__name__)

    def test_for_invalid_chars(self):
        with self.assertRaises(PySnipsError):
            total_characters(9)

