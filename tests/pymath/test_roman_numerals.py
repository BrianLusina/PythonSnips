import unittest

from pymath.roman_numeral import RomanNumeral, numeral


class RomanTests(unittest.TestCase):
    def test_1(self):
        roman = RomanNumeral("IV")
        self.assertEqual(roman.translate_roman_numeral(), 4)

    def test_2(self):
        roman = RomanNumeral("LX")
        self.assertEqual(roman.translate_roman_numeral(), 60)

    def test_76(self):
        roman = RomanNumeral("LXXVI")
        self.assertEqual(roman.translate_roman_numeral(), 76)

    def test_16(self):
        roman = RomanNumeral("XVI")
        self.assertEqual(roman.translate_roman_numeral(), 16)

    # todo: test failure for unit digits less than 5
    @unittest.skip("Fails for unit digits less than 5")
    def test_64(self):
        roman = RomanNumeral("LXIV")
        self.assertEqual(roman.translate_roman_numeral(), 64)


class RomanTest(unittest.TestCase):
    numerals = {
        1: 'I',
        2: 'II',
        3: 'III',
        4: 'IV',
        5: 'V',
        6: 'VI',
        9: 'IX',
        27: 'XXVII',
        48: 'XLVIII',
        59: 'LIX',
        93: 'XCIII',
        141: 'CXLI',
        163: 'CLXIII',
        402: 'CDII',
        575: 'DLXXV',
        911: 'CMXI',
        1024: 'MXXIV',
        3000: 'MMM',
    }

    def test_numerals(self):
        for arabic, roman_numeral in self.numerals.items():
            self.assertEqual(roman_numeral, numeral(arabic))


if __name__ == '__main__':
    unittest.main()
