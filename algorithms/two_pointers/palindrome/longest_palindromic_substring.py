from . import is_palindrome


def longest_palindromic_substring(phrase: str) -> str:
    """Finds the longest palindromic substring from a given string and returns it. If the string has
    more than 1 palindromic substring, the first is returned, that is, the first with the lowest index.

    Args:
        phrase (str): string to search palindrome substrings for

    Returns:
        str: first longest palindromic substring
    """
    if len(phrase) <= 1 or is_palindrome(phrase):
        return phrase

    n = len(phrase)
    dp = [[False] * n for _ in range(n)]

    # will hold the inclusive bounds for the answer
    result = [0, 0]

    # set all to True, all strings of length 1 are palindromes
    for i in range(n):
        dp[i][i] = True

    # iterate over pairs i, i+1, checking if they are equal, if they are, then they are palindromes
    for i in range(n - 1):
        if phrase[i] == phrase[i + 1]:
            dp[i][i + 1] = True
            result = [i, i + i]

    for diff in range(2, n):
        for i in range(n - diff):
            j = i + diff
            if phrase[i] == phrase[j] and dp[i + 1][j - 1]:
                dp[i][j] = True
                result = [i, j]

    i, j = result
    return phrase[i : j + 1]
