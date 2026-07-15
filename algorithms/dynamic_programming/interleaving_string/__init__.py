from functools import cache


def is_interleave_dp_top_down(s1: str, s2: str, s3: str) -> bool:
    """
    Checks if it is possible to form string 3 from s1 and s2 by interleaving them such that either characters from s1
    start or characters from s2 start.
    Args:
        s1(str): first string
        s2(str): second string
        s3(string): potentially interleaved string
    Returns:
        bool: True if it is possible to interleave s1 and s2 to form s3, False otherwise
    """
    len_s1, len_s2, len_s3 = len(s1), len(s2), len(s3)

    # If the length of s1 and s2 sum up to a value less than s3, we cannot interleave them to form s3
    if (len_s1 + len_s2) != len_s3:
        return False

    @cache
    def dfs(p1: int, p2: int) -> bool:
        """
        Recursively check if can form the remaining part of s3 from s1 and s2
        Args:
            p1(int): current index at s1
            p2(int): current index at s2
        Returns:
            bool: True if characters at (p1 + p2) can form the remaining part of s3
        """
        # base case, if we have used all the characters from both strings, we return True
        if p1 >= len_s1 and p2 >= len_s2:
            return True

        # Get the current position in s3
        p3 = p1 + p2

        # If we can still iterate through s1 and the character at the current position at s3 equals s1, we can take the
        # character from s1
        if p1 < len_s1 and s1[p1] == s3[p3]:
            # Recursively call dfs to check if the rest can form a valid interleaving string
            if dfs(p1 + 1, p2):
                return True
        if p2 < len_s2 and s2[p2] == s3[p3]:
            # Recursively call dfs to check if the rest can form a valid interleaving string
            if dfs(p1, p2 + 1):
                return True
        return False

    return dfs(0, 0)


def is_interleave_dp_bottom_up(s1, s2, s3):
    len_s1, len_s2, len_s3 = len(s1), len(s2), len(s3)
    # If lengths don't add up, interleaving is impossible
    if len_s3 != len_s1 + len_s2:
        return False

    # 1D DP array; dp[j] represents using s1[:i] and s2[:j]
    dp = [False] * (len_s2 + 1)

    # Iterate over prefixes of s1 (i) and s2 (j)
    for i in range(len_s1 + 1):
        for j in range(len_s2 + 1):
            if i == 0 and j == 0:
                # Empty + empty = empty → valid
                dp[j] = True

            elif i == 0:
                # First row: can only use s2's characters
                dp[j] = dp[j - 1] and s2[j - 1] == s3[j - 1]

            elif j == 0:
                # First column: can only use s1's characters
                dp[j] = dp[j] and s1[i - 1] == s3[i - 1]

            else:
                # General case: take from s1 or s2 if they match s3
                take_from_s1 = dp[j] and s1[i - 1] == s3[i + j - 1]
                take_from_s2 = dp[j - 1] and s2[j - 1] == s3[i + j - 1]
                dp[j] = take_from_s1 or take_from_s2

    return dp[len(s2)]
