from typing import List


def has_single_cycle(array: List[int]) -> bool:
    """
    Checks if the provided array has a single cycle.
    Args:
        array (List[int]): list of integers.
    Returns:
        bool: True if the given array has a single cycle, False otherwise.
    """
    n = len(array)

    def get_next_index(current_idx: int) -> int:
        jump = array[current_idx]
        next_index = (jump + current_idx) % n
        return next_index if next_index >= 0 else next_index + n

    number_of_elements_visited = 0
    current_index = 0
    while number_of_elements_visited < n:
        if number_of_elements_visited > 0 and current_index == 0:
            return False
        number_of_elements_visited += 1
        current_index = get_next_index(current_index)

    return current_index == 0
