from heapq import heappop, heapify
from typing import Any, List, Union

from .. import HeapNode, Heap


class MaxHeap(Heap):
    def __init__(self, heap: List[HeapNode] = None):
        super().__init__()
        if heap is None:
            heap = []
        self.heap = self.build_heap(heap)
        heapify(self.heap)

    def __len__(self):
        return len(self.heap)

    def __getitem__(self, item):
        raise NotImplementedError("Not yet implemented")

    def __setitem__(self, key, value):
        raise NotImplementedError("Not yet implemented")

    def __find_smaller_child(self, index: int) -> int:
        left_child_index = self.get_left_child_index(index)
        right_child_index = self.get_right_child_index(index)

        # no right child
        if right_child_index > len(self.heap):
            # not left child
            if left_child_index >= len(self.heap):
                return -1
            # left child only
            else:
                return left_child_index
        else:
            # compare left & right children
            if self.heap[left_child_index] < self.heap[right_child_index]:
                return left_child_index
            else:
                return right_child_index

    def __bubble_down(self, idx: int):
        min_child_index = self.__find_smaller_child(idx)

        if min_child_index == -1:
            return

        if self.heap[idx] > self.heap[min_child_index]:
            self.heap[idx], self.heap[min_child_index] = self.heap[min_child_index], self.heap[idx]
            self.idx_of_element[self.heap[min_child_index]], self.idx_of_element[self.heap[idx]] = (
                self.idx_of_element[self.idx_of_element[self.heap[idx]]],
                self.idx_of_element[self.idx_of_element[self.heap[min_child_index]]])

            self.__bubble_down(min_child_index)

    def __bubble_up(self, idx: int):
        if idx == 0:
            return
        parent_idx = (idx - 1) // 2
        if self.heap[idx] < self.heap[parent_idx]:
            # swap indices & recurse
            self.heap[idx], self.heap[parent_idx] = self.heap[parent_idx], self.heap[idx]
            self.idx_of_element[self.heap[parent_idx]], self.idx_of_element[self.heap[idx]] = (
                self.idx_of_element[self.idx_of_element[self.heap[idx]]],
                self.idx_of_element[self.idx_of_element[self.heap[parent_idx]]])

            self.__bubble_up(parent_idx)

    def build_heap(self, array: List[HeapNode]) -> List[HeapNode]:
        last_idx = len(array) - 1
        start_from = self.get_parent_index(last_idx)

        for idx, node in enumerate(array):
            self.idx_of_element[node] = idx
            self.heap_dict[node.name] = node.data

        for i in range(start_from, -1, -1):
            self.__bubble_down(i)

        return array

    def insert_data(self, data: Any):
        """
        Inserts a value into the heap
        """
        if data is None:
            raise TypeError("Data item can not be None")
        node = HeapNode(data, data.__name__)
        self.heap.append(node)
        self.__bubble_up(len(self.heap) - 1)

    def insert_node(self, node: HeapNode):
        pass

    def decrease_value_at(self, index, new_val):
        """
        Decrease value of key at index 'index' to new_val
        It is assumed that new_val is smaller than heap[i]
        """
        self.heap[index] = new_val
        while index != 0 and self.heap[self.get_parent_index(index)] > self.heap[index]:
            # Swap heap[i] with heap[parent(i)]
            self.heap[index], self.heap[self.get_parent_index(index)] = self.heap[self.get_parent_index(index)], \
                                                                        self.heap[index]

    def remove_min(self) -> Any:
        """
        Removes and returns the smallest value in the Heap
        """
        return heappop(self.heap)

    def delete_key(self, index):
        """
        Deletes key at index "index". It first reduces value to minus infinite and then calls remove_min
        """
        self.decrease_value_at(index, float("-inf"))
        self.remove_min()

    def get_minimum(self):
        """
        Returns the minimum value in the heap without removing it
        """
        return self.heap[0]

    def is_empty(self) -> bool:
        """
        Checks if the heap is empty
        """
        return len(self.heap) == 0

    def peek(self) -> Union[HeapNode, None]:
        """
        Gets the smallest item in the heap
        """
        return self.heap[0] if self.heap else None

    def size(self):
        """
        Returns the size of the heap
        """
        return len(self.heap)
