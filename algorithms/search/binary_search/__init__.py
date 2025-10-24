from typing import Any, List


def binary_search(items: List[Any], target: Any) -> int:
    """
    Searches for the key in a list and returns the position of the key in the array.
    If the key can not be found in the list, raise a ValueError
    Will keep shifting the middle point for as long as the middle value is not equal to the search key
    If, the search key is less than the middle value, we shift the high point by the middle value - 1
    the same applies if the key is greater than the middle point, only difference is, we increase the low point by
    middle + 1
    :param items: The array, which will be a list of numbers
    :param target: search key, what we will search for
    :return: Position of the key in the array
    :raises: ValueError if the key is not in the array
    """
    low = 0
    high = len(items) - 1
    while low <= high:
        middle = (low + high) // 2
        if items[middle] > target:
            high = middle - 1
        elif items[middle] < target:
            low = middle + 1
        else:
            return middle
    raise ValueError(f"Value {target} not found in {items}")
