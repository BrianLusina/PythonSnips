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


if __name__ == "__main__":
    chars = "".join(map(str, range(0, 10)))
    index = 1000000
    lexi_perms = lexicographic_permutations(chars, index)
    p = lexi_perms[index]
    print(f"The {index}th lexicographic permutation of {chars} is {p}")
