def on_square(chess_square: int) -> int:
    # a left shift is equivalent to multiplying by 2.  So we need to left
    # shift by num-1 times to get the number of grains on that square
    return 1 << chess_square - 1
    # or
    # return 2 ** (chess_square - 1)


def total_after(squares: int) -> int:
    return (1 << squares) - 1
    # or
    # return sum(on_square(i) for i in range(1, squares + 1))
