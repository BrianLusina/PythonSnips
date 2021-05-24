from .max_heap import MaxHeap
from .min_heap import MinHeap


def min_heapify(heap: MaxHeap, idx: int) -> MinHeap:
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


def convert_max_to_min(max_heap: MaxHeap) -> MinHeap:
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
