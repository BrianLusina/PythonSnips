def climb_stairs(n: int) -> int:
    if n == 1:
        return 1

    first = 1
    second = 2

    for _ in range(3, n + 1):
        third = first + second
        first = second
        second = third

    return second


def climb_stairs_dp_bottom_up(n: int) -> int:
    if n < 0:
        return 0
    if n <= 1:
        return 1

    dp = [0] * (n + 1)
    dp[1] = 1
    dp[2] = 2

    for idx in range(3, n + 1):
        dp[idx] = dp[idx - 1] + dp[idx - 2]

    return dp[n]


def climb_stairs_dp_top_down(n: int) -> int:
    """
    Finds the number of possible ways to climb up n steps given the steps can be climbed wither 1 at a time or 2 at a
    time
    :param n: number of steps
    :return: number of possible ways to climb up the steps

    >>> climb_stairs_dp_top_down(2)
    2

    >>> climb_stairs_dp_top_down(1)
    1

    >>> climb_stairs_dp_top_down(3)
    3
    """
    if n < 0:
        return 0
    if n == 1 or n == 0:
        return 1
    return climb_stairs_dp_top_down(n - 1) + climb_stairs_dp_top_down(n - 2)
