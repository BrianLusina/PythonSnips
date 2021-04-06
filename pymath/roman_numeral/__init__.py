ROMAN_MAP = ((1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'), (100, 'C'), (90, 'XC'), (50, 'L'),
             (40, 'XL'), (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I'))


def numeral(arabic):
    roman_number = ""
    for number, roman in ROMAN_MAP:
        while arabic >= number:
            roman_number += roman
            arabic -= number
    return roman_number


class Numerals(object):
    @staticmethod
    def int_to_roman(number):
        if type(number) != type(1):
            raise TypeError("expected integer, got %s" % type(number))
        if not 0 < number < 4000:
            raise ValueError("Argument must be between 1 and 3999")
        ints = (1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1)
        nums = ('M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I')
        result = ""
        for i in range(len(ints)):
            count = int(number / ints[i])
            result += nums[i] * count
            number -= ints[i] * count
        return result


class RomanNumeral(object):
    """
    Create a dictionary that contains the Roman numerals conversions and their Arabic numbers
    the Keys will be ones, tens and hundreds and thousands
    :translate_roman_numeral checks if the roman numeral is in dictionary, retuns the value
    if not, loops through the dictionary, checking each string

    :translate_roman_numeral_2, uses a ROMAN_LIST to loop through each value and number and checks
    """
    ROMANS = {
        "I": 1, "II": 2, "III": 3, "IV": 4, "V": 5, "VI": 6, "VII": 7, "VIII": 8, "IX": 9, "X": 10,
        "XX": 20, "XXX": 30, "XL": 40, "L": 50, "LX": 60, "LXX": 70, "LXXX": 80, "XC": 90,
        "C": 100, "CC": 200, "CCC": 300, "CD": 400, "D": 500, "DC": 600, "DCC": 700, "DCCC": 800,
        "CM": 900, "M": 1000, "MM": 2000, "MMM": 3000
    }

    ROMAN_LIST = [
        ["M", 1000], ["D", 500], ["C", 100], ["XC", 90], ["L", 50], ["X", 10], ["V", 5], ["IV", 4],
        ["I", 1]
    ]

    def __init__(self, number):
        self.number = number

    # todo: test fails for roman numerals with unit digit being less than 5
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

    def translate_roman_numeral_v3(self):
        if type(self.number) != type(""):
            raise TypeError("expected string, got %s" % type(self.number))
        else:
            num = self.number
            nums = ['M', 'D', 'C', 'L', 'X', 'V', 'I']
            ints = [1000, 500, 100, 50, 10, 5, 1]
            places = []
            for c in num:
                if not c in nums:
                    raise ValueError("input is not a valid roman numeral: %s" % self.number)
            for i in range(len(num)):
                c = num[i]
                value = ints[nums.index(c)]
                # If the next place holds a larger number, this value is negative.
                try:
                    nextvalue = ints[nums.index(num[i + 1])]
                    if nextvalue > value:
                        value *= -1
                except IndexError:
                    # there is no next place.
                    pass
                places.append(value)
            sum = 0

            # Easiest test for validity...
            for n in places:
                sum += n
            if Numerals.int_to_roman(sum) == input:
                return sum
            else:
                raise ValueError('input is not a valid roman numeral: %s' % self.number)
