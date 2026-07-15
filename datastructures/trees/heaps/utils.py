from typing import List, Any
from datastructures.trees.heaps import Heap
from datastructures.trees.heaps.binary.max_heap import MaxHeap
from algorithms.sorting.heapsort import left_child_index, right_child_index


def min_heapify(heap: MaxHeap, idx: int) -> Heap:
    left = heap.get_left_child_index(idx)
    right = heap.get_right_child_index(idx)
    smallest = idx

    # check if left child exists and is less than smallest
    if len(heap) > left and heap[smallest] > heap[left]:
        smallest = left
    # check if right child exists and is less than smallest
    if len(heap) > right and heap[smallest] > heap[right]:
        smallest = right
    # check if current index is not the smallest
    if smallest != idx:
        # swap current index value with smallest
        tmp = heap[smallest]
        heap[smallest] = heap[idx]
        heap[idx] = tmp
        # minHeapify the new node
        min_heapify(heap, smallest)
    return heap


def convert_max_to_min(max_heap: MaxHeap) -> MaxHeap:
    """
    Converts a max heap into a min heap
    @param max_heap:
    @type max_heap MaxHeap
    @return: Min Heap
    @rtype: MinHeap
    """

    # iterate from middle to first element
    # middle to first indices contain all parent nodes
    for i in range(len(max_heap) // 2, -1, -1):
        # call minHeapify on all parent nodes
        max_heap = min_heapify(max_heap, i)
    return max_heap


def has_smaller_child(data: List[Any], index: int) -> bool:
    """
    Checks whether a node at the given index has left and right children and if either of those children are less
    than the node at the given index.
    Args
        data(list): Node data
        index(int): Node index
    Returns:
        bool: True if the condition is met, false otherwise
    """
    left_child_idx = left_child_index(index)
    right_child_idx = right_child_index(index)

    left_child_exists = left_child_idx < len(data)
    right_child_exists = right_child_idx < len(data)

    if left_child_exists and right_child_exists:
        left_child = data[left_child_idx]
        right_child = data[right_child_idx]

        return left_child < data[index] or right_child < data[index]
    elif left_child_exists and not right_child_exists:
        left_child = data[left_child_idx]
        return left_child < data[index]
    elif right_child_exists and not left_child_exists:
        right_child = data[right_child_idx]
        return right_child < data[index]
    else:
        return False


def calculate_smaller_child_index(data: List[Any], index: int) -> int:
    """
    Calculates the index of the smaller child of a heap node in the given index position in the min heap.
    Args:
        data(list): Node data
        index(int): Node index
    Returns:
        int: Index of the smaller child
    """
    # if there is no right child
    if not data[right_child_index(index)]:
        # return the left child index
        return left_child_index(index)

    # if right child value is less than left child value
    if data[right_child_index(index)] < data[left_child_index(index)]:
        # return the left child index
        return left_child_index(index)
    else:
        # if the left child value is greater or equal to right child, return the right child index.
        return right_child_index(index)
