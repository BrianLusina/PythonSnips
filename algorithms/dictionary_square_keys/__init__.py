def square_keys():
    """
    :return: the square values of each dictionary key
    """
    d, out = dict(), ""
    for i in range(1, 21):
        d[i] = i ** 2
    for (_, v) in d.items():
        out += str(v) + "\n"
    return out
