from typing import List, TypeVar

T = TypeVar("T", str, int, float)


def partition(collection: List[T], start_index: int, end_index: int) -> int:
    """
    Partitions a list into 2 and returns the pivot index. This uses 2 pointers to partition a list around a pivot.
    The left and right pointers move to the right and left of the collection respectively as they check the values they
    are pointing to whether they are greater or less than the pivot value.

    The left pointer checks if the value it is pointing to is less than the chosen pivot value and is less than the end
    index. If it is, then it continues moving to the right. If this condition does not hold, we stop moving the pointer

    The right pointer checks if the value it is pointing to is greater than the chosen pivot value and the start index.
    if it is, then it moves on to the left. If these conditions are not met, then the right pointer stops moving.

    If the left pointer is still less than the right pointer, that is, it has not yet passed or is at the same position
    as the right pointer, then we swap the values at the left and right pointers.

    If the left pointer is either greater than the right pointer or is at the same position as the left pointer. We swap
    the value at the left pointer with the pivot value. At this point, the collection(read list) is properly partitioned.

    We return the left pointer as this will be the new pivot index.

    @param collection. The list to divide into 2 partitions to get the pivot index.
    @param start_index The start index to begin partitioning
    @param end_index The end index that will be used to get the pivot value
    @return pivot index
    """

    pivot = collection[end_index]

    left_pointer = start_index
    right_pointer = end_index - 1

    while left_pointer <= right_pointer:

        # We move the left pointer to the right as long as the value it is pointing to is less than the pivot and is
        # less than the end index
        while left_pointer <= end_index and collection[left_pointer] < pivot:
            left_pointer += 1

        # Move the right pointer to the left as long as the value it is pointing to is greater than the pivot and is
        # greater thant the start index
        while right_pointer >= start_index and collection[right_pointer] >= pivot:
            right_pointer -= 1

        # we have now reached the point where we have stopped moving both the left & right pointers. We check whether
        # the left pointer has gone beyond the right pointer or not.
        # if the left pointer is less than the right pointer, we swap the items at the left_pointer and right_pointer,
        # moving the element that's smaller than the pivot to the left
        # half and the element that's larger than the pivot to the right half

        if left_pointer < right_pointer:
            collection[right_pointer], collection[left_pointer] = (
                collection[left_pointer],
                collection[right_pointer],
            )

        # At this point, it means that the left pointer is either greater than or equal to the right pointer. In that
        # case, move the pivot element into it's final position
        else:
            collection[end_index], collection[left_pointer] = (
                collection[left_pointer],
                collection[end_index],
            )

    return left_pointer


def quicksort(collection: List[T]) -> List[T]:
    """
    Quicksort algorithm picking the last element in the list as a pivot.
    This assumes that the list of elements to be sorted are all uniform in type. i.e. Are all integers in this cases
    :param collection
    :returns list
    :rtype list
    """
    length = len(collection)

    # nothing to sort here
    if length <= 0:
        return collection

    def quicksort_sublist(items: List[T], start_index: int, end_index: int):
        """
        Recursively sorts the sublists
        :param items The list to sort
        :param start_index Start index of list
        :param end_index End index of list
        """

        # base case: list with 0 or 1 element(s)
        if start_index >= end_index:
            return

        # divide the list into 2 smaller sublists
        pivot_index = partition(items, start_index, end_index)

        # Recursively sort each sublist

        # sort the left half
        quicksort_sublist(items, start_index, pivot_index - 1)

        # sort the right half
        quicksort_sublist(items, pivot_index + 1, end_index)

    quicksort_sublist(collection, 0, length - 1)
    return collection
