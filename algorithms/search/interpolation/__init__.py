from typing import List, TypeVar

T = TypeVar("T")


def interpolation_search(collection: List[T], target: T) -> int:
    """Performs an interpolation search on a collection of items for a given target. The assumption made is that the
    collection is uniformly distributed and sorted. Otherwise, this will have a worst case Time Complexity of O(n) where
    n is the number of items in the collection. If the collection is uniformly distributed and sorted, the time complexity
    becomes O(log(log(n))

    Args:
        collection (list): Collection of items to search through
        target (TypeVar): Target to search for
    Raises:
        Exception: if the collection is empty. Search can not be performed on an empty collection
    Returns:
        int: The index of the target in the given collection.
    """
    if len(collection) == 0:
        raise Exception(f"Target {target} can not be found in an empty collection")

    left = 0
    right = len(collection) - 1

    while left <= right and collection[left] <= target <= collection[right]:
        # find the midpoint
        mid_point = left + int(
            ((float(right - left) / (collection[right] - collection[left])) * (target - collection[left])))

        # compare value at midpoint with target
        if collection[mid_point] == target:
            return mid_point
        elif collection[mid_point] < target:
            left = mid_point + 1
        else:
            right = mid_point - 1

    if target == collection[left]:
        return left

    raise Exception(f"Target {target} can not be found in collection")
