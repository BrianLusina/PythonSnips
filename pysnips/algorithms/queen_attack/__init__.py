def board(pos1, pos2):
    """
    Draws out a board with the positions of the two queens and places both queens on it
    :param pos1: Position of W queen
    :param pos2: Position of B queen
    :return: A well drawn out board with both queens
    :rtype: list
    """
    # first validate the positions before drawing out the board
    validate_position(pos1, pos2)

    # unpack the coordinates
    x1, y1 = pos1
    x2, y2 = pos2

    # draw the board
    chess_board = [["_"] * 8 for _ in range(8)]

    # place the queens in the positions
    chess_board[x1][y1] = "W"
    chess_board[x2][y2] = "B"

    # return the chess board
    return ["".join(r) for r in chess_board]


def can_attack(pos1, pos2):
    """
    Checks if either queen can attack the other, this is only possible if they share a diagonal
    or if they share the same path.

    :param pos1: position of white queen
    :param pos2: position of black queen
    :return: True/ False, if either can attack the other
    :rtype: bool
    """
    # validate the queen position
    validate_position(pos1, pos2)

    # unpack the coordinates for W queen
    x1, y1 = pos1
    # unpack B queen coordinates
    x2, y2 = pos2

    # get the difference of the coordinates
    dx = x1 - x2 if x1 >= x2 else x2 - x1
    dy = y1 - y2 if y1 >= y2 else y2 - y1

    # check if they share a diagonal or path
    if dx == dy or dy == 0 or dx == 0:
        return True
    return False


def validate_position(pos1, pos2):
    """
    This validates the position of both queens.
    If the queens' coordinates are not on the board, a value error is raised.
    If they are both on the same square, a value error is raised as well.
    :param pos1: position of white queen
    :param pos2: position of black queen
    :raises: ValueError
    """
    if any(x < 0 or x > 7 for x in pos1 + pos2):
        raise ValueError("Invalid queen position. Queen out of board.")
    if pos1 == pos2:
        raise ValueError("Both queens are on the same square {}".format(pos1))
