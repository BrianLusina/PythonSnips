# todo: add tests
def get_permutations(word):
    """
    Gets the permutations of word recursively
    :param word: the word to get permutations of
    :return: a set of all posibble permutations of the word
    :rtype: set
    """

    # base case
    if len(word) <= 1:
        return {word}

    all_chars_except_last = word[:-1]
    last_char = word[-1]

    # recursive call: get all possible permutations except last
    permutations_of_all_chars_except_last = get_permutations(all_chars_except_last)

    # get the last character in all possible positions in each of the above permutations
    permutations = set()
    for permutation_of_all_chars_except_last in permutations_of_all_chars_except_last:
        for position in range(len(all_chars_except_last) + 1):
            permutation = permutation_of_all_chars_except_last[
                          :position] + last_char + permutation_of_all_chars_except_last[position:]

            permutations.add(permutation)

    return permutations


# example output
print(get_permutations("word"))
