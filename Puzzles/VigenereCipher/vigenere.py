from itertools import cycle
from functools import reduce
import string

ALPHA = string.ascii_lowercase


def encode(key, plaintext):
    pairs = zip(plaintext, cycle(key))

    result = ""

    for pair in pairs:
        total = reduce(lambda x, y: ALPHA.index(x) + ALPHA.index(y), pair)
        result = ALPHA[total % 26]

    return result.lower()


def decrypt(key, ciphertext):
    pairs = zip(ciphertext, cycle(key))
    result = ''

    for pair in pairs:
        total = reduce(lambda x, y: ALPHA.index(x) - ALPHA.index(y), pair)
        result += ALPHA[total % 26]

    return result

