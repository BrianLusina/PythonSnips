from typing import List, Set


def is_valid_sudoku(board: List[List[str]]) -> bool:
    """
    Checks if a given sudoku board is a valid sudoku board. This does not check if the board is solvable. If the board
    is valid, it returns True, if not returns False. The board is a 9x9 grid with 3x3 cells. Each row only contains
    digits from 1-9, and each column contains digits from 1-9 repeated once. Each 3x3 cell only contains digits from 1-9
    repeated once
    Args:
        board(list): A 2D grid representing a sudoku board
    Returns:
        bool: True if the board provided is valid, False otherwise
    """
    # Handles edge cases to check if the board is of length 9
    if len(board) != 9:
        return False

    # Validate each row has exactly 9 columns
    if any(len(row) != 9 for row in board):
        return False

    number_of_rows = len(board)
    number_of_columns = len(board[0])
    row_sets: List[Set[str]] = [set() for _ in range(number_of_rows)]
    col_sets: List[Set[str]] = [set() for _ in range(number_of_columns)]
    box_sets: List[Set[str]] = [set() for _ in range(number_of_rows)]

    for row in range(number_of_rows):
        for col in range(number_of_columns):
            cell = board[row][col]
            # if the cell is empty, contains a '.', we don't need to check if, we can skip and continue to the next
            # iteration
            if cell == ".":
                continue

            # Identifying a cell within a sub-box can be found using the formula: i = (r//3)*3+(c//3) where r is the row number
            # and c is the column number all indexed from 0
            # The box_idx identifies the box this cell is in
            box_idx = (row // 3) * 3 + (col // 3)

            # Check if we have seen the digit before in the row, column or the box
            if (
                cell in row_sets[row]
                or cell in col_sets[col]
                or cell in box_sets[box_idx]
            ):
                return False

            # if not there, we add it to the row, column and sub box sets
            row_sets[row].add(cell)
            col_sets[col].add(cell)
            box_sets[box_idx].add(cell)

    return True
