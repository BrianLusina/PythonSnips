def count_palindromic_substrings(s: str) -> int:
    """
    Counts the number of palindromic substrings that can be found in the given string
    Args:
        s(str): string to check for palindromic substrings
    Returns:
        int: number of palindromic substrings
    """
    n = len(s)
    dp = [[False] * n for _ in range(n)]

    count = 0
    # Set all the strings of length 1 to true, these are all palindromes
    for i in range(n):
        count += 1
        dp[i][i] = True

    # iterate over pairs i, i+1, checking if they are equal, if they are, then they are palindromes
    for i in range(n - 1):
        if s[i] == s[i + 1]:
            count += 1
            dp[i][i + 1] = True

    for diff in range(2, n):
        for i in range(n - diff):
            j = i + diff
            if s[i] == s[j] and dp[i + 1][j - 1]:
                count += 1
                dp[i][j] = True

    return count


def count_palindromic_substrings_2(s: str) -> int:
    """
    Counts the number of palindromic substrings that can be found in the given string
    Args:
        s(str): string to check for palindromic substrings
    Returns:
        int: number of palindromic substrings
    """
    n = len(s)
    dp = [[False] * n for _ in range(n)]

    count = 0
    # Set all the strings of length 1 to true, these are all palindromes
    for i in range(n):
        count += 1
        dp[i][i] = True

    # iterate over pairs i, i+1, checking if they are equal, if they are, then they are palindromes
    for i in range(n - 1):
        dp[i][i + 1] = s[i] == s[i + 1]
        # A boolean value is added to the count where True means 1 and False means 0
        count += dp[i][i + 1]

    # Substrings of lengths greater than 2
    for length in range(3, n + 1):
        i = 0
        # Checking every possible substring of any specific length
        for j in range(length - 1, n):
            dp[i][j] = dp[i + 1][j - 1] and (s[i] == s[j])
            count += dp[i][j]
            i += 1

    return count
