from typing import List


def max_runtime(batteries: List[int], n: int) -> int:
    """
    Determines the maximum runtime of n computers given the power available from each battery.

    The function uses binary search to find the maximum runtime that can power n computers for the given amount of time.

    The function takes a list of integers representing the power available from each battery and an integer representing
    the number of computers to power.

    The function returns an integer representing the maximum runtime that can power the computers for the given amount of time.

    :param batteries: A list of integers representing the power available from each battery.
    :param n: An integer representing the number of computers to power.

    :return: An integer representing the maximum runtime that can power the computers for the given amount of time.
    """
    left = 0
    right = sum(batteries) // n
    result = 0

    while left <= right:
        mid = (left + right) // 2

        if can_run_for(batteries, n, mid):
            left = mid + 1
            result = mid
        else:
            right = mid - 1

    return result


def can_run_for(batteries: List[int], n: int, target_time: int) -> bool:
    """
    Determines whether the given list of batteries can power n computers for the given amount of time.

    :param batteries: A list of integers representing the power available from each battery.
    :param n: An integer representing the number of computers to power.
    :param target_time: An integer representing the amount of time to power the computers for.

    :return: A boolean indicating whether the batteries can power the computers for the given amount of time.
    """
    power_needed = n * target_time
    power_available = sum(min(battery, target_time) for battery in batteries)
    return power_available >= power_needed


def max_run_time_2(batteries: List[int], n: int) -> int:
    """
    Finds the maximum runtime that can power the computers for the given amount of time.

    :param batteries: A list of integers representing the power available from each battery.
    :param n: An integer representing the number of computers to power.

    :return: An integer representing the maximum runtime that can power the computers for the given amount of time.
    """

    total_power = sum(batteries)
    left, right = 0, total_power // n

    while left < right:
        mid = right - (right - left) // 2
        usable = sum(min(b, mid) for b in batteries)

        if usable >= mid * n:
            left = mid
        else:
            right = mid - 1
    return left
