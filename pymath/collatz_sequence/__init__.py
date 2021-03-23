"""
Collatz sequence
finds the starting number under 1M that produces the longest chain
"""


def generate_collatz_sequence(number):
    """
    Generates a Collatz sequence from the starting number
    Example(s)

    >>> generate_collatz_sequence(1)
    [1]

    >>> generate_collatz_sequence(2)
    [2, 1]

    >>> generate_collatz_sequence(13)
    [13, 40, 20, 10, 5, 16, 8, 4, 2, 1]

    :param number: Starting number
    :return: list of collatz sequence from the starting number
    :rtype: list
    """
    if number is None or not isinstance(number, int):
        raise ValueError(f"Invalid input {number}, this should be an integer")

    sequence = [number]

    if number == 1:
        return sequence

    # if the number is already 1, return it in a list
    while number != 1:

        # if the number is even, ie. number %2 == 0
        if number % 2 == 0:
            number //= 2
            sequence.append(number)

        # if number is odd
        elif number % 2 != 0:
            number = (3 * number) + 1
            sequence.append(number)

    return sequence


# TODO: add memoization to not repeat calculations for sequences, increases speed and reduces call count
def find_starting_number(limit):
    """
    Finds the starting number in a collatz seqence that produces the longest chain
    Example:

    >>> find_starting_number(1000000)
    837799

    :param limit This defines the limit we want to start checking for the starting point with the longest collatz seq
    :return: Starting number with the longest collatz sequence
    :rtype: int
    """
    if limit < 0 or limit is None:
        raise ValueError(f"Expected limit to be greater than one or not None instead found {limit}")

    if limit == 1:
        # short circuit, we already have the starting point
        return limit

    # cache = {}
    current_longest = 0
    starting_num = 0
    for x in range(limit, 1, -1):
        sequence = generate_collatz_sequence(x)
        seq_len = len(sequence)

        # cache[x] = sequence
        if seq_len > current_longest:
            current_longest = seq_len
            starting_num = x
    return starting_num


if __name__ == "__main__":
    range_limit = 1_000_000
    starting_number = find_starting_number(range_limit)
    print(f"Starting number with the longest collatz seq under {range_limit} is {starting_number}")
