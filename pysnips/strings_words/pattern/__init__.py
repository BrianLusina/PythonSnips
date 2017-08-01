def pattern(n):
    """
    Perform checks on the number, if 0, return an empty string,
    if 1, return a string literal of 1,
    else,find the range of the numbers and convert each to a string and repeat the string x times will adding to
     another list
    join this list with \n
    """
    return '\n'.join(['1'] + ['1' + '*' * (i - 1) + str(i)
                              for i in range(2, n + 1)]
                     )
