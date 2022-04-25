import codecs


def rot13(message: str) -> str:
    """
    >>> rot13("Hello, World!")
    'Uryyb, Jbeyq!'
    """
    return codecs.encode(message, "rot13")
