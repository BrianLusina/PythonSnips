def integer_square_root(k: int) -> int:
    """
    Finds the largest number whose square is less than or equal to the specified integer k

    Args:
        k (int): integer number to find the largest number whose square is less than or equal to this.
    Returns:
        int: largest number whose square is less than or equal to the specified integer
    """
    left = 0
    right = k

    while left <= right:
        mid = (left + right) // 2
        mid_squared = mid * mid

        if mid_squared <= k:
            left = mid + 1
        else:
            right = mid - 1

    return left - 1
