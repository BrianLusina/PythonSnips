def denumerate(enum_list):
    """
    denumerates a list of tuples into a word
    :param enum_list: list of tuples with the 1st index in the tuple being the position of the letter
    (the 2nd elem)
    :return: a word formed from the 'denumeration' or False if it does not start from 0
    :rtype: str or bool
    """
    try:
        # create a key-value pairing formt the list provided.
        numbers = dict(enum_list)

        # returns the largest key and adds 1 to it
        maximum = max(numbers) + 1

        # creates the string result from the dictionary and a range which will get the keys and return their values
        result = "".join(numbers[x] for x in range(maximum))

        # if the result is alphanumeric and the length is equal to the maximum, return it
        if result.isalnum() and len(result) == maximum:
            return result
    except (KeyError, ValueError, TypeError):
        return False
    return False
