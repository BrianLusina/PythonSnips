def make_diamond(letter):
    """
    makes a diamond from the given letter
    :return: a diamond
    :rtype: list
    """
    diamond = None

    # count how far the letter is from A and use that as counter
    size = ord(letter.upper()) - ord('A')

    for i in range(size, -1, -1):
        # gets 1 half of the top of the diamond
        half_row = ' ' * i + chr(i + ord('A')) + ' ' * (size - i)

        # gets the bottom half of the diamond
        row = ''.join(half_row[:0:-1]) + half_row

        if diamond:
            diamond = [row] + diamond + [row]
        else:
            diamond = [row]

    return "\n".join(diamond) + "\n"
