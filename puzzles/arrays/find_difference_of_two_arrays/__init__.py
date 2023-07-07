from typing import List


def find_difference(nums1: List[int], nums2: List[int]) -> List[List[int]]:
    s1 = set(nums1)
    s2 = set(nums2)

    return [list(s1 - s2), list(s2 - s1)]
