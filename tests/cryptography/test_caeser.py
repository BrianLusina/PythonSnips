import unittest

from cryptography.caeser_cipher import CaesarCipher, CaesarCipherV2


class CaeserCipherTests(unittest.TestCase):
    def test_rotate_a_by_1(self):
        caeser = CaesarCipher(1)
        self.assertEqual(caeser.encrypt('a'), 'b')

    def test_rotate_a_by_26(self):
        caeser = CaesarCipher(26)
        self.assertEqual(caeser.encrypt('a'), 'a')

    def test_rotate_a_by_0(self):
        caeser = CaesarCipher(0)
        self.assertEqual(caeser.encrypt('a'), 'a')

    def test_rotate_m_by_13(self):
        caeser = CaesarCipher(13)
        self.assertEqual(caeser.encrypt('m'), 'z')

    def test_rotate_n_by_13_with_wrap_around_alphabet(self):
        caeser = CaesarCipher(13)
        self.assertEqual(caeser.encrypt('n'), 'a')

    def test_rotate_capital_letters(self):
        caeser = CaesarCipher(5)
        self.assertEqual(caeser.encrypt('OMG'), 'TRL')

    def test_rotate_spaces(self):
        caeser = CaesarCipher(5)
        self.assertEqual(caeser.encrypt('O M G'), 'T R L')

    def test_rotate_numbers(self):
        caeser = CaesarCipher(4)
        self.assertEqual(caeser.encrypt('Testing 1 2 3 testing'), 'Xiwxmrk 1 2 3 xiwxmrk')

    def test_rotate_punctuation(self):
        caeser = CaesarCipher(21)
        self.assertEqual(caeser.encrypt("Let's eat, Grandma!"), "Gzo'n zvo, Bmviyhv!")

    def test_rotate_all_letters(self):
        caeser = CaesarCipher(13)
        self.assertEqual(caeser.encrypt("The quick brown fox jumps"
                                        " over the lazy dog."),
                         "Gur dhvpx oebja sbk whzcf bire gur ynml qbt.")

    def test_rotate_a_by_1_on_caeser_v2(self):
        caeser = CaesarCipherV2(1)
        self.assertEqual(caeser.encode('a'), 'b'.upper())

    def test_rotate_a_by_26_on_caeser_v2(self):
        caeser = CaesarCipherV2(26)
        self.assertEqual(caeser.encode('a'), 'a'.upper())

    def test_rotate_a_by_0_on_caeser_v2(self):
        caeser = CaesarCipherV2(0)
        self.assertEqual(caeser.encode('a'), 'a'.upper())

    def test_rotate_m_by_13_on_caeser_v2(self):
        caeser = CaesarCipherV2(13)
        self.assertEqual(caeser.encode('m'), 'z'.upper())

    def test_rotate_n_by_13_with_wrap_around_alphabet_on_caeser_v2(self):
        caeser = CaesarCipherV2(13)
        self.assertEqual(caeser.encode('n'), 'a'.upper())

    def test_rotate_capital_letters_on_caeser_v2(self):
        caeser = CaesarCipherV2(5)
        self.assertEqual(caeser.encode('OMG'), 'TRL'.upper())

    def test_rotate_spaces_on_caeser_v2(self):
        caeser = CaesarCipherV2(5)
        self.assertEqual(caeser.encode('O M G'), 'T R L'.upper())

    def test_rotate_numbers_on_caeser_v2(self):
        caeser = CaesarCipherV2(4)
        self.assertEqual(caeser.encode('Testing 1 2 3 testing'), 'Xiwxmrk 1 2 3 xiwxmrk'.upper())

    def test_rotate_punctuation_on_caeser_v2(self):
        caeser = CaesarCipherV2(21)
        self.assertEqual(caeser.encode("Let's eat, Grandma!"), "Gzo'n zvo, Bmviyhv!".upper())

    def test_rotate_all_letters_on_caeser_v2(self):
        caeser = CaesarCipherV2(13)
        self.assertEqual(caeser.encode("The quick brown fox jumps"
                                       " over the lazy dog."),
                         "Gur dhvpx oebja sbk whzcf bire gur ynml qbt.".upper())


if __name__ == '__main__':
    unittest.main()
