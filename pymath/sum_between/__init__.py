from random import choice


def sum_between(array):
    """
    The function takes in a list of 2 numbers, Sums the numbers in between the list including the numbers and returns
    result. The numbers in the array may not be in the same order, so a check will be performed to test which number
    is lower and create a range to the greater number
    If the array input has 3 or more numbers an error will be raised and program will exit
    if the array has length or 0 or 1, raise an error
    :param array: Array to sum all numbers in between the 2 numbers in array
    :return: sum of all numbers from the array 'range'
    :rtype: int
    :raises: TypeError: if the array input is invalid
    """

    # test if the input is a list
    if array is None or not isinstance(array, list):
        raise TypeError("Expected input to be a list instead got {}".format(array))
    # test if the array is of a valid length
    elif len(array) < 2 or len(array) > 2:
        raise TypeError("Expect array to be of length 2 instead got array of length: {}".format(str(len(array))))

    # If the first number is less than second sum up to the 2nd
    if array[0] < array[1]:
        return sum(range(array[0], array[1] + 1))
    # if the second number is less than 1st
    elif array[1] < array[0]:
        return sum(range(array[1], array[0] + 1))
    # if both numbers are the same
    elif array[1] == array[0]:
        return choice(array)
