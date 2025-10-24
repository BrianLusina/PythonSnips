from typing import List, TypeVar

T = TypeVar("T")


def intersection(a: List[T], b: List[T]) -> List[T]:
    """
    Finds the intersection between 2 lists and returns a list with the values that occur in both

    Complexity Analysis:
        Time Complexity:
            This will depend on the sizes of each list. If both lists are identical in size, the Worst case scenario is
            O(N^2) where N is the size of each list, this is because we are comparing each value in the first list to
            each value in the second list. If they are not identical in size, then the complexity becomes O(N * M) where
            N is the size of the first list and M the size of the second list.
        Space Complexity:
            Again, this will depend on the sizes of each list, but it averages to O(N+M) where N is the size of the first
            list and M is the size of the second list
    Args:
        a list: first collection
        b list: second collectoin
    Returns:
        list: all values that intersect between the 2 collections

    >>> a1 = [3,1,4,2]
    >>> b1 = [4,5,3,6]
    >>> intersection(a1, b1)
    [3, 4]
    """

    result = []

    for x in range(len(a)):
        for y in range(len(b)):
            if a[x] == b[y]:
                result.append(a[x])
                # adding break here ensures that we save on time and steps. if we have found a value that is identical
                # then there is no need to perform another iteration to check another value, We should proceed to the
                # next value
                break

    return result
