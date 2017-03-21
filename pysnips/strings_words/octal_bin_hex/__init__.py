"""
Converts a number to octal, decimal and binary equivalents from 1 up to the number(inclusive)
"""


def print_formatted(number):
    """
    formats the given number, returning its decimal equivalent, octal, hexadecimal and binary
    :param number: number to convert to octal, decimal, binary
    :return: String
    :rtype: str
    """
    # define the width
    width = len(bin(number)[2:])
    result = []
    # create a range from 1 up to the number (inclusive)
    for num in range(1, number + 1):
        # for each number convert the number to octal, binary and hexadecimal and add it to a list
        result.append(
            "{} {} {} {}".format(str(num).rjust(width), oct(num)[2:].rjust(width), hex(num)[2:].upper().rjust(width),
                                 bin(num)[2:].rjust(width)))
    # return each output on a new line
    return "\n".join(result)


def print_formatted_2(n):
    results = []

    for i in range(1, n + 1):
        decimal = str(i)
        octal = str(oct(i)[2:])
        hex_ = str(hex(i)[2:]).upper()
        binary = str(bin(i)[2:])

        results.append([decimal, octal, hex_, binary])

    width = len(results[-1][3])  # largest binary number

    for i in results:
        print(*(rep.rjust(width) for rep in i))
