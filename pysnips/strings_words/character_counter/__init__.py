from pysnips.errors import PySnipsError
try:
    from functools import reduce
except ImportError:



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
        raise PySnipsError("ParameterError", "Expect input to be a list")

    # create a variable to hold current total
    total_chars = 0

    # reduce the array to