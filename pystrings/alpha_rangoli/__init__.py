from string import ascii_lowercase


def print_rangoli(size):
    """
    prints alphabet rangoli based on the size given
    :param size the size of the rangoli pattern to print
    :return alphabet rangoli pattern
    :rtype: str
    """
    result = []
    for x in range(size):
        alpha = "-".join(ascii_lowercase[x:size])
        result.append((alpha[::-1] + alpha[1:]).center(4 * size - 3, "-"))
    return "\n".join(result[:0:-1] + result)
