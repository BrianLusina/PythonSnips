"""
Find the lexicographic permutations of a given list of characters
"""
from itertools import permutations


def lexicographic_permutations(input_, index):
    """
    Finds the lexicographic permutations of a given array of characters
    :param input_: string input
    :type input_ str
    :param index: the index of the lexicographic permutation to return
    :type: int
    :return: List of permutations for the given input
    :rtype: list
    """
    count = 0
    result = ""
    for permutation in permutations(input_, len(input_)):
        count += 1
        if count == index:
            result = permutation
            break

    return "".join(result)
