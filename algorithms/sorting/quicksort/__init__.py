def partition(thelist: list, start_index: int, end_index: int) -> int:
    """
    Partitions a list into 2 and returns the pivot index
    :param thelist The list to divide into 2 partitions to get the pivot index.
    This uses the last element as the pivot of the list
    :type thelist list
    :param start_index
    :type start_index int
    :param end_index
    :type end_index int
    :returns pivot index
    :rtype int
    """

    pivot = thelist[end_index]

    left_index = start_index
    right_index = end_index - 1

    while left_index <= right_index:

        # walk until we find something on the left side that belongs on the right (less than the pivot)
        while left_index <= end_index and thelist[left_index] < pivot:
            left_index += 1

        # walk until we find something on the right side that belongs on the left(greater than or equal to the pivot)
        while right_index >= start_index and thelist[right_index] >= pivot:
            right_index -= 1

        # swap the items at the left_index and right_index, moving the element that's smaller than the pivot to the left
        # half and the element that's larger than the pivot to the right half

        if left_index < right_index:
            thelist[right_index], thelist[left_index] = thelist[left_index], thelist[right_index]

        # unless we have looked at all the elements in the list and are done partitioning. In that case, move the pivot element
        # into it's final position
        else:
            thelist[end_index], thelist[left_index] = thelist[left_index], thelist[end_index]

    return left_index


def quicksort_sublist(thelist: list, start_index: int, end_index: int):
    """
    Recursively sorts the sublists
    :param thelist The list to sort
    :type thelist list
    :param start_index Start index of list
    :type start_index int
    :param end_index End index of list
    :type end_index int
    """

    # base case: list with 0 or 1 element(s)
    if start_index >= end_index:
        return

    # divide the list into 2 smaller sublists
    pivot_index = partition(thelist, start_index, end_index)

    # Recursively sort each sublist
    quicksort_sublist(thelist, start_index, pivot_index - 1)
    quicksort_sublist(thelist, pivot_index + 1, end_index)


def quicksort(thelist: list) -> list:
    """
    Quicksort algorithm picking the last element in the list as a pivot.
    This assumes that the list of elements to be sorted are all uniform in type. i.e. Are all integers in this cases
    :param thelist
    :returns list
    :rtype list
    """
    length = len(thelist)

    # nothing to sort here
    if length <= 0:
        return thelist

    quicksort_sublist(thelist, 0, length - 1)
    return thelist
