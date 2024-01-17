from typing import List


def remove_duplicates(nums: List[int]) -> int:
    nums[:] = list(set(nums))
    nums.sort()
    return len(nums)


def remove_duplicates_from_sorted_list(nums: List[int]) -> int:
    """
    Removes duplicates from a sorted list of integers and returns the number of the unique elements in the list. This
    modifies the list in place so no extra space is used, effectively the Space complexity is O(1). However, the time
    complexity is O(n) where n is the length of the list.

    This uses 2 pointers to keep track of the unique and non-unique elements in the list of integers. 'i' pointer is at
    the element before, and j pointer is at the next element. These are moved along the elements in the list as below:
    1. As long as j is less than the length of the list, we shall iterate until j reaches the end of the list, i.e. the
     last element in the list
    2. if the element at position i is not equal to the element at position j(at this point j is ahead of i), we
     increase the i index by 1 and assign the index at 'i' the value of the index at j and increment the index at j,
     i.e. moving the pointer j and i forward by 1
    3. If the elements are equal, then that means we have encountered a duplicate & therefore we move the pointer j
     forward by 1 until we encounter a unique element.
    4. When the loop is complete, we return i +1. This is because the pointer 'i' is now pointing to the last unique
     element in the list.

    The other elements after the pointer 'i' are the duplicate elements. This modifies the sorted list in place
    retaining "some" of the duplicated elements to the right of i. Note that this means we will not know how many times
    an element occurred in the original sorted list of elements.

    Args:
        nums (list): list of integers.
    Returns:
        int: integer denoting the number of unique elements in the list
    """

    if not nums:
        return 0

    i, j = 0, 1

    while j < len(nums):
        if nums[i] != nums[j]:
            i += 1
            nums[i] = nums[j]
        j += 1
    return i + 1


def remove_duplicates_two(nums: List[int]) -> int:
    # Initialize an integer k that updates the kth index of the array...
    # only when the current element does not match either of the two previous indexes. ...
    k = 0
    # Traverse all elements through loop...
    for num in nums:
        # If the index does not match elements, count that element and update it...
        if k < 2 or num != nums[k - 2]:
            nums[k] = num
            k += 1
    # Return k after placing the final result in the first k slots of nums...
    return k
