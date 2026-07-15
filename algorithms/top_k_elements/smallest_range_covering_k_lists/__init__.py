from collections import defaultdict
from typing import List, Tuple, DefaultDict
import heapq


def smallest_range(nums: List[List[int]]) -> List[int]:
    # min heap that will store (value, list index, element index) for the smallest elements
    min_heap: List[Tuple[int, int, int]] = []
    heapq.heapify(min_heap)
    # Initialize the maximum value among the current elements in the heap
    max_value = float("-inf")
    # Initialize range boundaries with placeholders
    range_start = 0
    range_end = float("inf")

    number_of_lists = len(nums)

    # insert the first elements from each list into the min-heap and update max_value to be the maximum value seen so far
    for list_idx in range(number_of_lists):
        # (value, list index, index within the list)
        value = nums[list_idx][0]
        heapq.heappush(min_heap, (value, list_idx, 0))
        # Track the max value among the current elements
        max_value = max(max_value, value)

    # Continue processing until we can't proceed further
    while len(min_heap) == number_of_lists:
        # Pop the smallest element from the heap (min_val from one of the lists)
        min_value, row, col = heapq.heappop(min_heap)

        # Update the smallest range if the current range is smaller
        if max_value - min_value < range_end - range_start:
            range_start = min_value
            range_end = max_value

        # If possible, add the next element from the same row to the heap
        if col + 1 < len(nums[row]):
            next_value = nums[row][col + 1]
            # Push the next element from the same list
            heapq.heappush(min_heap, (next_value, row, col + 1))
            # Update max_val if needed
            max_value = max(max_value, next_value)

        # If any list runs out of elements, we can't form a complete range anymore

    # Return the smallest range found
    return [range_start, range_end]


def smallest_range_two_pointer(nums: List[List[int]]) -> List[int]:
    merged: List[Tuple[int, int]] = []

    # merge all lists with their list index
    for list_idx, num_list in enumerate(nums):
        for num in num_list:
            merged.append((num, list_idx))

    # sort the merged list
    merged.sort()

    # Two pointers to track the smallest range
    freq: DefaultDict[int, int] = defaultdict(int)
    left, count = 0, 0
    range_start, range_end = 0, float("inf")

    for right in range(len(merged)):
        val = merged[right][1]
        freq[val] += 1
        if freq[val] == 1:
            count += 1

        # when all lists are represented, try to shrink the window
        while count == len(nums):
            current_range = merged[right][0] - merged[left][0]
            if current_range < range_end - range_start:
                range_start = merged[left][0]
                range_end = merged[right][0]

            freq[merged[left][1]] -= 1
            if freq[merged[left][1]] == 0:
                count -= 1

            left += 1

    return [range_start, range_end]


def smallest_range_brute_force(nums: List[List[int]]) -> List[int]:
    k = len(nums)
    # Stores the current index of each list
    indices = [0] * k
    # To track the smallest range
    range_list = [0, float("inf")]

    while True:
        cur_min, cur_max = float("inf"), float("-inf")
        min_list_index = 0

        # Find the current minimum and maximum values across the lists
        for i in range(k):
            current_element = nums[i][indices[i]]

            # Update the current minimum
            if current_element < cur_min:
                cur_min = current_element
                min_list_index = i

            # Update the current maximum
            if current_element > cur_max:
                cur_max = current_element

        # Update the range if a smaller one is found
        if cur_max - cur_min < range_list[1] - range_list[0]:
            range_list[0] = cur_min
            range_list[1] = cur_max

        # Move to the next element in the list that had the minimum value
        indices[min_list_index] += 1
        if indices[min_list_index] == len(nums[min_list_index]):
            break

    return range_list
