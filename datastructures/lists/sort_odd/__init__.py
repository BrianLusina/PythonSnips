from cProfile import Profile, run
from collections import deque


def sort_array(arr):
    """
    Sorts only the odd numbers leaving the even numbers in place
    :param: arr Array of numbers
    :return sorted numbers with only the odds sorted by value and evens retain their place
    :rtype: list
    """
    odds = sorted([x for x in arr if x % 2], reverse=True)
    return [x if x % 2 == 0 else odds.pop() for x in arr]


def sort_array_2(arr):
    """
    Another variation of sorting odd numbers and leaving even numbers in place.
    This uses deque to increases performances on pop operations on the sorted odds array
    :param: arr Array of numbers
    :return: List of numbers having only the odd numbers sorted
    :rtype: list
    """
    sorted_odds = deque(sorted(x for x in arr if x % 2))
    return [x if x % 2 == 0 else sorted_odds.popleft() for x in arr]


if __name__ == "__main__":
    profile = Profile()
    source_array = [1, 3, 4, 5, 6, 7, 8, 9, 2, 3, 5, 6, 8, 9, 0]
    print(f"Sorted array of {source_array} using implementation 2 is {sort_array(source_array)}")
    print(f"Profile stats for 1st implementation")
    run("sort_array(source_array)")
    print(f"{'-' * 100}")
    print(f"Sorted array of {source_array} using implementation 3 is {sort_array_2(source_array)}")
    print(f"Profile stats for 2nd implementation")
    run("sort_array(source_array)")
