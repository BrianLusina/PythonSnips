from typing import List


def max_number(nums1: List[int], nums2: List[int], k: int) -> List[int]:
    """
    Creates Maximum number from two arrays nums1 and nums2 where the number has to be of length k using digits from both
    integer arrays
    Args:
        nums1(int): first integer array
        nums2(int): second integer array
        k(int): number of digits of final array
    Returns:
        list: list of integers formed from integer array
    """

    def extract_maximum_subsequence(nums: List[int], l: int):
        """
        Extracts maximum subsequence from nums of length l using a monotonic stack approach
        Args:
            nums(list): list of integers
            l(int): length of extracted maximum subsequence
        Returns:

        """
        n = len(nums)
        stack = [0] * l  # Pre-allocate stack of size k
        top = -1  # Stack pointer (top index)
        elements_to_drop = n - l  # Number of elements we can skip

        for num in nums:
            # Pop smaller elements from stack if we can still drop elements
            while top >= 0 and stack[top] < num and elements_to_drop > 0:
                top -= 1
                elements_to_drop -= 1

            # Add current element if stack not full
            if top + 1 < l:
                top += 1
                stack[top] = num
            else:
                # Stack is full, just decrement elements_to_drop
                elements_to_drop -= 1

        return stack

    def is_greater(nums_one, nums_two, idx1: int, idx2: int) -> bool:
        """
        Compare two arrays starting from given indices.
        Returns True if nums1[idx1:] is lexicographically greater than nums2[idx2:].
        """
        # If nums1 exhausted, it's not greater
        if idx1 >= len(nums_one):
            return False
        # If nums2 exhausted but nums1 has elements, nums1 is greater
        if idx2 >= len(nums_two):
            return True
        # Compare current elements
        if nums_one[idx1] > nums_two[idx2]:
            return True
        if nums_one[idx1] < nums_two[idx2]:
            return False
        # If equal, recursively compare next elements
        return is_greater(nums_one, nums_two, idx1 + 1, idx2 + 1)

    def merge_arrays(
        nums_1_subsequence: List[int], nums_2_subsequence: List[int]
    ) -> List[int]:
        """
        Merge two arrays to create the maximum possible array.
        Always picks the lexicographically larger remaining portion.
        """
        nums_1_len, nums_2_len = len(nums_1_subsequence), len(nums_2_subsequence)
        idx1 = idx2 = 0
        result = [0] * (nums_1_len + nums_2_len)

        for pos in range(nums_1_len + nums_2_len):
            # Choose from nums1 if it has greater or equal remaining portion
            if is_greater(nums_1_subsequence, nums_2_subsequence, idx1, idx2):
                result[pos] = nums_1_subsequence[idx1]
                idx1 += 1
            else:
                result[pos] = nums_2_subsequence[idx2]
                idx2 += 1

        return result

    # Main logic
    m, n = len(nums1), len(nums2)
    # Determine valid range for elements to take from nums1
    min_from_nums1 = max(0, k - n)  # Must take at least k-n from nums1
    max_from_nums1 = min(k, m)  # Can take at most min(k, m) from nums1

    max_result = [0] * k

    # Try all valid splits between nums1 and nums2
    for take_from_nums1 in range(min_from_nums1, max_from_nums1 + 1):
        take_from_nums2 = k - take_from_nums1

        # Get maximum subsequences from each array
        subsequence1 = extract_maximum_subsequence(nums1, take_from_nums1)
        subsequence2 = extract_maximum_subsequence(nums2, take_from_nums2)

        # Merge the subsequences to get candidate result
        candidate = merge_arrays(subsequence1, subsequence2)

        # Update max_result if candidate is lexicographically larger
        if max_result < candidate:
            max_result = candidate

    return max_result
