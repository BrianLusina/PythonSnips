from algorithms.two_pointers.palindrome import is_palindrome


def longest_palindromic_substring(phrase: str) -> str:
    """
    Finds the longest palindromic substring from a given string and returns it. If the string has
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

    # Substrings of length greater than 2
    for length in range(2, n):
        for i in range(n - length):
            j = i + length
            if phrase[i] == phrase[j] and dp[i + 1][j - 1]:
                dp[i][j] = True
                result = [i, j]

    i, j = result
    return phrase[i : j + 1]


def longest_palindromic_substring_2(s):
    # To store the starting and ending indexes of LPS
    res = [0, 0]

    n = len(s)

    # Initialize a lookup table of dimensions len(s) * len(s)
    dp = [[False for _ in range(n)] for _ in range(n)]

    # Base case: A string with one letter is always a palindrome
    for i in range(n):
        dp[i][i] = True

    # Base case: Substrings of length 2
    for i in range(n - 1):
        dp[i][i + 1] = s[i] == s[i + 1]  # Check if two characters are equal
        if dp[i][i + 1]:
            res = [i, i + 1]  # Update the resultant array

    # Substrings of lengths greater than 2
    for length in range(3, n + 1):
        i = 0
        # Checking every possible substring of any specific length
        for j in range(length - 1, len(s)):  # Iterate over possible ending indexes
            dp[i][j] = dp[i + 1][j - 1] and (s[i] == s[j])
            if dp[i][j]:
                res = [i, j]
            i += 1

    i, j = res
    # Return the longest palindromic substring
    return s[i : j + 1]
