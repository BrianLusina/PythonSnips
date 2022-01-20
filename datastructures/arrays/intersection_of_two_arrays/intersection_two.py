from typing import List


def intersect(nums1: List[int], nums2: List[int]) -> List[int]:
    """
    Given two arrays, find their intersection.
    """
    n1, n2, result = sorted(nums1), sorted(nums2), []
    pt1, pt2 = 0, 0

    while pt1 < len(n1) and pt2 < len(n2):
        if n1[pt1] < n2[pt2]:
            pt1 += 1
        elif n2[pt2] < n1[pt1]:
            pt2 += 1
        else:
            result.append(n1[pt1])
            pt1 += 1
            pt2 += 1
    return result
