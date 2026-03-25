from typing import List, Tuple
import heapq


def kth_smallest_in_matrix_with_heap_1(matrix: List[List[int]], k: int) -> int:
    """
    Finds the kth smallest element in a matrix that has its rows and columns sorted in ascending order.
    Args:
        matrix (List[List[int]]): The matrix to find the kth smallest element in.
        k (int): The kth smallest element.
    Returns:
        int: The kth smallest element.
    """
    if not matrix:
        return -1

    min_heap: List[int] = []

    for lst in matrix:
        for element in lst:
            heapq.heappush(min_heap, element)

    counter = k - 1

    while counter > 0:
        heapq.heappop(min_heap)
        counter -= 1

    return min_heap[0]


def kth_smallest_in_matrix_with_heap_2(matrix: List[List[int]], k: int) -> int:
    """
    Finds the kth smallest element in a matrix that has its rows and columns sorted in ascending order.
    Args:
        matrix (List[List[int]]): The matrix to find the kth smallest element in.
        k (int): The kth smallest element.
    Returns:
        int: The kth smallest element.
    """
    # storing the number of rows in the matrix to use it in later
    row_count = len(matrix)
    # declaring a min-heap to keep track of smallest elements
    min_numbers: List[Tuple[int, int, int]] = []

    for index in range(min(row_count, k)):
        # pushing the first element of each row in the min-heap
        # The heappush() method pushes an element into an existing heap
        # in such a way that the heap property is maintained.
        first_element = matrix[index][0]
        element_index = 0
        heapq.heappush(min_numbers, (first_element, index, element_index))

    numbers_checked, smallest_element = 0, 0
    # iterating over the elements pushed in our min-heap
    while min_numbers:
        # get the smallest number from top of heap and its corresponding row and column
        smallest_element, row_index, col_index = heapq.heappop(min_numbers)
        numbers_checked += 1
        # when numbers_checked equals k, we'll return smallest_element
        if numbers_checked == k:
            break
        # if the current popped element has a next element in its row,
        # add the next element of that row to the min-heap
        if col_index + 1 < len(matrix[row_index]):
            heapq.heappush(
                min_numbers,
                (matrix[row_index][col_index + 1], row_index, col_index + 1),
            )

    # return the Kth smallest element found in the matrix
    return smallest_element
