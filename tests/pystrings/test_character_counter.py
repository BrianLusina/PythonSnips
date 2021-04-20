import unittest

from pystrings.character_counter import total_characters


class CharacterCounterTest(unittest.TestCase):
    def shortDescription(self):
        return "Tests for {}".format(total_characters.__name__)

    def test_for_invalid_chars(self):
        with self.assertRaises(Exception):
            total_characters(9)

    def test_for_word_list(self):
        self.assertEqual(12, total_characters(["adios", "bye", "ciao"]), msg="Expected 12")

    def test_for_int_array(self):
        self.assertEqual(0, total_characters([1, 2, 3, 4, 5, 6]), "Expected 0")

    def test_for_diff_elements_in_array(self):
        self.assertEqual(5, total_characters(["Brian", 5, {}, []]), "Expected 5")

    def test_for_one_element_in_array(self):
        self.assertEqual(10, total_characters(["abcdefghij"]), "Expected count to be 10")
