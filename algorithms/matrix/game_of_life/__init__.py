from typing import List


def game_of_life(board: List[List[int]]) -> None:
    # Store the board’s dimensions
    rows = len(board)
    cols = len(board[0])

    # Offsets to generate the 8 neighbors (order doesn't matter)
    neighbors = [-1, 0, 1]

    # Pass 1: mark transitions in place
    # Encoding:
    #   -1 : was 1, becomes 0   (live → dead)
    #    2 : was 0, becomes 1   (dead → live)
    for row in range(rows):
        for col in range(cols):
            liveNeighbors = 0

            # Count originally-live neighbors around (row, col)
            for i in range(3):
                for j in range(3):
                    # Skip (0,0) so we don't count the cell itself
                    if not (neighbors[i] == 0 and neighbors[j] == 0):
                        r = row + neighbors[i]
                        c = col + neighbors[j]

                        # In bounds and originally alive?
                        # abs(...) == 1 is true for 1 and -1 (originally live),
                        # and false for 0 and 2 (originally dead)
                        if 0 <= r < rows and 0 <= c < cols and abs(board[r][c]) == 1:
                            liveNeighbors += 1

            # Apply Conway's rules using the cell's original state
            if board[row][col] == 1 and (liveNeighbors < 2 or liveNeighbors > 3):
                board[row][col] = -1  # live → dead (under/overpopulation)

            if board[row][col] == 0 and liveNeighbors == 3:
                board[row][col] = 2  # dead → live (reproduction)

    # Pass 2: normalize markers to final 0/1 states
    for row in range(rows):
        for col in range(cols):
            board[row][col] = 1 if board[row][col] > 0 else 0

    return board
