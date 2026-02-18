from typing import List


def find_missing_element(numbers: List[int]) -> int:
    """
    Finds the missing element in a list of numbers
    Args:
        numbers (List[int]): list of numbers
    Returns:
        int: missing element
    """
    missing_element = len(numbers)

    for index, number in enumerate(numbers):
        missing_element = missing_element ^ number ^ index

    return missing_element


def find_missing_number(nums):
    len_nums = len(nums)
    index = 0

    while index < len_nums:
        value = nums[index]

        if value < len_nums and value != nums[value]:
            nums[index], nums[value] = nums[value], nums[index]

        else:
            index += 1

    for x in range(len_nums):
        if x != nums[x]:
            return x
    return len_nums


def find_missing_number_sum_of_n_terms(nums):
    """
    Finds the missing element in a list of numbers

    The sum of the first n natural numbers is given by the formula (n * (n + 1)) / 2. The idea is to compute this sum
    and subtract the sum of all elements in the array from it to get the missing number.

    Args:
        nums (List[int]): list of numbers
    Returns:
        int: missing element
    """
    len_nums = len(nums)

    total_sum = sum(nums)

    expected_sum = len_nums * (len_nums + 1) // 2

    return expected_sum - total_sum
