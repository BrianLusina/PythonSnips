from typing import List, TypeVar, Set

T = TypeVar("T")


def set_intersection(set1: Set[T], set2: Set[T]) -> List[T]:
    return [x for x in set1 if x in set2]


def intersection(list_one: List[T], list_two: List[T]) -> List[T]:
    """
    Returns the intersection of two arrays. Uses a set to solve the problem in linear time. A set provides in/contains
    operation in O(1) time in average case. This converts both arrays to sets and iterates over the smallest set
    checking the presence of each element in the other larger set. The time complexity is O(n+m) where n is the size of
    the first array and m is the size of the second array.
    Args:
        list_one list: 1st Array of items
        list_two list: 2nd Array of items
    Returns:
        list: the intersection of the two arrays
    """
    set1 = set(list_one)
    set2 = set(list_two)

    if len(set1) < len(set2):
        return set_intersection(set1, set2)
    else:
        return set_intersection(set2, set1)
