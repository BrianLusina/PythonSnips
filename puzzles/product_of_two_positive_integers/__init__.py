def recursive_multiply(x: int, y: int) -> int:
    """Uses recursion to find the product of x and y
    Args:
        x (int): first number
        y (int): second number
    Returns:
        int: result of multiplication
    """
    # this cuts down the recursive calls
    if x < y:
        return recursive_multiply(y, x)
    if y == 0:
        return 0
    return x + recursive_multiply(x, y - 1)