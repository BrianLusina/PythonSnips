from typing import List, Tuple
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
