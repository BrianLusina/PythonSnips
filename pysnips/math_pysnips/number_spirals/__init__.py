def diagonal_sum(n):
    """
    Finds the diagonal sum of a spiral of n by n

    An example:
    >>> diagonal_sum(5)
    101

    :param n: Number of rows and columns of the grid
    :type n int
    :return: Total of the numbers along the diagonal
    :rtype: int
    """
    count = 1
    last = 1
    total = last

    while count < 2 * n - 1:
        i = int(count * 0.5 + 1.5)
        for _ in range(4):
            last += i
            total += last
            count += 1
    return total


if __name__ == "__main__":
    number = 1001
    diag = diagonal_sum(number)
    print(f"Diagonal sum of {number} by {number} spiral is {diag}")
