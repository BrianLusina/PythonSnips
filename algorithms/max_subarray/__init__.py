"""
Finds the maximum sub-array in an array
"""
try:
    from collections import Iterable
except ImportError:
    from collections.abc import Iterable
try:
    from sys import maxsize as maxint
except ImportError:
    from sys import maxint


def find_max_sub_array(array):
    """
    Finds the maximum sub-array in an array of integers
    Examples:
    >>> find_max_sub_array([1, 2, 3])
    6

    :param array: Array of numbers
    :type array list
    :return: Sum of sub-array that is the maximum of all sub-arrays
    :rtype: int
    """

    if array is None or not isinstance(array, Iterable):
        raise ValueError(f"Expected an iterable instead found {array}")

    if len(array) == 0:
        return 0

    max_so_far = -maxint - 1
    max_ending = 0

    for x in range(len(array)):
        max_ending = max_ending + array[x]

        if max_so_far < max_ending:
            max_so_far = max_ending

        if max_ending < 0:
            max_ending = 0

    return max_so_far


if __name__ == "__main__":
    arr = [-13, -3, -25, -20, -3, -16, -23, -12, -5, -22, -15, -4, -7]
    print(f"Maximum sub-array of {arr} is {find_max_sub_array(arr)}")
