"""
Evaluates whether a 2d array is a magic square. where the sum of each row, column and diagonal are equal
"""


def magic_square(array):
    """

    :param array:A 2D array
    :return: True or False whether the array is a magic squre
    :rtype: bool
    """
    if array is None or not isinstance(array, list):
        return False
    if len(array) == 0:
        return False
