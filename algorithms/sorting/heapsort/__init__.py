from typing import List, Any


def left_child_index(parent_index: int) -> int:
    return parent_index * 2 + 1


def right_child_index(parent_index: int) -> int:
    return parent_index * 2 + 2


def bubble_down(heap: List, heap_length: int, index: int):
    """
    Restore a max heap where the value at index may be out of place
    """
    while index < heap_length:
        left_index = left_child_index(index)
        right_index = right_child_index(index)

        # if we don't have any child nodes, we can stop
        if left_index >= heap_length:
            break

        # Find the larger of the 2 children
        larger_child_index = left_index

        if right_index < heap_length and heap[left_index] < heap[right_index]:
            larger_child_index = right_index

        if heap[index] < heap[larger_child_index]:
            heap[index], heap[larger_child_index] = (
                heap[larger_child_index],
                heap[index],
            )

            # continue bubbling down
            index = larger_child_index
        else:
            # we're larger than both children, so we're done
            break


def remove_max(heap: List, heap_length: int):
    """
    Remove and return the largest item from a heap
    Updates the heap in-place, maintaining validity
    """

    # Grab the largest value from the root
    max_value = heap[0]

    # Move the last item in the heap into the root position
    heap[0] = heap[heap_length - 1]

    bubble_down(heap, heap_length - 1, 0)

    return max_value


def heapify(the_list: List[Any]):
    # bubble down from the leaf nodes up to the top
    for index in range(len(the_list) - 1, -1, -1):
        bubble_down(the_list, len(the_list), index)


def heapify_2(the_list: List[Any], n: int, i: int):
    # Assume the current index i is the largest
    largest = i
    # index of left child
    left = 2 * i + 1
    # index of right child
    right = 2 * i + 2

    # Check if the left child exists and is greater than the current largest
    if left < n and the_list[left] > the_list[largest]:
        largest = left

    # Check if the right child exists and is greater than the current largest
    if right < n and the_list[right] > the_list[largest]:
        largest = right

    # If the largest is not the root, swap and continue heapifying the affected subtree
    if largest != i:
        # swap
        the_list[i], the_list[largest] = the_list[largest], the_list[i]
        # recursively heapify the sub-tree
        heapify_2(the_list, n, largest)


def heapsort(the_list: List[Any]):
    heapify(the_list)

    heap_size = len(the_list)

    while heap_size > 0:
        # Remove the largest item and update the heap size
        largest_size = remove_max(the_list, heap_size)
        heap_size -= 1

        # store the removed value at the end of the list,
        # after the entries used by the heap
        the_list[heap_size] = largest_size


def heapsort_2(the_list: List[Any]) -> List[Any]:
    n = len(the_list)
    # Step 1: Build a max heap from the input array
    # (Start from the last non-leaf node and heapify each one)
    for i in range(n // 2 - 1, -1, -1):
        heapify_2(the_list, n, i)
    # Step 2: Extract elements one by one from the heap
    # Move the current root (largest element) to the end,
    # then reduce the heap size and re-heapify the root
    for i in range(n - 1, 0, -1):
        # move current max to the end
        the_list[0], the_list[i] = the_list[i], the_list[0]
        # heapify reduced heap
        heapify_2(the_list, i, 0)
    # Return the sorted array (ascending order)
    return the_list
