def duplicate_chars(word_one: str, word_two: str): bool:


if len(word_one) != len(word_two):
    return False
return set(word_one) == set(word_two)
