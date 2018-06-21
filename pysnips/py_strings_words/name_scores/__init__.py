"""
Calculates the name scores of each name in the names.txt file
"""
from collections import Iterable, OrderedDict
from string import ascii_lowercase, ascii_uppercase

ALPHABET_UPPER_POSITIONS = {letter: index for index, letter in enumerate(ascii_uppercase, start=1)}
ALPHABET_LOWER_POSITIONS = {letter: index for index, letter in enumerate(ascii_lowercase, start=1)}


def name_scores(names):
    """
    Calculates the scores of each name in the names array/list. This is obtained by first sorting the array of names in
    the list and obtaining the value of each name, an example is COLIN =  3 + 15 + 12 + 9 + 14 = 53, with the example
    provided, this would end up being 1 * 53 = 53. As it is the only name in the list.
    An example:

    >>> name_scores(["COLIN"])
    53

    :param names:
    :type names list
    :return: total of all name scores
    :rtype: int
    """
    # sanity checks, ensure this is an iterable
    if not isinstance(names, Iterable):
        raise ValueError(f"Expected names to be an iterable, instead got {names}")

    # sort the list of names in alphabetical order in place
    names.sort()
    score_board = OrderedDict()

    # check the alphabetical score for each name and the position in the list
    for name in names:
        alphabetical_score = find_alphabetical_score(name)
        position = names.index(name) + 1
        score_board[name] = alphabetical_score * position

    return sum(score_board.values())


def find_alphabetical_score(name):
    """
    Finds the alphabetical score of a name. An example:

    >>> find_alphabetical_score("COLIN")
    53

    Assumption made here is that the name will be uppercase

    :param name: Name of the alphabet
    :type name str
    :return: Alphabetical score of the name
    :rtype: int
    """
    # ascertain that this will get a string
    if name is None or not isinstance(name, str):
        raise ValueError(f"Name should be a string, instead got {name}")

    # if any of the letters in the name is upper
    if any(x for x in name if x.isupper()):
        name = name.upper()
        numbers = [ALPHABET_UPPER_POSITIONS[letter] for letter in name if letter in ALPHABET_UPPER_POSITIONS]
        return sum(numbers)
    else:
        # use lower case
        name = name.lower()
        numbers = [ALPHABET_LOWER_POSITIONS[letter] for letter in name if letter in ALPHABET_LOWER_POSITIONS]
        return sum(numbers)


if __name__ == "__main__":
    file_name = "names.txt"
    with open(file_name) as name_file:
        names_list = name_file.readline().split(",")
    print(f"Name scores for {names_list} is \n {name_scores(names_list)}")
