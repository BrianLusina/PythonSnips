def num_decodings(s: str) -> int:
    if not s or s[0] == "0":
        return 0

    n = len(s)
    # Initialize the dp array. dp[i] will store the number of ways to decode the string s[:i]
    dp = [0] * (n + 1)
    dp[0] = 1
    dp[1] = 1

    # Iterate through the string
    for i in range(2, n + 1):
        # Get the current character
        current_char = s[i - 1]
        # Get the previous character
        prev_char = s[i - 2]

        # If the current character is not a zero, then we can decode it as a single character
        if current_char != "0":
            dp[i] += dp[i - 1]

        # If the previous character is 1 or 2 and the current character is less than or equal to 6, then we can decode
        # it as a two character
        if prev_char == "1" or (prev_char == "2" and current_char <= "6"):
            dp[i] += dp[i - 2]

    # Return the number of ways to decode the string
    return dp[n]
