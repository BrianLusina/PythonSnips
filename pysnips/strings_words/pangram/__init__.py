from string import ascii_lowercase


class Pangram:
    def __init__(self, s):
        self.s = s

    def is_pangram(self):
        return not set(ascii_lowercase) - set(self.s.lower())
