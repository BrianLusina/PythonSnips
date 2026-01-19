from typing import List


def split_array(nums: List[int], k: int) -> int:
    if not nums:
        return -1

    left = max(nums)
    right = sum(nums)
    first_true_index = -1

    def feasible(max_sum: int) -> bool:
        """
        Check if we can split the array into at most k sub arrays with each sub array sum less than or equal to max_sum
        """
        current_sum = 0
        # Start with one
        sub_array_count = 1

        for num in nums:
            if current_sum + num > max_sum:
                current_sum = num
                sub_array_count += 1
            else:
                current_sum += num

        return sub_array_count <= k

    while left <= right:
        mid = (right + left) // 2
        if feasible(mid):
            first_true_index = mid
            # Find a smaller valid value
            right = mid - 1
        else:
            # Find a larger valid value
            left = mid + 1

    return first_true_index


def split_array_2(nums, k):
    if not nums:
        return -1

    # Set the initial search range for the largest sum:
    # Minimum is the largest number in the array, and maximum is the sum of all numbers
    left, right = max(nums), sum(nums)

    def can_split(middle: int):
        # Initialize the count of subarrays and the current sum of the current subarray
        subarrays = 1
        current_sum = 0

        for num in nums:
            # Check if adding the current number exceeds the allowed sum (mid)
            if current_sum + num > middle:
                # Increment the count of subarrays
                subarrays += 1
                # Start a new subarray with the current number
                current_sum = num

                # If the number of subarrays exceeds the allowed k, return False
                if subarrays > k:
                    return False
            else:
                # Otherwise, add the number to the current subarray
                current_sum += num

        # Return True if the array can be split within the allowed subarray count
        return True

    # Perform binary search to find the minimum largest sum
    while left < right:
        # Find the middle value of the current range
        mid = (left + right) // 2

        # Check if the array can be split into k or fewer subarrays with this maximum sum
        if can_split(mid):
            # If possible, try a smaller maximum sum
            right = mid
        else:
            # Otherwise, increase the range to allow larger sums
            left = mid + 1

    # Return the smallest maximum sum that satisfies the condition
    return left
