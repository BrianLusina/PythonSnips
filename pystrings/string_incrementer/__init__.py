import re
from itertools import takewhile


def increment_string(word):
    if word == "":
        return "1"

    word_pattern = r"[a-zA-Z]*"
    number_pattern = r"(?P<numbers>[0-9]*)$"
    word_match = re.match(word_pattern, word)
    number_match = re.search(number_pattern, word)
    number = number_match.group("numbers")

    if number:
        leading_zeroes = "".join(["0" for _ in takewhile("0".__eq__, number)])
        new_number = f"{leading_zeroes}{int(number) + 1}"

    # find the number at the end of the word
    # increment it by 1
    # append it to the string
    # if the word does not have a number, add 1 to it
    return word
