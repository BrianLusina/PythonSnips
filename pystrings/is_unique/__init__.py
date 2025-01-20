from collections import defaultdict
from typing import DefaultDict


def is_unique(input_str: str) -> bool:
    """
    Checks if the input string contains unique characters.
    Args:
        input_str (str): the input string to evaluate
    Returns:
        bool: True if the input string contains unique characters, False otherwise.
    """
    frequency_map: DefaultDict[str, int] = defaultdict(int)

    for char in input_str:
        if char not in frequency_map:
            frequency_map[char] = 1
        else:
            return False

    return True
