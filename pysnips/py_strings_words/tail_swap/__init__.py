def tail_swap(word_list):
    """
    Creates a format for the final replacement
    Picks the head and tail for each string in the list via tuple unpacking
    Swaps the tails using the format created.
    :param word_list: The word list with 2 strings which contain exactly 1 colon
    :return: a list with the tails of each string swapped
    :rtype: list
    """
    # create a format for final replacement
    fmt = '{}:{}'.format

    # pick the head and tail for each word in the list
    (head, tail), (head_2, tail_2) = (a.split(':') for a in word_list)

    # return the formatted list
    return [fmt(head, tail_2), fmt(head_2, tail)]
