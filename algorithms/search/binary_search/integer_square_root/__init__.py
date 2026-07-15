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
            # this discards all the numbers less than mid, i.e. moves the left pointer to be 1 greater than mid
            left = mid + 1
        else:
            # otherwise, we discard all the numbers greater than mid, i.e. move the right pointer to 1 less than mid
            right = mid - 1

    # this becomes the largest integer whose square is less than the provided integer k
    return left - 1
