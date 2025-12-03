from typing import List


def lucky_numbers(matrix: List[List[int]]) -> List[int]:
    """
    This function takes a matrix as input and returns a list containing the lucky number(s) if they exist.

    A lucky number is a number that is the maximum of the minimum values from each row and the minimum of the maximum
    values from each column.

    If a lucky number exists, the function returns a list containing that number. Otherwise, it returns an empty list.

    Time Complexity: O(m * n) where m is the number of columns and n is the number of rows in the matrix.
    Space Complexity: O(1) as we are using a constant amount of extra space.

    Args:
        matrix (List[List[int]]): The input matrix.

    Returns:
        List[int]: A list containing the lucky number(s) if they exist, otherwise an empty list.
    """
    row_length = len(matrix)
    col_length = len(matrix[0])

    # initialize a variable to keep track of the maximum of the minimum values from each row
    r_largest_min = float("-inf")

    # We start by iterating over the rows to find the minimum values. Out of those minimum values, we choose the
    # largest minimum value and store it in r_largest_min
    for i in range(row_length):
        # find the minimum value in current row
        row_min = min(matrix[i])
        # update r_largest_min to be the maximum of current r_largest_min and the current row minimum
        r_largest_min = max(r_largest_min, row_min)

    # initialize a variable to keep track of the minimum of the maximum values from each column
    c_smallest_max = float("inf")
    # Similarly, we calculate the maximum values in columns and after finding all the largest values, we choose the
    # smallest of them and store them in c_smallest_max
    for c in range(col_length):
        # find the maximum value in the current row
        col_max = max(matrix[r][c] for r in range(row_length))
        # update c_smallest_max to be the minium of the current c_smallest_max and the current column maximum
        c_smallest_max = min(c_smallest_max, col_max)

    # If they are, we return either of the values; r_largest_min or c_smallest_max. Otherwise if now matching value is
    # found, we return an empty matrix.

    # check if the maximum of row minima is equal to the minimum of column maxima
    if r_largest_min == c_smallest_max:
        # if they are equal, return a list containing the luky number
        return [r_largest_min]
    # Otherwise, return an empty list indicating no luky number exists
    return []


def lucky_numbers_simulation(matrix: List[List[int]]) -> List[int]:
    """
    This function takes a matrix as input and returns a list containing all the lucky number(s) if they exist.

    A lucky number is a number that is the maximum of the minimum values from each row and the minimum of the maximum
    values from each column.

    The function first calculates the minimum values from each row and the maximum values from each column, then compares
    these two lists to find the lucky number(s).

    Time Complexity: O(m * n) where m is the number of columns and n is the number of rows in the matrix.
    Space Complexity: O(m + n) as we are using two lists of size m and n respectively.

    Args:
        matrix (List[List[int]]): The input matrix.

    Returns:
        List[int]: A list containing all the lucky number(s) if they exist, otherwise an empty list.
    """
    row_length = len(matrix)
    col_length = len(matrix[0])

    row_min = []
    for i in range(row_length):
        r_min = float('inf')
        for j in range(col_length):
            r_min = min(r_min, matrix[i][j])
        row_min.append(r_min)

    col_max = []
    for i in range(col_length):
        c_max = float('-inf')
        for j in range(row_length):
            c_max = max(c_max, matrix[j][i])
        col_max.append(c_max)

    result = []
    for i in range(row_length):
        for j in range(col_length):
            if matrix[i][j] == row_min[i] and matrix[i][j] == col_max[j]:
                result.append(matrix[i][j])

    return result
