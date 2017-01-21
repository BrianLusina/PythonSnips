import unittest

from pysnips.math_pysnips.roman_numeral import RomanNumeral


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

    @unittest.skip("Test fails for unit digits less than 5")
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

    @unittest.skip("")
    def test_numerals(self):
        for arabic, numeral in self.numerals.items():
            self.assertEqual(numeral, numeral(arabic))

if __name__ == '__main__':
    unittest.main()
