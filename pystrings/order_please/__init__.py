import collections
import re


def order(sentence):
    """
    Split the string into a list,
    Loop through it checking if the number in the string is greater than the number in the next string
    if the current string has a number that is less than the next, add it to a result string
    """
    # split the string
    sent_li = sentence.split(" ")
    # stores the words as keys and the digits within words as keys
    word_dict = {}

    for word in sent_li:
        # check for the digit in the word
        for let in word:
            if re.match("[0-9]", let):
                word_dict[let] = word
    # sort the dict by keys and return the values
    result = collections.OrderedDict(sorted(word_dict.items()))
    return " ".join([v for k, v in result.items()])


def order_2(words):
    return ' '.join(sorted(words.split(), key=lambda w: sorted(w)))
