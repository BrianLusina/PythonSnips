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

    - Create and initialize variables:
        start_row_index – starting row index
        end_row_index – ending row index
        start_col_index - starting column index
        end_col_index – ending column index
    - Run a loop until all the squares of loops are printed.
    - In each outer loop traversal print the elements of a square in a clockwise manner.
    - Print the top row, i.e. Print the elements of the start_row_index'th row from column index start_col_index to
        end_col_index, and increase the count of start_row_index.
    - Print the right column, i.e. Print the last column or (end_col_index - 1)'th column from row index start_row_index
        to end_row_index and decrease the count of end_col_index
    - Print the bottom row, i.e. if start_row_index < end_row_index, then print the elements of (end_row_index - 1)th
        row from column (end_col_index - 1) to start_col_index and decrease the count of end_row_index
    - Print the left column, i.e. if start_col_index < end_col_index, then print the elements of start_col_index'th
        column from (end_row_index - 1)th row to start_row_index and increase the count of start_col_index.

    Complexity Analysis:

    Time Complexity: O(m * n).
    To traverse the matrix O(m * n) time is required where m is the number of rows and n is the number of columns

    Space Complexity:
        O(1): without considering the output array, since we don't use any additional data structures for our
        computations. No extra space is required.
        O(n): it the output array is taken into account

    @param matrix: 2D array indicating the matrix
    @type matrix list
    @return: an array of the matrix in spiral form
    @rtype: list
    """
    start_row_index = 0
    start_col_index = 0

    # this is the number of rows
    end_row_index = len(matrix)

    # number of columns
    end_col_index = len(matrix[0])

    spiral_matrix_form = []

    while start_row_index < end_row_index and start_col_index < end_col_index:
        """
        Getting the items from rows moving left to right
        
        To do this, we iterate on the columns of the first row or the items in the first
        array in the matrix. this will be a range from the start_col_index to the end_col_index. Moving us from left to 
        right. To get the items we need from this row, we use the start_row_index and the col_num. The start row_index
        is the first row in the matrix at the first iteration, while the col_num will move from left to right thus 
        picking each element in the first row.
        
        We then increment the start_row_index, to move to the next row
        """

        for col_num in range(start_col_index, end_col_index):
            item = matrix[start_row_index][col_num]
            spiral_matrix_form.append(item)

        # increment the row index
        start_row_index += 1

        """
        Getting items from the end columns or from top to bottom. 
        
        To get the last column in our matrix we move down the matrix from top to bottom on the
        last column. we iterate on the row indices or number of rows, that will be provided or shown by the 
        start_row_index which will have been incremented from the first or initial for loop and up to, but not including
        the end_row_index which will be the last row in the matrix.
        To get an item, we get each item in the column using the row_num which is the result of ranging from 
        start_row_index to end_row_index and getting each last item in each row as shown with end_col_index - 1, becase
        of 0-based-indexing. these items are now added to the final list/array
        
        After this we decrement the end_col_index by 1 in order to move to the next column from the end allowing us to
        move from right to left
        """
        for row_num in range(start_row_index, end_row_index):
            item = matrix[row_num][end_col_index - 1]
            spiral_matrix_form.append(item)

        # decrement the col index
        end_col_index -= 1

        """
        Getting items on the bottom rows from right to left.
        
        First we check if the current start_row_index is less than the end_row_index
        
        Moving from right to left we move against the columns & to do this, we shall move backwards in the range from
        end_col_index to the start_col_index moving 1 step at a time. Because from previous iterations we have already
        gotten the bottom right item, we shall start on the left of the bottom_right_item, which will be given by
        end_col_index - 1 up to, but not including the item at the bottom right of the matrix.
        
        To get items on this row, we shall use the end_row_index which will let us traverse items on the last row, 
        moving column by column.
        
        We then decrement the end_row_index in order to move up the matrix in subsequent operations
        """

        if start_row_index < end_row_index:

            for col_num in range(end_col_index - 1, start_col_index - 1, -1):
                item = matrix[end_row_index - 1][col_num]
                spiral_matrix_form.append(item)

            end_row_index -= 1

        """
        Getting items on the left columns, i.e from bottom to top
        
        We move along the leftmost column by moving from bottom rows to top rows. We do this by using the end_row_index 
        - 1 which will give us inner rows. And using the start_row_index - 1 will also give us the inner rows. This will
        have been incremented by 1 in previous iterations.
        
        To get items on this column, we traverse the row numbers from the range of end_row_index - 1 to 
        start_row_index - 1, getting each item on this column.
        
        We increment the start_col_index by 1 in order to move from left to right within our matrix
        """
        if start_col_index < end_col_index:

            for row_num in range(end_row_index - 1, start_row_index - 1, -1):
                item = matrix[row_num][start_col_index]
                spiral_matrix_form.append(item)

            start_col_index += 1

    return spiral_matrix_form
