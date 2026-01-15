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


def climb(n: int) -> int:
    """
    Finds the number of possible ways to climb up n steps given the steps can be climbed wither 1 at a time or 2 at a
    time
    :param n: number of steps
    :return: number of possible ways to climb up the steps

    >>> climb(2)
    2

    >>> climb(1)
    1

    >>> climb(3)
    3
    """
    if n < 0:
        return 0
    if n == 1 or n == 0:
        return 1
    return climb(n - 1) + climb(n - 2)
