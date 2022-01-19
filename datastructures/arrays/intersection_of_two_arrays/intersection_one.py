from typing import List


def set_intersection(set1, set2):
    return [x for x in set1 if x in set2]


def intersection(nums1: List[int], nums2: List[int]) -> List[int]:
    """
    Returns the intersection of two arrays. Uses a set to solve the problem in linear time. A set provides in/contains
    operation in O(1) time in average case. This converts both arrays to sets and iterates over the smallest set
    checking the presence of each element in the other larger set. The time complexity is O(n+m) where n is the size of
    the first array and m is the size of the second array.
    @param nums1: 1st Array of numbers
    @param nums2: 2nd Array of numbers
    @return: Returns the intersection of the two arrays
    @rtype: List[int]
    """
    set1 = set(nums1)
    set2 = set(nums2)

    if len(set1) < len(set2):
        return set_intersection(set1, set2)
    else:
        return set_intersection(set2, set1)
