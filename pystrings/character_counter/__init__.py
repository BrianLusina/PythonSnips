try:
    from functools import reduce
except ImportError:
    print("No Module named reduce")


def total_characters(word_list):
    """
    Counts the total number of characters in a word list. Accepts a word list where each element
    is a word. Throws an Exception whenever an invalid parameter is used.
    :param word_list: string word list
    :return: total number of characters
    :raises: TypeError
    :rtype: int
    """
    # check for valid parameters
    if word_list is None or not isinstance(word_list, list):
        raise Exception("ParameterError", "Expect input to be a list")

    # create a variable to hold current total
    total_chars = 0

    # perform a loop to check if each element in word list is a string
    for x in range(len(word_list)):
        if isinstance(word_list[x], str):
            total_chars += len(word_list[x])
        else:
            total_chars += 0
    return total_chars
