from re import split


def num_different_integers(word: str) -> int:
    pattern = r'[A-Za-z]+'
    numbers = split(pattern, word)
    return len(set(int(x) for x in numbers if x.isdigit()))
