import re


def sort_twisted37(arr):
    """
    Sorts the array in ascending order, but where there is a 3 a 7 is placed and vice versa
    Will first sort the array the usual way, creating a sorted copy of the input array
    Loops through each number in the sorted array, checking the number is 3 or contains a 3
    :param arr: The array of numbers to sort
    :return: The sorted array
    :rtype: list
    """
    # first sort the array the normal way
    sorted_arr = sorted(arr)
    three, seven = 0, 0

    for num in sorted_arr:
        if re.match(r'^3$|^[1-9]+3$', str(num)):
            three = num
            # find its index
            sorted_arr.index(num)
        elif num == 7 or str(num).__contains__(str(7)):
            seven = num

    return []
