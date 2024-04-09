def reverse_vowels(word: str) -> str:
    word_length = len(word)

    if word_length <= 1:
        return word

    characters = list(word)
    left_pointer = 0
    right_pointer = word_length - 1

    while left_pointer < right_pointer:
        # move the left pointer until we get to a vowel
        while left_pointer < right_pointer and not is_vowel(characters[left_pointer]):
            left_pointer += 1

        # move the right pointer until we get to a vowel
        while left_pointer < right_pointer and not is_vowel(characters[right_pointer]):
            right_pointer -= 1

        characters[left_pointer], characters[right_pointer] = (
            characters[right_pointer],
            characters[left_pointer],
        )

        left_pointer += 1
        right_pointer -= 1

    return "".join(characters)


def is_vowel(letter: str) -> bool:
    vowels = {
        "a": True,
        "A": True,
        "e": True,
        "E": True,
        "i": True,
        "I": True,
        "o": True,
        "O": True,
        "u": True,
        "U": True,
    }
    return vowels.get(letter, False)
