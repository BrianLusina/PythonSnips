import unittest


class RomanNumeral(object):
    """
    Create a dictionary that contains the Roman numerals conversions and their Arabic numbers
    """
    ROMANS = {"I": 1, "II": 2, "III": 3, "IV": 4, "V": 5, "VI": 6, "VII": 7, "VIII": 8, "IX": 9, "X": 10,
             "XX": 20, "XXX": 30,"XL": 40, "L": 50, "LX": 60, "LXX": 70, "LXXX": 80, "XC": 90,
              "C": 100, "CC": 200, "CCC": 300, "CD": 400,"D": 500, "DC": 600, "DCC": 700, "DCCC": 800, "CM": 900
              "M": 1000, "MM": 2000, "MMM": 3000}

    def __init__(self, number):
        self.number = number

    def translate_roman_numeral(self):
        self.ROMANS.get(self.number)

class RomanTests(unittest.TestCase):
    def test_1(self):
        roman = RomanNumeral("IV")
        self.assertEqual(roman.translate_roman_numeral(), 4)

    def test_2(self):
        roman = RomanNumeral("LX")
        self.assertEqual(roman.translate_roman_numeral(), 60)