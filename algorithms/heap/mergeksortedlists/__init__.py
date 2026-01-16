from typing import List
import heapq


def merge_k_lists(lists: List[List[int]]) -> List[int]:
    """
    Merges k sorted lists into one list
    Args:
        lists(list): list of lists
    Returns:
        list: Combined list from the input list that is sorted
    """
    # Validate that the input provided is not empty. If it is empty, return an empty list. Nothing more to do here
    if not lists:
        return []

    # Check if any of the lists provided is empty. If we have an empty list, we return, as there is nothing more to do
    has_non_empty = any(lst for lst in lists)
    if not has_non_empty:
        return []

    # Initialize our heap. This will be used to keep the lowest value from each list at the root of the heap. Whenever
    # a value is popped from the root, the next value is added to the list and if it is the lowest value it will be
    # at the root of the heap
    min_heap = []

    # We will iterate through the list storing only the first values from each list, including the list index and the
    # element index which we will use to iterate through a given list. The list index will be used to iterate through
    # the provided lists
    for idx, lst in enumerate(lists):
        if lst:
            value, list_index, element_index = lst[0], idx, 0
            heapq.heappush(min_heap, (value, list_index, element_index))

    # Result will store the final output
    result: List[int] = []

    # While we still have elements in the heap
    while min_heap:
        # We get the top element from the heap
        value, list_index, element_index = heapq.heappop(min_heap)
        # Add the value to the result, at this point, we know this is the smallest value in the lists of lists
        result.append(value)

        # We check if the element index is less than the current list it can be found in. This means that there are
        # still other elements within this list
        if element_index + 1 < len(lists[list_index]):
            # We add the next value to the heap
            next_value = lists[list_index][element_index + 1]
            heapq.heappush(min_heap, (next_value, list_index, element_index + 1))

    # Return the result
    return result
