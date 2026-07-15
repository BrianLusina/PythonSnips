from typing import List


def rescue_boats(people: List[int], limit: int) -> int:
    """
    Finds the minimum number of rescue boats that can be used to save people from a sinking ship. Note that the assumption
    made here is that the number of boats is unlimited
    Args:
        people (list): list of weights of people
        limit (int): weight limit of each boat
    Returns:
        int: minimum number of rescue boats required
    """
    # copy over the people list to avoid mutating the input list
    weights = people[:]
    # sort the list of weights
    weights.sort()

    # using two pointers to move along the weights to be able to track pairs of people, the left pointer will be at 0
    # initially, i.e. at the lighter person and the right pointer will be at the end of the list, which will be the heavier
    # person
    left_pointer, right_pointer = 0, len(weights) - 1

    # this keeps track of the total rescue boats that will be used
    boats = 0

    while left_pointer <= right_pointer:
        lightest = weights[left_pointer]
        heaviest = weights[right_pointer]
        current_weight = lightest + heaviest
        # If the current weight is less than the limit of a single boat
        if current_weight <= limit:
            # move to the next heavier person and back down the heavier scale
            left_pointer += 1
        # the heavier person boards the boat and we move the right pointer
        right_pointer -= 1

        # either way, we increment the number of boats
        boats += 1

    return boats
