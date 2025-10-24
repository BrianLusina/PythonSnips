from typing import List, Any


def reverse_array_in_place(collection: List[Any]):
    left_pointer = 0
    right_pointer = len(collection) - 1

    while left_pointer < right_pointer:
        left = collection[left_pointer]
        right = collection[right_pointer]

        collection[left_pointer] = right
        collection[right_pointer] = left

        left_pointer += 1
        right_pointer -= 1
