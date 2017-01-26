def binary_search(arr: list, key: int) -> int:
    """
    Searches for the key in a list and returns the position of the key in the array.
    If the key can not be found in the list, raise a ValueErr
    :param arr: The array, which will be a list of numbers
    :param key: search key, what we will search for
    :return: Position of the key in the array
    :raises: ValueError if the key is not in the array
    """

    if key in arr:
        return arr.index(key)
    else:
        raise ValueError
