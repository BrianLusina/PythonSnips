"""
Find the lexicographic permutations of a given list of characters
"""
from itertools import permutations


def lexicographic_permutations(input_):
    """
    Finds the lexicographic permutations of a given array of characters
    :param input_: string input
    :type input_ str
    :return: List of permutations for the given input
    :rtype: list
    """
    return sorted(map(lambda x: "".join(x), permutations(input_)))


if __name__ == "__main__":
    chars = "".join(map(str, range(0, 10)))
    index = 1000000
    lexi_perms = lexicographic_permutations(chars)
    p = lexi_perms[index]
    print(f"The {index}th lexicographic permutation of {chars} is {p}")
