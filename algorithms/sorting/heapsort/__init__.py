def left_child_index(parent_index):
    return parent_index * 2 + 1


def right_child_index(parent_index):
    return parent_index * 2 + 2


def bubble_down(heap, heap_length, index):
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
            heap[index], heap[larger_child_index] = heap[larger_child_index], heap[index]

            # continue bubbling down
            index = larger_child_index
        else:
            # we're larger than both children, so we're done
            break


def remove_max(heap, heap_length):
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


def heapify(the_list):
    # bubble down from the leaf nodes up to the top
    for index in range(len(the_list) - 1, -1, -1):
        bubble_down(the_list, len(the_list), index)


def heapsort(the_list: list):
    heapify(the_list)

    heap_size = len(the_list)

    while heap_size > 0:
        # Remove the largest item and update the heap size
        largest_size = remove_max(the_list, heap_size)
        heap_size -= 1

        # store the removed value at the end of the list,
        # after the entries used by the heap
        the_list[heap_size] = largest_size
