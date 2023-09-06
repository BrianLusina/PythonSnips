from typing import List, TypeVar, Generic

T = TypeVar("T")


def selection_sort(numbers: List[Generic[T]]) -> List[Generic[T]]:
    for x in range(len(numbers)):
        lowest_number_idx = x

        for y in range(x + 1, len(numbers)):
            if numbers[y] < numbers[lowest_number_idx]:
                lowest_number_idx = y

        if lowest_number_idx != x:
            temp = numbers[x]
            numbers[x] = numbers[lowest_number_idx]
            numbers[lowest_number_idx] = temp

    return numbers
