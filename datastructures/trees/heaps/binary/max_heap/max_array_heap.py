from typing import Any

from datastructures.trees.heaps.array_heap import ArrayBasedHeap


class MaxArrayBasedHeap(ArrayBasedHeap):
    """
    Max Heap that uses an array as the underlying datastructure of a heap
    """

    def __init__(self):
        super().__init__()

    def insert(self, value: Any):
        """
        Inserts a value into the heap
        """
        # add the value into the last node
        self.data.append(value)

        # keep track of the index of the newly inserted node
        new_node_index = len(self.data) - 1

        # the following executes the "trickle up" algorithm. If the new node is not in the root position and it's greater
        # than its parent node
        while (
            new_node_index > 0
            and self.data[new_node_index]
            > self.data[self.get_parent_index(new_node_index)]
        ):
            # swap the new node with the parent node
            (
                self.data[self.get_parent_index(new_node_index)],
                self.data[new_node_index],
            ) = (
                self.data[new_node_index],
                self.data[self.get_parent_index(new_node_index)],
            )

            # update the index of the new node
            new_node_index = self.get_parent_index(new_node_index)

    def delete(self) -> Any:
        if len(self.data) == 0:
            raise Exception("Heap is empty")

        # we only ever delete the root node from a heap, so we pop the last node from the array and make it the root node
        root_node = self.data[0]
        self.data[0] = self.data.pop()

        # track the current index of the "trickle node". This is the node that will be moved into the correct position
        trickle_node_index = 0

        # the following loop executes the "trickle down" algorithm: We run the loop as long as the trickle node has a
        # child that is greater than it.
        while self.__has_greater_child(trickle_node_index):
            larger_child_index = self.__calculate_larger_child_index(trickle_node_index)

            # swap the trickle node with its larger child
            self.data[trickle_node_index], self.data[larger_child_index] = (
                self.data[larger_child_index],
                self.data[trickle_node_index],
            )

            trickle_node_index = larger_child_index

        return root_node

    def __has_greater_child(self, index: int) -> bool:
        """
        Checks whether the node at index has a left and right children and if either of those children are greater than
        the node at the index.
        :param index: the index to check for
        :return: True if the condition is met, false otherwise
        """
        left_child_index = self.get_left_child_index(index)
        right_child_index = self.get_right_child_index(index)

        left_child_exists = left_child_index < len(self.data)
        right_child_exists = right_child_index < len(self.data)

        if left_child_exists and right_child_exists:
            left_child = self.data[left_child_index]
            right_child = self.data[right_child_index]

            return left_child > self.data[index] or right_child > self.data[index]
        elif left_child_exists and not right_child_exists:
            left_child = self.data[left_child_index]
            return left_child > self.data[index]
        elif right_child_exists and not left_child_exists:
            right_child = self.data[right_child_index]
            return right_child > self.data[index]
        else:
            return False

    def __calculate_larger_child_index(self, index: int) -> int:
        """
        Calculates the index of the larger child of the node in the given index position in the heap.
        :param index: The index position of the larger child of this node's position
        :return: The position of the larger child
        """
        # if there is no right child
        if not self.data[self.get_right_child_index(index)]:
            # return the left child index
            return self.get_left_child_index(index)

        # if right child value is greater than left child value
        if (
            self.data[self.get_right_child_index(index)]
            > self.data[self.get_left_child_index(index)]
        ):
            # return the right child index
            return self.get_right_child_index(index)
        else:
            # if the left child value is greater or equal to right child, return the left child index.
            return self.get_left_child_index(index)
