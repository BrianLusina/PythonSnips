from random import seed, choice
from string import ascii_lowercase
from time import time


class Cipher(object):

    def __init__(self, key=None):
        if not key:
            seed(time())
            key = ''.join(choice(ascii_lowercase) for _ in range(100))
        elif not key.isalpha() or not key.islower():
            raise ValueError('Wrong key parameter!')
        self.key = key

    def encode(self, text):
        text = ''.join(c for c in text if c.isalpha()).lower()
        key = self.key * (len(text) // len(self.key) + 1)
        return ''.join(chr((ord(c) - 194 + ord(k)) % 26 + 97)
                       for c, k in zip(text, key))

    def decode(self, text):
        key = self.key * (len(text) // len(self.key) + 1)
        return ''.join(chr((ord(c) - ord(k) + 26) % 26 + 97)
                       for c, k in zip(text, key))


class Caesar(Cipher):

    def __init__(self):
        Cipher.__init__(self, 'd')
