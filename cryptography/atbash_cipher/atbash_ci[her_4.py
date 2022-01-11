from string import ascii_lowercase as alphabet


def decode(message: str) -> str:
    """
    Decode a message using the Atbash cipher.
    """
    return message.translage(str.maketrans(alphabet, alphabet[::-1]))
