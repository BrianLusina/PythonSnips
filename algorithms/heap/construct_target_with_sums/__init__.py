from typing import List
import heapq


def is_possible(target: List[int]) -> bool:
    if not target:
        return False

    current_total_sum = sum(target)
    max_heap = []
    for x in target:
        heapq.heappush(max_heap, -x)

    # While the largest element is greater than 1
    while -max_heap[0] > 1:
        # Pop the maximum element from the heap
        current_max = -heapq.heappop(max_heap)
        # Compute the sum of the remaining elements
        remaining_sum = current_total_sum - current_max

        if remaining_sum == 1:
            return True

        if remaining_sum == 0:
            return False

        # Using modulo % to efficiently reverse multiple subtraction steps at once
        previous_max = current_max % remaining_sum

        # If the result is invalid (≤ 0 or unchanged), return False.
        if previous_max == 0 or previous_max >= current_max:
            return False

        heapq.heappush(max_heap, -previous_max)
        current_total_sum = remaining_sum + previous_max

    return True


def is_possible_2(target: List[int]) -> bool:
    # Calculate the total sum of the target array
    total_sum = sum(target)

    # Convert the target array into a max heap by negating the values
    # (Python's heapq is a min-heap, so we negate to simulate a max-heap)
    max_heap = [-num for num in target]
    heapq.heapify(max_heap)  # Turn the list into a heap

    while True:
        # Pop the largest element (the most negative value, so negate it back)
        current_max = -heapq.heappop(max_heap)

        # Calculate the sum of the remaining elements (total_sum - current_max)
        remaining_sum = total_sum - current_max

        # Base cases:
        # If the current max is 1 or the sum of the remaining elements is 1, we can return True
        if current_max == 1 or remaining_sum == 1:
            return True

        # Invalid cases:
        # If the sum of the remaining elements is 0, or the current max is smaller than
        # the remaining sum, or the current max divides evenly by the remaining sum, return False
        if (
            remaining_sum == 0
            or current_max < remaining_sum
            or current_max % remaining_sum == 0
        ):
            return False

        # Update the current_max with the modulo of remaining_sum to simulate the "reverse operation"
        updated_value = current_max % remaining_sum

        # Update the total sum for the next iteration
        total_sum = remaining_sum + updated_value

        # Push the updated value back into the heap (negate it to keep max-heap behavior)
        heapq.heappush(max_heap, -updated_value)
