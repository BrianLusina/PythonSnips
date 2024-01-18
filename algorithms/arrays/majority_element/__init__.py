from typing import List
from collections import defaultdict


def majority_element(nums: List[int]) -> int:
    """
    Finds the element that occurs more than n/2 times, where n is the size of the input list.

    This first sorts the list in place and finds the element at index n/2, since the majority element will always occupy
     the middle position when the array is sorted.

    Complexity:
    - Time Complexity O(n log(n)) since sorting an array of size n takes O(n log(n)) time
    - Space Complexity O(1) since no extra space is required

    Args:
        nums (list): list of integers.
    Return:
        int: element that occurs the most in the list
    """
    nums.sort()
    n = len(nums)
    return nums[n // 2]


def majority_element_two(nums: List[int]) -> int:
    """
    Finds the element that occurs more than n/2 times, where n is the size of the input list.

    This uses a hash map to keep track of how frequent an element occurs in the list.
    The key value pairs will be the element itself, while the value will be the count/occurrences in the hash map.

    Complexity:
    - Time Complexity O(n):
        Since iteration is done through the array once to count the occurrences and then iterates through the hash map,
        which has a maximum size of the number of distinct elements in the array.
    - Space Complexity O(n) since a hashmap is used to keep track of frequencies of the elements in the list.

    Args:
        nums (list): list of integers.
    Return:
        int: element that occurs the most in the list
    """
    hash_map = defaultdict(int)
    n = len(nums)

    # Keep track of the count of each element from the list in the hash map
    for num in nums:
        hash_map[num] += 1

    # Update n to be n/2, where n is the size of the list.
    # This is done to check if an element occurs more than n/2 times
    n = n // 2

    for key, value in hash_map.items():
        if value > n:
            return key

    # If no majority element is found in the hash map, 0 is returned as the default value.
    # This will only occur if the input array is empty or does not have a majority element.
    return 0
