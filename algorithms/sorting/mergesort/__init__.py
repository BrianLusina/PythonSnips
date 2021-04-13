from typing import List


def merge_sort_in_place(the_list: List[int]) -> List[int]:
    """
    Performs a merge sort on a list in-place
    :param the_list: list of integer values to sort
    :return: same list orded in ascending order
    Examples:
    >>> merge_sort_in_place([0, 5, 3, 2, 2])
    [0, 2, 2, 3, 5]
    >>> merge_sort_in_place([])
    []
    >>> merge_sort_in_place([-2, -5, -45])
    [-45, -5, -2]
    """
    mid = len(the_list) // 2
    left_half = the_list[:mid]
    right_half = the_list[mid:]

    merge_sort_in_place(left_half)
    merge_sort_in_place(right_half)

    i = 0
    j = 0
    k = 0

    while i < len(left_half) and j < len(right_half):
        if left_half[i] < right_half[j]:
            the_list[k] = left_half[i]
            i += 1
        else:
            the_list[k] = right_half[j]
            j += 1
        k += 1

    # check if any element was left in the left_half
    while i < len(left_half):
        the_list[k] = left_half[i]
        i += 1
        k += 1

    # check if any element was left in the right_half
    while i < len(right_half):
        the_list[k] = right_half[j]
        j += 1
        k += 1

    return the_list


def combine_lists(list_a: List[int], list_b: List[int]) -> List[int]:
    """
    Combines 2 integer lists
    :param list_a: List a
    :param list_b: List b
    :return merged list of a & b
    """
    list_a_index = 0
    list_b_index = 0
    merged_list = []

    # both lists have some items left in them
    while list_a_index < len(list_a) and list_b_index < len(list_b):
        # choose smaller of the 2 items and add it to the merged list
        if list_a[list_a_index] <= list_b[list_b_index]:
            merged_list.append(list_a[list_a_index])
            list_a_index += 1
        else:
            merged_list.append(list_b[list_b_index])
            list_b_index += 1

    # Grab any lingering items in the first list after we've exhaused the second list
    while list_a_index < len(list_a):
        merged_list.append(list_a[list_a_index])
        list_a_index += 1

    # Grab any lingering items in the second list after we've exhaused the first list
    while list_b_index < len(list_b):
        merged_list.append(list_b[list_b_index])
        list_b_index += 1

    return merged_list


def merge_sort_out_of_place(the_list: List[int]) -> List[int]:
    """
    Sorts a list of integer values out of place & returns a new list of integer
    :param the_list: List of integer values
    :return: a sorted integer list
    >>> merge_sort_out_of_place([0, 5, 3, 2, 2])
    [0, 2, 2, 3, 5]
    >>> merge_sort_out_of_place([])
    []
    >>> merge_sort_out_of_place([-2, -5, -45])
    [-45, -5, -2]
    """

    # base case
    if len(the_list) <= 1:
        return the_list

    middle_index = len(the_list) // 2
    left_half = the_list[:middle_index]
    right_half = the_list[middle_index:]

    # sort each half
    left_half_sorted = merge_sort_out_of_place(left_half)
    right_half_sorted = merge_sort_out_of_place(right_half)

    return combine_lists(left_half_sorted, right_half_sorted)
