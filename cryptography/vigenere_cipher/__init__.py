import string
from functools import reduce
from itertools import cycle

ALPHA = string.ascii_lowercase


def encode(key, plaintext):
    pairs = zip(plaintext, cycle(key))

    result = ""

    for pair in pairs:
        total = reduce(lambda x, y: ALPHA.index(x) + ALPHA.index(y), pair)
        result += ALPHA[total % 26]

    return result.lower()


def decode(key, ciphertext):
    pairs = zip(ciphertext, cycle(key))
    result = ''

    for pair in pairs:
        total = reduce(lambda x, y: ALPHA.index(x) - ALPHA.index(y), pair)
        result += ALPHA[total % 26]

    return result


def show_result(plaintext, key):
    """Generate a resulting cipher with elements shown"""
    encrypted = encode(key, plaintext)
    decrypted = decode(key, encrypted)

    print('Key: %s' % key)
    print('Plaintext: %s' % plaintext)
    print('Encrypted: %s' % encrypted)
    print('Decrypted: %s' % decrypted)


show_result('ihadadream', 'boom')
