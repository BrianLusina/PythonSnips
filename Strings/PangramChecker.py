class Pangram:
    def __init__(self,s):
        self.s = s

    def is_pangram(self):
        return not set(self.s.lowercase) - set(self.s.lower())

    def is_pangram_lambda(self):
        return not set('abcdefghijklmnopqrstuvwxyz') - set(self.s.lower())