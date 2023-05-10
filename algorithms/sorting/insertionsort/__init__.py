from typing import List, TypeVar

T = TypeVar("T", str, int, float)


def insertion_sort(collection: List[T]) -> List[T]:
    """
    Performs an insertion sort on a collection of comparable elements returning the collection sorted in place.

    Complexity Analysis:
        Time Complexity: O(N^2 + N), which is approximately O(N^2) as we take the more significant order of N which is
        N^2.
        Space Complexity: O(1), since no extra storage is used
    :param collection: Collection of elements
    :type list
    :return: sorted collection
    :rtype: list
    """
    for index in range(1, len(collection)):
        temp = collection[index]
        previous_position = index - 1

        while previous_position >= 0:
            if collection[previous_position] > temp:
                collection[previous_position + 1] = collection[previous_position]
                previous_position -= 1
            else:
                break

        collection[previous_position + 1] = temp

    return collection
