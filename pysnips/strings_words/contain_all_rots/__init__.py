def contain_all_rots(word, word_list):
    """
    Checks if the word_list contains all the rotations of the word
    Returns true if all rotations are found, false otherwise
    If the word is an empty string the function will return True early
    First, gets all possible rotations of the word and checks if all the possible rotations are in the
    word_list
    :param word: The word to check for
    :param word_list: The list of possible rotations for the word
    :return: True if the word_list contains all rotations of the word
    :rtype: bool
    """

    # return early if the string is empty
    if word == "":
        return True
    # get all the rotations of the word
    rotations = word_rotations(word)

    # check if all these rotations are in the word_list
    return set(word_list).issuperset(rotations)


def word_rotations(word):
    """
    Gets all possible rotations of a word and stores them in a list
    checks if a given rotation has already appeared. If so -- the sequence is periodic and you have already discovered
     all distinguishable rotations, so just return the result:
    :param word: The word to check for
    :return: A list of all possible rotations of the word
    :rtype: list
    """
    result = set()
    for mid in range(len(word)):
        rot = word[mid:] + word[:mid]
        if rot in result:
            return result
        else:
            result.add(rot)

    return list(result)
