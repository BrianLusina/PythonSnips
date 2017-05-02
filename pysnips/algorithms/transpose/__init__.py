def transpose(input_lines):
    """
    transposes letters in input lines like a matrix, where the columns become rows and rows
    become columns
    :param input_lines: lines to transpose
    :return: String with the characters transposed
    """
    lines = input_lines.split("\n")
    zipped = map(list, [line.ljust(len(max(lines, key=len))) for line in lines])

    return "\n".join("".join(line) for line in zip(*zipped)).strip()
