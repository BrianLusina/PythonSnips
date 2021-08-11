from typing import List


def find_max_length(nums: List[int]) -> int:
    """
    Finds the maximum length of a contiguous sub array in a binary array. Makes use of a hashmap to store the entries in
    the form of (count, index). We make an entry for a count in the map whenever the count is encountered first and
    later on use the corresponding index to find the length of the largest sub array with equal number of zeros and ones
    when the same count is encountered again.

    Complexity Analysis:

    - Time complexity : O(n). The entire array is traversed only once.
    - Space complexity : O(n). Maximum size of the HashMap mapmap will be n, if all the elements are either 1 or 0.

    @param nums: Binary Array
    @return: Maximum length of contiguous sub array
    """
    # initializing map to (0, -1) is to avoid the edge cases like [0, 1] when you only have one zero and one.
    hashmap = {0: -1}
    max_len, count = 0, 0

    for x in range(0, len(nums)):
        count = count + (1 if nums[x] == 1 else -1)

        if count in hashmap:
            max_len = max(max_len, x - hashmap.get(count))
        else:
            hashmap[count] = x

    return max_len
