def odd_occurences_in_array(a):
    """
    Finds the odd number of occurences of an element in an array
    :param a
    """
    result = 0

    for number in a:
        result = result ^ number
    return result