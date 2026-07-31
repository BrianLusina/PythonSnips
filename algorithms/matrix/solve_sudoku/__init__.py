from typing import List


def solve_sudoku(board: List[List[str]]) -> None:
    """
    Solves a Sudoku puzzle using backtracking.
    Modifies the board in-place.
    """

    def backtrack(index):
        """
        Recursively fill empty cells using DFS backtracking.

        Args:
            index: Current index in the empty_cells list
        """
        nonlocal solved

        # Base case: all empty cells have been filled successfully
        if index == len(empty_cells):
            solved = True
            return

        # Get the current empty cell's position
        row_idx, col_idx = empty_cells[index]

        # Try each digit from 1 to 9
        for digit in range(9):
            # Check if placing digit+1 is valid in current position
            if (
                not row_used[row_idx][digit]
                and not col_used[col_idx][digit]
                and not block_used[row_idx // 3][col_idx // 3][digit]
            ):
                # Mark the digit as used in row, column, and 3x3 block
                row_used[row_idx][digit] = True
                col_used[col_idx][digit] = True
                block_used[row_idx // 3][col_idx // 3][digit] = True

                # Place the digit on the board
                board[row_idx][col_idx] = str(digit + 1)

                # Recursively solve for the next empty cell
                backtrack(index + 1)

                # If solution found, stop backtracking
                if solved:
                    return

                # Backtrack: undo the current placement
                row_used[row_idx][digit] = False
                col_used[col_idx][digit] = False
                block_used[row_idx // 3][col_idx // 3][digit] = False

    # Initialize tracking arrays for used digits
    # row_used[i][d] = True if digit d+1 is used in row i
    row_used = [[False] * 9 for _ in range(9)]
    # col_used[j][d] = True if digit d+1 is used in column j
    col_used = [[False] * 9 for _ in range(9)]
    # block_used[bi][bj][d] = True if digit d+1 is used in block (bi, bj)
    block_used = [[[False] * 9 for _ in range(3)] for _ in range(3)]

    # List to store positions of empty cells
    empty_cells = []

    # Flag to indicate if solution is found
    solved = False

    # Initialize the board state and collect empty cells
    for row_idx in range(9):
        for col_idx in range(9):
            if board[row_idx][col_idx] == ".":
                # Record empty cell position
                empty_cells.append((row_idx, col_idx))
            else:
                # Mark existing digits as used
                digit = int(board[row_idx][col_idx]) - 1
                row_used[row_idx][digit] = True
                col_used[col_idx][digit] = True
                block_used[row_idx // 3][col_idx // 3][digit] = True

    # Start solving from the first empty cell
    backtrack(0)


def solve_sudoku_2(board: List[List[str]]) -> None:
    """
    Solves a Sudoku puzzle using backtracking.
    Modifies the board in-place.
    """

    def get_possible_numbers(i, j):
        # Find all entries currently in the row
        row_entries = board[i]

        # Find all entries currently in the column
        col_entries = [row[j] for row in board]

        subox_entries = []

        subox_row = (i // 3) * 3
        subox_col = (j // 3) * 3

        # Find all entries currently in the 3x3 sub-box
        for r in range(subox_row, subox_row + 3):
            for c in range(subox_col, subox_col + 3):
                subox_entries.append(board[r][c])

        # Find all invalid entries by taking union of the three sets
        invalid_entries = row_entries + col_entries + subox_entries

        # Return all possible numbers
        return [
            e
            for e in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
            if e not in invalid_entries
        ]

    def solve_sudoku_rec(i, j):
        # All rows have been traversed representing the board has been completely filled
        if i == 9:
            return True

        # A complete row has been traversed
        if j == 9:
            return solve_sudoku_rec(i + 1, 0)

        # Continue to the next cell if the current cell is already fill
        if board[i][j] != ".":
            return solve_sudoku_rec(i, j + 1)

        # Find all possible numbers for the empty cell
        possible_numbers = get_possible_numbers(i, j)

        # Try all possible numbers
        for n in possible_numbers:
            board[i][j] = n
            if solve_sudoku_rec(i, j):
                return True
            board[i][j] = "."

        # Backtrack
        return False

    solve_sudoku_rec(0, 0)
