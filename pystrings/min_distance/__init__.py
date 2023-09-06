def min_distance(a: str, b: str) -> int:
    """Returns the minimum number of operations required to convert a string a into string b

    Args:
        a (str): string to convert to string b
        b (str): string to be compared against
    Returns:
        int: minimum number of operations to convert from string a to string b
    """

    # edge cases
    # strings are exactly the same, so no need for performing any operations on it
    if a == b:
        return 0

    # if string a is empty, then it will need the length of string a as the number of operations
    if len(a) == 0:
        return len(b)

    m = len(a)
    n = len(b)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(m + 1):
        dp[i][0] = i

    for j in range(n + 1):
        dp[0][j] = j

    for i in range(m):
        for j in range(n):
            # swap or identical character
            x = dp[i][j] + (0 if a[i] == b[j] else 1)

            # remove last character
            y = dp[i][j + 1] + 1

            # add last character
            z = dp[i + 1][j] + 1

            dp[i + 1][j + 1] = min(x, y, z)

    return dp[m][n]
