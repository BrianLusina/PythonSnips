from itertools import combinations, permutations


def solve(puzzle):
    """
    Solve a given phrase and return a dictionary with the keys as letters and values as numbers
    :param puzzle: String to solve
    :return: dictionary
    :rtype: dict
    """
    # get a set of letters and map 0-9 range to a string
    letters = set(char for char in puzzle if char.isupper())  # retrieves letters from the puzzle
    numbers = map(str, range(10))  # returns a map object of string numbers from 0-9

    # will produce combinations of numbers using length of the letters
    # so, if letters has a length of 3, then c will be 012
    for c in combinations(numbers, len(letters)):
        for p in permutations(c):
            subs = dict(zip(letters, p))
            if test_equation(puzzle, subs):
                return {k: int(v) for k, v in subs.items()}

    # we could not find a solution
    return {}


def test_equation(puzzle, substitution):
    """
    test the equation given the puzzle and the subsitution
    :param puzzle:
    :param substitution:
    :return: True if equation checks out
    :rtype: bool
    """
    equation = "".join(substitution.get(char) or char for char in puzzle)
    left, right = equation.split(" == ")
    left_numbers = left.split(" + ")

    if check_leading_zeros(right, *left_numbers):
        return False

    return sum(map(int, left_numbers)) == int(right)


def check_leading_zeros(*numbers):
    return any(n[0] == "0" for n in numbers)
