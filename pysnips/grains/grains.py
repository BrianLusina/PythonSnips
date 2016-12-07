def on_square(chess_square):
    return 2 ** (chess_square - 1)


def total_after(squares):
    return sum(on_square(i) for i in range(1, squares + 1))
