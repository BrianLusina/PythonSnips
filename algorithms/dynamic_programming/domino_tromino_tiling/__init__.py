MOD = 10 ** 9 + 7


def num_tilings(n: int) -> int:
    if n < 3:
        return n

    dp = [[0] * 3 for _ in range(n + 1)]

    dp[0][0] = dp[1][0] = 1
    dp[1][1] = dp[1][2] = 1

    for i in range(2, n + 1):
        dp[i][0] = (dp[i - 1][0] +
                    dp[i - 2][0] +
                    dp[i - 2][1] +
                    dp[i - 2][2]) % MOD

        dp[i][1] = (dp[i - 1][0] +
                    dp[i - 1][2]) % MOD

        dp[i][2] = (dp[i - 1][0] +
                    dp[i - 1][1]) % MOD

    return dp[n][0]
