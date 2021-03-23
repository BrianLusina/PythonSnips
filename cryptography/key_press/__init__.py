class KeyPress(object):
    def __init__(self, phrase):
        self.phrase = phrase

    def presses(self):
        """
        Create the dictionary to store the numbers as keys and the list of strings as values
        Create a counter variable to store counts whenever a letter is found in the key-value pairing.
        Convert the input string to uppercase for easier dictionary 'parsing'
        loop through dictionary keys and loop through the strings,
        checking if each letter in the string is in the value of the key(list).
         :returns key count, how many presses are made on the keypad
        """

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

    def presses_v2(self):
        BUTTONS = ['1', 'abc2', 'def3',
                   'ghi4', 'jkl5', 'mno6',
                   'pqrs7', 'tuv8', 'wxyz9',
                   '*', ' 0', '#']
        return sum(1 + button.find(c) for c in self.phrase.lower() for button in BUTTONS if c in button)

    # using lambda expression
    presses_v3 = lambda s: sum((c in b) * (1 + b.find(c)) for c in s.lower() for b in
                               '1,abc2,def3,ghi4,jkl5,mno6,pqrs7,tuv8,wxyz9,*, 0,#'.split(","))
