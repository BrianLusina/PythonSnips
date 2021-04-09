import unittest

from pystrings.isogram import is_isogram


class Tests(unittest.TestCase):
    """
    Tests the isogram function
    """

    def test1(self):
        self.assertEqual(is_isogram("Dermatoglyphics"), True)

    def test2(self):
        self.assertEqual(is_isogram("isogram"), True)

    def test3(self):
        self.assertEqual(is_isogram("aba"), False, "same chars may not be adjacent")

    def test4(self):
        self.assertEqual(is_isogram("moOse"), False, "same chars may not be same case")

    def test5(self):
        self.assertEqual(is_isogram("isIsogram"), False)

    def test6(self):
        self.assertEqual(is_isogram(""), True, "an empty string is a valid isogram")

    def test_empty_string(self):
        self.assertTrue(is_isogram(""))

    def test_isogram_with_only_lower_case_characters(self):
        self.assertTrue(is_isogram("isogram"))

    def test_word_with_one_duplicated_character(self):
        self.assertFalse(is_isogram("eleven"))

    def test_longest_reported_english_isogram(self):
        self.assertTrue(is_isogram("subdermatoglyphic"))

    def test_word_with_duplicated_character_in_mixed_case(self):
        self.assertFalse(is_isogram("Alphabet"))

    def test_hypothetical_isogrammic_word_with_hyphen(self):
        self.assertTrue(is_isogram("thumbscrew-japingly"))

    def test_isogram_with_duplicated_non_letter_character(self):
        self.assertTrue(is_isogram("Hjelmqvist-Gryb-Zock-Pfund-Wax"))

    def test_made_up_name_that_is_an_isogram(self):
        self.assertTrue(is_isogram("Emily Jung Schwartzkopf"))


if __name__ == "__main__":
    unittest.main()
