def shortest_common_supersequence(str1: str, str2: str) -> str:
    str1_length = len(str1)
    str2_length = len(str2)

    # Create a 2D array dp of size (str1_length + 1) x (str2_length + 1), where dp[i][j] represents the length of the
    # shortest common supersequence (SCS) for the first i characters of str1 and the first j characters of str2.
    dp = [[0 for _ in range(str2_length + 1)] for _ in range(str1_length + 1)]

    # Initialize the base cases, the first row.
    # When str2 is empty, the supersequence is str1 itself (length = row index).
    # This is because if str2 is empty, the only option is to append all characters of str1.
    for row in range(str1_length + 1):
        dp[row][0] = row

    # When str1 is empty, the supersequence is str2 itself (length = col index)
    # because if str1 is empty, the only option is to append all characters of str2.
    for col in range(str2_length + 1):
        dp[0][col] = col

    # Fill the DP table using bottom-up DP programming
    # If characters at str1[row - 1] and str2[col - 1] match, inherit dp[row - 1][col - 1] and add 1 (since the common
    # character is counted once).
    # Otherwise, take the minimum of dp[row - 1][col] and dp[row][col - 1], then add 1 (since we need to include either
    # str1[row - 1] or str2[col - 1]).
    for row in range(1, str1_length + 1):
        for col in range(1, str2_length + 1):
            if str1[row - 1] == str2[col - 1]:
                # If characters match, inherit the length from the diagonal +1
                dp[row][col] = dp[row - 1][col - 1] + 1
            else:
                # If characters do not match, take the minimum length option +1
                dp[row][col] = min(dp[row - 1][col], dp[row][col - 1]) + 1

    # Reconstruct the supersequence
    super_sequence = []
    row, col = str1_length, str2_length

    while row > 0 and col > 0:
        if str1[row - 1] == str2[col - 1]:
            # If characters match, take it from diagonal
            super_sequence.append(str1[row - 1])
            row -= 1
            col -= 1
        elif dp[row - 1][col] < dp[row][col - 1]:
            # If str1’s character is part of the supersequence, move up
            super_sequence.append(str1[row - 1])
            row -= 1
        else:
            # If str2’s character is part of the supersequence, move left
            super_sequence.append(str2[col - 1])
            col -= 1

    # Append any remaining characters
    # If there are leftover characters in str1
    while row > 0:
        super_sequence.append(str1[row - 1])
        row -= 1
    # If there are leftover characters in str2
    while col > 0:
        super_sequence.append(str2[col - 1])
        col -= 1

    # Reverse the built sequence to get the correct order
    return "".join(super_sequence[::-1])
