import unittest


class RomanNumeral(object):
    """
    Create a dictionary that contains the Roman numerals conversions and their Arabic numbers
    the Keys will be ones, tens and hundreds and thousands
    :translate_roman_numeral checks if the roman numeral is in dictionary, retuns the value
    if not, loops through the dictionary, checking each string
    """
    ROMANS = {"I": 1, "II": 2, "III": 3, "IV": 4, "V": 5, "VI": 6, "VII": 7, "VIII": 8, "IX": 9, "X": 10,
              "XX": 20, "XXX": 30,"XL": 40, "L": 50, "LX": 60, "LXX": 70, "LXXX": 80, "XC": 90,
              "C": 100, "CC": 200, "CCC": 300, "CD": 400, "D": 500, "DC": 600, "DCC": 700, "DCCC": 800, "CM": 900,
              "M": 1000, "MM": 2000, "MMM": 3000}

    ROMAN_LIST = [["M", 1000], ["D", 500], ["C", 100], ["XC", 90], ["L", 50], ["X", 10], ["V", 5], ["IV", 4], ["I", 1]]

    def __init__(self, number):
        self.number = number

    # test fails for roman numerals with unit digit being less than 5
    def translate_roman_numeral(self):
        arabic_no = 0
        if self.number in self.ROMANS:
            return self.ROMANS.get(self.number)
        else:
            for x in self.number:
                arabic_no += self.ROMANS.get(x)
        return arabic_no

    # variation two of the translate roman numeral
    def translate_roman_numeral_v2(self):
        num_str = self.number.upper()
        arabic_no = 0
        if isinstance(int(num_str), int):
            raise TypeError("Please input a string")
        else:
            for letter, value in self.ROMAN_LIST:
                if num_str.startswith(letter):
                    num_str = num_str[1:]
                    arabic_no += value
            return arabic_no


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

    def test_64(self):
        roman = RomanNumeral("LXIV")
        self.assertEqual(roman.translate_roman_numeral(), 64)


