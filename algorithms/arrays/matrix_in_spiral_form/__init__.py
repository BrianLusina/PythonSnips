from typing import List


def matrix_in_spiral_form(matrix: List[List[int]]) -> List[int]:
    """
    The problem can be solved by dividing the matrix into loops or squares or boundaries. It can be seen that the
    elements of the outer loop are printed first in a clockwise manner then the elements of the inner loop is printed.
    So printing the elements of a loop can be solved using four loops which prints all the elements. Every ‘for’ loop
    defines a single direction movement along with the matrix. The first for loop represents the movement from left to
    right, whereas the second crawl represents the movement from top to bottom, the third represents the movement from
    the right to left, and the fourth represents the movement from bottom to up.

    Algorithm:

    - Create and initialize variables k – starting row index, m – ending row index, l – starting column index, n –
    ending column index
    - Run a loop until all the squares of loops are printed.
    - In each outer loop traversal print the elements of a square in a clockwise manner.
    - Print the top row, i.e. Print the elements of the kth row from column index l to n, and increase the count of k.
    - Print the right column, i.e. Print the last column or n-1th column from row index k to m and decrease the count of
    n
    - Print the bottom row, i.e. if k < m, then print the elements of m-1th row from column n-1 to l and decrease the
    count of m
    - Print the left column, i.e. if l < n, then print the elements of lth column from m-1th row to k and increase the
    count of l.

    Complexity Analysis:

    Time Complexity: O(m*n).
    To traverse the matrix O(m*n) time is required.
    Space Complexity: O(1).
    No extra space is required.

    @param matrix:
    @return:
    """
    start_row_index = 0
    start_col_index = 0

    # this is the number of rows
    end_row_index = len(matrix)

    # number of columns
    end_col_index = len(matrix[0])

    spiral_matrix_form = []

    while start_row_index < end_row_index and start_col_index < end_col_index:
        # get the first row
        for x in range(start_col_index, end_col_index):
            spiral_matrix_form.append(matrix[start_row_index][x])

        # increment the row index
        start_row_index += 1

        # get the last column
        for y in range(start_row_index, end_row_index):
            spiral_matrix_form.append(matrix[y][end_col_index - 1])

        # decrement the col index
        end_col_index -= 1

        # get the last row
        if start_row_index < end_row_index:

            for i in range(end_col_index - 1, start_col_index - 1, -1):
                spiral_matrix_form.append(matrix[end_row_index - 1][i])

            end_row_index -= 1

        # get the first column
        if start_col_index < end_col_index:

            for i in range(end_row_index - 1, start_row_index - 1, -1):
                spiral_matrix_form.append(matrix[i][start_col_index])

            start_col_index += 1

    return spiral_matrix_form
