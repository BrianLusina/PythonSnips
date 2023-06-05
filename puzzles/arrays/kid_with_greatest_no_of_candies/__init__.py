from typing import List


def kids_with_candies(candies: List[int], extra_candies: int) -> List[bool]:
    result = []

    current_max = max(candies)

    for candy in candies:
        additional_candies = candy + extra_candies
        if additional_candies >= current_max:
            result.append(True)
        else:
            result.append(False)

    return result
