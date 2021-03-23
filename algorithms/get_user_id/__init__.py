import re
from string import punctuation


def get_users_ids(phrase):
    """
    Gets user ids from a phrase
    :param phrase: The phrase which will contain uid and other symbols
    :return: the user id without uid and other symbols
    :rtype: list
    """

    # list to add every word that has been altered
    output = []

    # split the phrase into a list, with each word as an element, first remove all the white spaces
    # and lower the words
    phrase = phrase.strip().lower()

    # split it into a list by either spaces, or commas
    phrase = re.split(",|\s", phrase)

    # create a map to remove all the punctuation characters to empty strings
    translator = str.maketrans("", "", punctuation)

    # for each word in the phrase, remove the uid and the punctuation marks
    for word in phrase:
        # removes all the punctuation marks
        word = word.translate(translator)
        output.append(re.sub(r"(uid)", "", word, 1))

    return output
