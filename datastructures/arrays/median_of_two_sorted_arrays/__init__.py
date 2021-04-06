def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
    """
    Finds the median of 2 sorted arrays

    First extends the nums1 array with nums2 array. This can be done with nums1 + nums2
    Sort the newly formed array & determine the mid points, mid1 & mid2

    If we have an even number of items, return the average of the 2 middle items

    Else we just return the middle value of the newly formed array
    """
    nums1.extend(nums2)
    nums1.sort()
    length = len(nums1)

    mid1 = (length - 1) // 2
    mid2 = length // 2

    # if we have an even number of items
    if length % 2 == 0:
        return (nums1[mid2] + nums1[mid2 - 1]) / 2

    return nums1[mid1]
