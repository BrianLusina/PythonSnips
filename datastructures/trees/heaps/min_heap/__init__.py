from heapq import heappush, heappop, nsmallest, heapify
from typing import Any


class MinHeap:
    def __init__(self, heap=None):
        if heap is None:
            heap = []
        self.heap = heap
        heapify(self.heap)

    @staticmethod
    def parent(i):
        return (i - 1) / 2

    def insert(self, value):
        """
        Inserts a value into the heap
        """
        heappush(self.heap, value)

    def decrease_value_at(self, index, new_val):
        """
        Decrease value of key at index 'index' to new_val
        It is assumed that new_val is smaller than heap[i]
        """
        self.heap[index] = new_val
        while index != 0 and self.heap[self.parent(index)] > self.heap[index]:
            # Swap heap[i] with heap[parent(i)]
            self.heap[index], self.heap[self.parent(index)] = self.heap[self.parent(index)], self.heap[index]

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

    def peek(self):
        """
        Gets the smallest item in the heap
        """
        return nsmallest(1, self.heap)[0]

    def size(self):
        """
        Returns the size of the heap
        """
        return len(self.heap)
