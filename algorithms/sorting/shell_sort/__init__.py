from typing import List, TypeVar

T = TypeVar("T")


def shell_sort(collection: List[T]) -> List[T]:
    """Performs a shell sort on a collection of items provided the items are comparable. This
    sorts the list in place.

    Args:
        collection (List[T]): collection of items

    Returns:
        List[T]: sorted collection of items
    """
    if len(collection) <= 1:
        return collection

    distance = len(collection) // 2

    while distance > 0:
        for i in range(distance, len(collection)):
            temp = collection[i]
            j = i

            # sort the sub list for this distance
            while j >= distance and collection[j - distance] > temp:
                collection[j] = collection[j - distance]
                j = j - distance

            collection[j] = temp
        # reduce the distance for the next element
        distance = distance // 2

    return collection
