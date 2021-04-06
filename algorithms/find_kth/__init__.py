"""
Find the kth largest element in an unsorted array of elements
"""


def find_kth(arr, k):
    """
    Finds the kth largest element in the given array arr of integers,
    :param: arr unsorted array of integers
    :param: k, the order of value to return
    :return: kth largest element in array
    :rtype: int
    """

    # sanity checks
    # if this is not a valid integer or float, raise a ValueError
    if not isinstance(k, (int, float)) or k < 0:
        raise ValueError("Expected k to be a valid number")

    # if k is 1 or is equal to 0, return the maximum in the given array
    # if k is greater than the given length, it makes sense to return the maximum
    if (k == 1 or k == 0) or k > len(arr):
        return max(arr)

    # convert given number to integer
    kth = int(k)

    # find the current maximum
    current_max = max(arr)

    # filter out the numbers that are not equal to the current maximum
    new_array = list(filter(lambda x: x != current_max, arr))

    # recurse and return the kth largest number in the given array
    return find_kth(new_array, kth - 1)


if __name__ == "__main__":
    k = 2
    array = [10, 10, 20, 30, 40, 40]
    print(f"{k}th largest element in array {array} is {find_kth(array, k)}")
