from typing import Any, List


def binary_search(items: List[Any], target: Any, modified: bool = False) -> int:
    """
    Searches for the key in a list and returns the position of the key in the array.
    If the key can not be found in the list, raise a ValueError
    Will keep shifting the middle point for as long as the middle value is not equal to the search key
    If, the search key is less than the middle value, we shift the high point by the middle value - 1
    the same applies if the key is greater than the middle point, only difference is, we increase the low point by
    middle + 1
    Args:
        items (List[Any]): The list of items to search
        target (Any): The target to search for
        modified (bool, optional): Whether the search key should be modified or not
    Returns:
        int: The position of the key in the array
    Raises:
        ValueError: If the target is not in the array
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
    if modified:
        return low
    raise ValueError(f"Value {target} not found in {items}")
