import string


def encode(plaintext):
    return _group(_codec(plaintext.lower()), 5)


def decode(cyphertext):
    return _codec(cyphertext)


def _codec(text):
    a = string.ascii_lowercase
    t = str.maketrans(a, a[::-1])
    return "".join(c.translate(t) if c.isalnum() else "" for c in text)


def _group(text, n):
    return " ".join(text[i: i + n] for i in range(0, len(text), n))
