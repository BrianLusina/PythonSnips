def binary_search(arr, key):
    """
    Searches for the key in a list and returns the position of the key in the array.
    If the key can not be found in the list, raise a ValueError
    Will keep shifting the middle point for as long as the middle value is not equal to the search key
    If, the search key is less than the middle value, we shift the high point by the middle value - 1
    the same applies if the key is greater than the low point, only difference is, we increase the low point by 1
    :param arr: The array, which will be a list of numbers
    :param key: search key, what we will search for
    :return: Position of the key in the array
    :raises: ValueError if the key is not in the array
    """
    low = 0
    high = len(arr) - 1
    while low <= high:
        middle = (low + high) // 2
        if arr[middle] > key:
            high = middle - 1
        elif arr[middle] < key:
            low = middle + 1
        else:
            return middle
    raise ValueError("Value not found")
