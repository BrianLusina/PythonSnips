from typing import Any, List, Optional

from algorithms.sorting.heapsort import heapsort, heapify, right_child_index
from datastructures.trees.heaps import ArrayBasedHeap
from datastructures.trees.heaps.utils import has_smaller_child


class MinArrayBasedHeap(ArrayBasedHeap):
    """
    Min Heap that uses an array as the underlying data structure of a heap
    """

    def __init__(self, data: Optional[List[Any]] = None):
        built_heap = self.build_heap(data)
        super().__init__(built_heap)

    @staticmethod
    def swap(i: int, j: int, data: List[Any]) -> None:
        """
        Swaps the elements at index i and j in place
        Args:
            i (int): index of element to swap
            j (int): index of element to swap
            data (List[Any]): data to swap
        Returns:
            None
        """
        data[i], data[j] = data[j], data[i]

    def bubble_up(self, current_idx: int, data: List[Any]) -> None:
        """
        Bubble up one element at index current_idx. Incurs time complexity of O(log n) and space of O(1)
        Args:
            current_idx (int): index of element to bubble up
            data (List[Any]): data to bubble
        Returns:
            None
        """
        parent_idx = self.get_parent_index(current_idx)
        while current_idx > 0 and data[current_idx] < data[parent_idx]:
            self.swap(current_idx, parent_idx, data)
            current_idx = parent_idx
            parent_idx = (current_idx - 1) // 2

    def bubble_down(self, current_idx: int, end_idx: int, data: List[Any]) -> None:
        left_idx = self.get_left_child_index(current_idx)
        while left_idx <= end_idx:
            idx = self.get_right_child_index(current_idx)
            right_idx = idx if idx <= end_idx else -1
            if right_idx != -1 and data[right_idx] < data[left_idx]:
                idx_to_swap = right_idx
            else:
                idx_to_swap = left_idx
            if data[idx_to_swap] < data[current_idx]:
                self.swap(current_idx, idx_to_swap, data)
                current_idx = idx_to_swap
                left_idx = self.get_left_child_index(current_idx)
            else:
                break

    def build_heap(self, data: List[Any]) -> List[Any]:
        """
        Build a heap from a list
        """
        if not data:
            return []
        first_parent_idx = (len(data) - 2) // 2

        for currentIdx in reversed(range(first_parent_idx + 1)):
            self.bubble_down(currentIdx, len(data) - 1, data)
        return data

    def insert(self, value: Any):
        """
        Inserts a value into the heap
        """
        # add the value into the last node
        self.heap.append(value)

        # keep track of the index of the newly inserted node
        new_node_index = len(self.heap) - 1

        # the following executes the "trickle down" algorithm. If the new node is not in the root position and it's less
        # than its parent node
        while (
            new_node_index > 0
            and self.heap[new_node_index]
            < self.heap[self.get_parent_index(new_node_index)]
        ):
            # swap the new node with the parent node
            (
                self.heap[self.get_parent_index(new_node_index)],
                self.heap[new_node_index],
            ) = (
                self.heap[new_node_index],
                self.heap[self.get_parent_index(new_node_index)],
            )

            # update the index of the new node
            new_node_index = self.get_parent_index(new_node_index)

    def delete(self) -> Any:
        if len(self.heap) == 0:
            raise Exception("Heap is empty")

        # we only ever delete the root node from a heap, so we pop the last node from the array and make it the root node
        root_node = self.heap[0]
        # Note that this operation of popping an element from the last item in a list is O(1) operation, however,
        # making the first item in the list the popped element is an O(n) operation where n is the size of the list. This
        # is because the system has to "shift" each element in the array to the right
        self.heap[0] = self.heap.pop()

        # track the current index of the "trickle node". This is the node that will be moved into the correct position
        trickle_node_index = 0

        # the following loop executes the "trickle up" algorithm: We run the loop as long as the trickle node has a
        # child that is less than it.
        while self.__has_smaller_child(trickle_node_index):
            smaller_child_index = self.__calculate_smaller_child_index(
                trickle_node_index
            )

            # swap the trickle node with its smaller child
            self.heap[trickle_node_index], self.heap[smaller_child_index] = (
                self.heap[smaller_child_index],
                self.heap[trickle_node_index],
            )

            trickle_node_index = smaller_child_index

        return root_node

    def __has_smaller_child(self, index: int) -> bool:
        """
        Checks whether the node at the given index has left and right children and if either of those children are less
        than the node at the given index.
        :param index: the index to check for
        :return: True if the condition is met, false otherwise
        """
        left_child_idx = self.get_left_child_index(index)
        right_child_idx = self.get_right_child_index(index)

        left_child_exists = left_child_idx < len(self.heap)
        right_child_exists = right_child_idx < len(self.heap)

        if left_child_exists and right_child_exists:
            left_child = self.heap[left_child_idx]
            right_child = self.heap[right_child_idx]

            return left_child < self.heap[index] or right_child < self.heap[index]
        elif left_child_exists and not right_child_exists:
            left_child = self.heap[left_child_idx]
            return left_child < self.heap[index]
        elif right_child_exists and not left_child_exists:
            right_child = self.heap[right_child_idx]
            return right_child < self.heap[index]
        else:
            return False

    def __calculate_smaller_child_index(self, index: int) -> int:
        """
        Calculates the index of the smaller child of the node in the given index position in the heap.
        :param index: The index position of the larger child of this node's position
        :return: The position of the larger child
        """
        # if there is no right child
        right_child_idx = self.get_right_child_index(index)
        left_child_idx = self.get_left_child_index(index)

        if right_child_idx < len(self.heap) and not self.heap[right_child_idx]:
            # return the left child index
            return left_child_idx

        # if right child value is less than left child value
        if (
            right_child_idx < len(self.heap)
            and self.heap[right_child_idx] < self.heap[left_child_idx]
        ):
            # return the left child index
            return left_child_idx
        else:
            # if the left child value is greater or equal to right child, return the right child index.
            return right_child_idx
