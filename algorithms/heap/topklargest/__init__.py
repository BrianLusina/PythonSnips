from typing import List
import heapq


def k_largest(nums: List[int], k: int = 3) -> List[int]:
    """
    Finds the k largest elements in a given list. K is defaulted to three, but can be used to tweak the k largest
     elements in the array
    Args:
        nums(list): list of elements to check for
        k(int): number of elements to check, defaulted to 3
    Returns:
        list: top k largest elements
    """
    # input validation to ensure we don't get unexpected results
    if not nums or k <= 0:
        return []
    
    # Adjust k if it exceeds the length of nums
    k = min(k, len(nums))
    
    # create a minimum heap with the first k elements
    min_heap = nums[:k]
    heapq.heapify(min_heap)

    # iterate through the remaining elements
    for num in nums[k:]:
        # if the current number is greater than the element at the top of the heap
        if num > min_heap[0]:
            # Remove it and add this element
            heapq.heappushpop(min_heap, num)

    # return the top k elements
    return min_heap


def kth_largest(nums: List[int], k: int) -> int:
    """
    Finds the kth largest element in a given list
    Args:
        nums(list): list of elements to check for
        k(int): the kth largest element to return
    Returns:
        int: the kth largest element
    """
    # input validation to ensure we don't get unexpected results
    if not nums or k <= 0 or k > len(nums):
        return -1

    # create a minimum heap with the first k elements
    min_heap = []

    # iterate through the remaining elements
    for num in nums:
        if len(min_heap) < k:
            heapq.heappush(min_heap, num)
        # if the current number is greater than the element at the top of the heap
        elif num > min_heap[0]:
            # Remove it and add this element
            heapq.heappushpop(min_heap, num)

    # return the top kth element
    return min_heap[0]


def kth_largest_sorting(nums: List[int], k: int) -> int:
    """
    Finds the kth largest element in a given list using sorting
    Args:
        nums(list): list of elements to check for
        k(int): the kth largest element to return
    Returns:
        int: the kth largest element
    """
    # input validation to ensure we don't get unexpected results
    if not nums or k <= 0 or k > len(nums):
        return -1

    # Sort the list which incurs a time complexity cost of O(n log(n)). Space complexity is O(n) due to creating
    # a new sorted list
    sorted_nums = sorted(nums, reverse=True)
    # Return the kth largest element
    return sorted_nums[k - 1]
