def perm_missing_element(numbers: list) -> int:
    """
    Finds the missing element in a list of numbers
    :param list of numbers
    :return missing element 
    :rtype: int
    """

    missing_element = len(numbers) + 1

    for index, number in enumerate(numbers):
        missing_element = missing_element ^ number ^ (index + 1)

    return missing_element
