def longest_common_subsequence(text1: str, text2: str) -> int:
    """LCS is a classic problem. Let dp[i][j] be the LCS for string text1 ends at index i and string text2 ends at index
    j. If text1[i]==text2[j], then dp[i][j] would be 1+dp[i−1][j−1]. Otherwise, we target the largest LCS if we skip one
    character from either text1 or text2, i.e. dp[i][j]=max(dp[i−1][j],dp[i][j−1]).

    Complexity:
    Where m is the length of text1 and n is the length of text2
    - Time complexity: O(m*n)
    - Space complexity: O(m*n)
    """
    dp = [[0 for _ in range(len(text2) + 1)] for _ in range(len(text1) + 1)]

    for i in range(len(text1) - 1, -1, -1):
        for j in range(len(text2) - 1, -1, -1):
            if text1[i] == text2[j]:
                dp[i][j] = 1 + dp[i + 1][j + 1]
            else:
                dp[i][j] = max(dp[i + 1][j], dp[i][j + 1])

    return dp[0][0]
