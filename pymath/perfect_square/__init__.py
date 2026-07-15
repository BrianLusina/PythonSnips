from math import sqrt


def is_square(n: int) -> bool:
    """
    Checks if a number is a perfect square.
    Args:
        n (int): The number to check.
    Returns:
        bool: True if n is a perfect square, False otherwise.
    """
    if n < 0:
        return False
    else:
        return sqrt(n).is_integer()


def is_perfect_square(n: int) -> bool:
    """
    Checks if a number is a perfect square.
    Args:
        n (int): The number to check.
    Returns:
        bool: True if n is a perfect square, False otherwise.
    """
    if n < 0:
        return False
    sqrt_num = int(sqrt(n))
    return sqrt_num * sqrt_num == n


def num_squares(n: int) -> int:
    """
    Finds the least number of perfect square numbers that sum to n.
    Args:
        n (int): The target number to find the least number of perfect square numbers that sum to it.
    Returns:
        int: The least number of perfect square numbers that sum to n.
    """
    if n < 0:
        raise ValueError("n must be non-negative")
    if n == 0:
        return 0

    dp = [float("inf")] * (n + 1)
    dp[0] = 0

    for i in range(1, n + 1):
        j = 1
        while j * j <= i:
            dp[i] = min(dp[i], dp[i - j * j] + 1)
            j += 1

    return dp[n]


def num_squares_2(n: int) -> int:
    """
    Finds the least number of perfect square numbers that sum to n.
    Args:
        n (int): The target number to find the least number of perfect square numbers that sum to it.
    Returns:
        int: The least number of perfect square numbers that sum to n.
    """
    if n < 0:
        raise ValueError("n must be non-negative")
    if n == 0:
        return 0

    # Apply reduction by removing factors of 4
    while n % 4 == 0:
        n = n // 4

    # Check if n is of form (8k + 7)
    if n % 8 == 7:
        return 4

    # Check if n itself is a perfect square
    if is_perfect_square(n):
        return 1

    # Check if n is the sum of two perfect squares
    for value in range(1, int(sqrt(n)) + 1):
        if is_perfect_square(n - value * value):
            return 2

    return 3
