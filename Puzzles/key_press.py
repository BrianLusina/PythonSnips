import unittest


class KeyPress(object):
    """
    Create the dictionary to store the numbers as keys and the list of strings as values
    Create a counter variable to store counts whenever a letter is found in the key-value pairing.
    Convert the input string to uppercase for easier dictionary 'parsing'
    loop through dictionary keys and loop through the strings, checking if each letter in the string is in the value of the key(list).
     :returns key count, how many presses are made on the keypad
     :arg takes in a phrase
    """
    def __init__(self, phrase):
        self.phrase = phrase

    def presses(self):
        # converts the string to upper, and stores in variable,
        phrase = self.phrase.upper()  # .replace(" ", "")
        # creates a counter variable
        key_count = 0
        keys_dict = {"1": ["1"], "2": ["A", "B", "C", "2"], "3": ["D", "E", "F", "3"],
                     "4": ["G", "H", "I", "4"], "5": ["J", "K", "L", "5"], "6": ["M", "N", "O", "6"],
                     "7": ["P", "Q", "R", "S", "7"], "8": ["T", "U", "V", "8"], "9": ["W", "X", "Y", "Z", "9"],
                     "*": ["*"], "0": [" ", "0"], "#": ["#"]
                     }

        # perform loop
        for k in keys_dict.keys():
            curr_list = keys_dict.get(k)
            for letter in phrase:
                if letter in curr_list:
                    # add 1, as indexes start from 0
                    key_count += curr_list.index(letter) + 1
        return key_count


class Tests(unittest.TestCase):
    def test1(self):
        press = KeyPress("V8")
        self.assertEqual(7, press.presses())

    def test2(self):
        press = KeyPress("LOL")
        self.assertEqual(9, press.presses())

    def test3(self):
        press = KeyPress("How R u 2day")
        self.assertEqual(23, press.presses())

    def test4(self):
        press = KeyPress("i 8 2 Many mandazi 4 brekky")
        self.assertEqual(45, press.presses())

