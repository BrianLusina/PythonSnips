def get_length_of_missing_array(array_of_arrays):
    """
    Sort the list in ascending order and extract the lengths of each list into another list
    Loop through the list of lengths searching to the greatest distance between 2 elements
    if the distance is greater than 1, add 1 to the previous element (or subtract 1 from next element)
    return the sum of this operation
    :param array_of_arrays:
    :return: The length of the missing array
    """
    indx, m = 0, 0

    if array_of_arrays is None or [] in array_of_arrays:
        return 0
    if None in array_of_arrays:
        return 0

    len_list = [len(lst) for lst in sorted(array_of_arrays, key=len)]

    while indx <= len(len_list):
        try:
            if (len_list[indx + 1] - len_list[indx]) > 1:
                m = len_list[indx + 1] - 1
            indx += 1
        except IndexError:
            break
    return m


def get_length_of_missing_array_2(a):
    lns = a and all(a) and list(map(len, a))
    return bool(lns) and sum(range(min(lns), max(lns) + 1)) - sum(lns)
