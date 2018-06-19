try:
    from collections import Iterable
except ImportError:
    from collections.abc import Iterable
from collections import defaultdict


# TODO
def find_sub_arr_maxsum(array):
    """
    Finds the sub array with the maximum value
    An example:
    >>> find_sub_arr_maxsum([-2, 1, -3, 4, -1, 2, 1, -5, 4])
    [[4, -1, 2, 1], 6]

    >>> find_sub_arr_maxsum([4, -1, 2, 1, -40, 1, 2, -1, 4])
    [[[4, -1, 2, 1], [1, 2, -1, 4]], 6]

    >>> find_sub_arr_maxsum([])
    [[], 0]

    :param array:
    :type array list
    :return: List or list of lists
    :rtype: list
    """
    if array is None or not isinstance(array, Iterable):
        raise ValueError(f"Expected array to be iterable, instead got {array}")

    if len(array) == 0:
        return [[], 0]

    current_max = 0
    maximum = 0

    sub_array_dict = defaultdict(lambda: [])

    for x in range(len(array)):
        maximum = maximum + array[x]

        if current_max < maximum:
            current_max = maximum

            if current_max in sub_array_dict:
                sub_array_dict[current_max].append([array[:x]])
            sub_array_dict[current_max] = [array[:x]]

        if maximum < 0:
            maximum = 0

    return sub_array_dict


if __name__ == "__main__":
    arr = [4, -1, 2, 1, -40, 1, 2, -1, 4]
    print(f"Sub arrays for {arr} are {find_sub_arr_maxsum(arr)}")
