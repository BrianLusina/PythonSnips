from typing import List


def count_bits(n: int) -> List[int]:
    """
    Counts the number of 1 bits in the given integer provided returning a list where count[i] stores the count of '1'
    bits in the binary form of i.
    Args:
        n(int): integer
    Returns:
        list: count of 1 bits where each index contains the count of 1 bits
    """
    dp = [0] * (n + 1)

    for i in range(1, n + 1):
        # this can also be solved as which is faster in Python
        # dp[i] = dp[i >> 1] + (i & 1)
        dp[i] = dp[i // 2] + (i % 2)

    return dp
