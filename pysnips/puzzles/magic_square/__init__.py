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

    # summing rows
    # loop through the array summing each nested array and checking if all sums are equal
    # row_sum = all(sum(arr) == sum(array[0]) for arr in array)
    row_totals = [sum(row) for row in array]

    # check if all the rows are equal, return false early if not
    if not all(r == row_totals[0] for r in row_totals):
        return False

    # columns
    # sum the 1st element of each, 2nd element of each upto nth element of each and check if sums are equal
    # check if all the columns are equal, return false immediately if not
    col_totals = [sum(col) for col in zip(*array)]
    if not all(c == col_totals[0] for c in col_totals):
        return False

    # 2 diagonals
    # sum the 2 diagonals and check if the sum is equal
    diagonal_sum = sum((row[i]) for i, row in enumerate(array))

    # return true if all the above are equal false otherwise
    return col_totals[0] == row_totals[0] == diagonal_sum
