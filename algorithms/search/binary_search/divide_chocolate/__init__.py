from typing import List


def maximize_sweetness(sweetness: List[int], k: int) -> int:
    """
    Finds the maximum possible sweetness of the piece you will receive if you cut the chocolate bar optimally.
    Args:
        sweetness (List[int]): A list of sweetness values for each chunk of the chocolate bar.
        k (int): The number of friends to share the chocolate bar with.
    Returns:
        int: The maximum possible sweetness of the piece you will receive if you cut the chocolate bar optimally.
    """
    lower_bound = 1
    upper_bound = sum(sweetness) // (k + 1)

    while lower_bound < upper_bound:
        current_sweetness = 0
        pieces_count = 0
        mid = (lower_bound + upper_bound + 1) // 2

        for s in sweetness:
            current_sweetness += s
            if current_sweetness >= mid:
                pieces_count += 1
                current_sweetness = 0

        # check if pieces_count is at least k+1
        if pieces_count >= k + 1:
            lower_bound = mid
        else:
            upper_bound = mid - 1

    return lower_bound


def maximize_sweetness_2(sweetness: List[int], k: int) -> int:
    """
    Finds the maximum possible sweetness of the piece you will receive if you cut the chocolate bar optimally.
    Args:
        sweetness (List[int]): A list of sweetness values for each chunk of the chocolate bar.
        k (int): The number of friends to share the chocolate bar with.
    Returns:
        int: The maximum possible sweetness of the piece you will receive if you cut the chocolate bar optimally.
    """
    low, high = 1, sum(sweetness) // (k + 1)
    result = low
    while low <= high:
        mid = (low + high) // 2
        if can_divide(sweetness, k, mid):
            result = mid
            low = mid + 1
        else:
            high = mid - 1
    return result


def can_divide(sweetness: List[int], k: int, min_sweetness: int) -> bool:
    total_sweetness, pieces = 0, 0
    for sweet in sweetness:
        total_sweetness += sweet
        if total_sweetness >= min_sweetness:
            pieces += 1
            total_sweetness = 0
    return pieces >= k + 1
